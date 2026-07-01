# 💰 Finance & Accounting

> Replace: a bookkeeper + an AP/AR clerk + a FP&A analyst + your invoicing SaaS.

A self-hosted finance stack can run invoicing, bookkeeping, expense capture, and
financial research end-to-end. Pair the tools below with an LLM (see the
[Quickstart](../../docs/quickstart.mdx)) to auto-extract receipts, categorize
transactions, and answer "how are we doing this month?" in plain English.

**Recommended starter stack:** Invoice Ninja (invoicing) + Paperless-ngx (receipt/invoice OCR) + Firefly III or Actual (books & budgets). Add OpenBB when you need real financial analysis.

---

### [ERPNext](https://github.com/frappe/erpnext)

> Full open-source ERP: accounting, invoicing, orders, inventory, manufacturing, and assets in one system.

| | |
|---|---|
| **Stars** | ~36k |
| **Replaces** | SAP / NetSuite / QuickBooks Enterprise — a whole finance + ops back office |
| **Self-host** | Medium — multi-service `frappe_docker` compose |
| **Ship in** | ~half a day to an eval deploy |
| **Stack** | Python + JS (Frappe / MariaDB) |
| **License** | GPL-3.0 |

**Why it's on the list:** the most complete open-source ERP. Heavier to run, but nothing else replaces this much SaaS at once.

### [OpenBB](https://github.com/OpenBB-finance/OpenBB)

> Open-source financial data + analysis platform; feeds an AI analyst via Python, REST, Excel, or MCP.

| | |
|---|---|
| **Stars** | ~70k |
| **Replaces** | Bloomberg Terminal / Refinitiv for research & analysis |
| **Self-host** | Medium — run the FastAPI backend locally |
| **Ship in** | 1–2 hours |
| **Stack** | Python (FastAPI) |
| **License** | AGPL-3.0 |

**Why it's on the list:** the single best base for an AI FP&A/analyst agent — clean data access an LLM can drive.

### [Actual Budget](https://github.com/actualbudget/actual)

> Local-first, very fast budgeting and personal/SMB finance with multi-device sync.

| | |
|---|---|
| **Stars** | ~27k |
| **Replaces** | YNAB / Mint |
| **Self-host** | Easy — Docker image + sync-server |
| **Ship in** | ~30 min |
| **Stack** | TypeScript / Node |
| **License** | MIT |

**Why it's on the list:** MIT-licensed, delightful UX, trivial to host. Best default for budgets.

### [Firefly III](https://github.com/firefly-iii/firefly-iii)

> Self-hosted finance manager for income, expenses, and budgets with a strong rules engine and API.

| | |
|---|---|
| **Stars** | ~24k |
| **Replaces** | Mint / YNAB; SMB bookkeeping |
| **Self-host** | Easy — official Docker + compose |
| **Ship in** | ~1 hour |
| **Stack** | PHP / Laravel |
| **License** | AGPL-3.0 |

**Why it's on the list:** its API and rule engine make it easy to plug an LLM in for auto-categorization.

### [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx)

> Document management with OCR — turn physical receipts and invoices into a searchable, taggable archive.

| | |
|---|---|
| **Stars** | ~43k |
| **Replaces** | Manual receipt filing / commercial DMS |
| **Self-host** | Easy — compose + install script |
| **Ship in** | ~1 hour |
| **Stack** | Python (Django) + Angular |
| **License** | GPL-3.0 |

**Why it's on the list:** the perfect front door for AI receipt/invoice extraction. OCR in, structured data out.

### [Invoice Ninja](https://github.com/invoiceninja/invoiceninja)

> Invoicing, quotes, projects, and time-tracking for freelancers and small businesses.

| | |
|---|---|
| **Stars** | ~10k |
| **Replaces** | FreshBooks / Bill.com invoicing |
| **Self-host** | Easy — official Docker image |
| **Ship in** | ~1 hour |
| **Stack** | PHP / Laravel |
| **License** | Elastic License (source-available) |

**Why it's on the list:** fastest path to sending real invoices you get paid on. Note the source-available license.

### [Akaunting](https://github.com/akaunting/akaunting)

> Online accounting for small businesses — invoicing, expenses, budgeting, plus an app store.

| | |
|---|---|
| **Stars** | ~10k |
| **Replaces** | QuickBooks / Xero for SMB bookkeeping |
| **Self-host** | Medium — standard Laravel/PHP/DB setup |
| **Ship in** | 1–2 hours |
| **Stack** | PHP / Laravel + Vue |
| **License** | BSL (Business Source License) |

**Why it's on the list:** double-entry accounting with an extensible marketplace. Check the BSL terms for commercial use.

### [Documenso](https://github.com/documenso/documenso)

> Open-source DocuSign alternative — sign finance approvals, agreements, and vendor docs.

| | |
|---|---|
| **Stars** | ~14k |
| **Replaces** | DocuSign / Adobe Sign |
| **Self-host** | Easy — official Docker + compose |
| **Ship in** | ~1 hour |
| **Stack** | TypeScript / Prisma |
| **License** | AGPL-3.0 |

**Why it's on the list:** finance runs on signatures. This closes the loop, self-hosted.

---

📘 **Deploy guide:** [Ship an AI finance back-office](../../docs/departments/finance.mdx)
🏭 **Industry cross-links:** [Fintech](../../industries/README.md#fintech)
