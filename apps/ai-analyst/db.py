"""Load a CSV into an in-memory SQLite table and run read-only queries."""
from __future__ import annotations

import csv
import re
import sqlite3
from pathlib import Path

TABLE = "data"


def _is_number(v: str) -> bool:
    try:
        float(v)
        return True
    except (TypeError, ValueError):
        return False


class DataStore:
    def __init__(self, csv_path: str | Path):
        self.csv_path = Path(csv_path)
        self.conn = sqlite3.connect(":memory:", check_same_thread=False)
        self.columns: list[str] = []
        self.numeric: set[str] = set()
        self._load()

    def _load(self) -> None:
        with self.csv_path.open(newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f))
        self.columns = rows[0]
        body = rows[1:]

        # Infer numeric columns from the first data row.
        if body:
            for i, col in enumerate(self.columns):
                if all(_is_number(r[i]) for r in body if len(r) > i and r[i] != ""):
                    self.numeric.add(col)

        col_defs = ", ".join(
            f'"{c}" {"REAL" if c in self.numeric else "TEXT"}' for c in self.columns
        )
        self.conn.execute(f"CREATE TABLE {TABLE} ({col_defs})")
        placeholders = ", ".join("?" for _ in self.columns)
        self.conn.executemany(f"INSERT INTO {TABLE} VALUES ({placeholders})", body)
        self.conn.commit()

    def schema(self) -> str:
        cols = ", ".join(f"{c} ({'num' if c in self.numeric else 'text'})" for c in self.columns)
        return f"Table `{TABLE}` with columns: {cols}"

    def run_sql(self, sql: str) -> dict:
        """Execute a single read-only SELECT and return columns + rows."""
        if not re.match(r"^\s*select\b", sql, re.IGNORECASE):
            raise ValueError("Only SELECT queries are allowed.")
        if ";" in sql.rstrip(";"):
            raise ValueError("Only a single statement is allowed.")
        cur = self.conn.execute(sql)
        cols = [d[0] for d in cur.description]
        rows = [list(r) for r in cur.fetchall()]
        return {"columns": cols, "rows": rows, "sql": sql}

    def summary(self) -> dict:
        (count,) = self.conn.execute(f"SELECT COUNT(*) FROM {TABLE}").fetchone()
        stats = {}
        for col in self.numeric:
            row = self.conn.execute(
                f'SELECT SUM("{col}"), AVG("{col}"), MIN("{col}"), MAX("{col}") FROM {TABLE}'
            ).fetchone()
            stats[col] = {"sum": row[0], "avg": round(row[1], 2) if row[1] else 0, "min": row[2], "max": row[3]}
        return {"rows": count, "columns": self.columns, "numeric_stats": stats}
