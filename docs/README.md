# AI Workforce — Docs & Tutorials

These are the deploy guides for [AI Workforce](../README.md). They're plain
Markdown/MDX with frontmatter, so they render on GitHub **and** publish to
[hub.arunrajiah.com](https://hub.arunrajiah.com).

- [`index.mdx`](index.mdx) — the docs landing page
- [`quickstart.mdx`](quickstart.mdx) — the shared foundation every app needs
- [`departments/`](departments/) — one deploy guide per department

## Publishing to a hub (Docusaurus / Next.js / Nextra)

Every file uses standard frontmatter (`title`, `description`, `slug`,
`sidebar_label`, `keywords`). To publish:

- **Docusaurus:** point `docs.path` at this folder (or symlink it into `docs/`). The `slug` fields map cleanly to routes.
- **Nextra / Next.js:** drop the `.mdx` files into your `pages/` or `content/` tree; the frontmatter is read by most MDX loaders.
- **Astro Starlight:** copy into `src/content/docs/`; `title`/`description` are used as-is.

Relative links between guides use `slug`-style paths (e.g. `/departments/sales`)
so they work once mounted at the docs root. On GitHub they resolve via the folder
structure.
