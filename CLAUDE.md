# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

This repository is the source for **rrmesh.net**, the public website for the Rock River Mesh community (regional Meshtastic / MeshCore mesh network). It is a **MkDocs Material** static site — there is no application backend in this repo. Authoring is done in Markdown under `docs/`, with a small amount of Jinja/HTML/CSS in `overrides/` for theme customization.

## Common commands

A Python venv lives at `.venv/`. Activate it (or use `.venv/bin/<cmd>` directly) for all commands below.

- Install deps: `pip install -r requirements.txt`
- Local dev server (live reload): `mkdocs serve` — defaults to http://127.0.0.1:8000
- Production build: `mkdocs build` — outputs to `site/` (gitignored)
- Strict build (treat warnings as errors, mirrors what CI effectively expects): `mkdocs build --strict`
- Deploy (CI does this automatically; do not run locally): `mkdocs gh-deploy --force`

`requirements.txt` is fully pinned. When adding a plugin, pin its version and confirm it loads under `mkdocs build --strict`.

## Deployment

GitHub Actions (`.github/workflows/ci.yml`) runs on every push to `main` (or `master`) and deploys to the `gh-pages` branch via `mkdocs gh-deploy --force`. There is no preview environment — merges to `main` go live. `docs/CNAME` pins the custom domain `rrmesh.net`.

## Architecture and conventions

### Content structure

`mkdocs.yml`'s `nav:` is the source of truth for site navigation; new pages must be added there or they will only appear via direct URL. The structure mirrors `docs/`:

- `docs/index.md` — landing page (grid cards)
- `docs/portal.md` — uses a custom template (see Theme overrides below) to embed the live mesh map
- `docs/meshcore/`, `docs/meshtastic/` — protocol-specific guides
- `docs/resources/` — community resources, including `.drawio` templates rendered via the `mkdocs-drawio` plugin

`validation:` in `mkdocs.yml` is set to **warn** on omitted files, unrecognized links, and bad anchors. Don't introduce broken cross-links — `mkdocs build --strict` will fail.

A redirect is configured: `meshtastic/map.md` → `portal.md` (via `mkdocs-redirects`). Preserve this if reorganizing the portal page.

### Theme overrides (`overrides/`)

The `material` theme is customized via `theme.custom_dir: overrides`. Two patterns are in use:

1. **Partial overrides** (`overrides/partials/header.html`, `nav.html`) — copies of upstream Material partials. When updating these, diff against the same partial in the installed `mkdocs-material` version to avoid drifting from upstream fixes.
2. **Page-level templates** (`overrides/portal.html`) — used by setting `template: portal.html` in a page's front matter (see `docs/portal.md`). `portal.html` embeds `https://portal.rrmesh.net/embed/...` in a full-bleed iframe and bridges the Material light/dark theme into the iframe via `postMessage`. The CSS in this file deliberately overrides Material's `.md-main` / `.md-content` layout to make the iframe fill the viewport — be careful when touching it.

`main.html` at the repo root is the Material convention for global block overrides; currently it only extends `base.html` and exists as a hook for future use.

### Diagrams

`.drawio` files under `docs/` are rendered client-side by the `mkdocs-drawio` plugin, which depends on `viewer-static.min.js` loaded via `extra_javascript`. `assets/javascripts/drawio-reload.js` re-runs the drawio viewer on Material's instant navigation (`document$.subscribe`) — without it, diagrams disappear when navigating between pages without a full reload. Keep this if `navigation.instant` stays enabled.

### Third-party embeds

The portal iframe points at `portal.rrmesh.net` (a separate service, not in this repo). The page assumes the portal supports `updateThemeLight` / `updateThemeDark` `postMessage` events and emits `iframeNavigationStart` back. Changes to either side need to be coordinated.

## Things to know

- Edits to `mkdocs.yml`'s `nav:` are required for new pages to appear in navigation.
- The footer copyright in `mkdocs.yml` explicitly disclaims affiliation with Meshtastic LLC — preserve that wording when editing the copyright string.
- `repo_url` is intentionally commented out in `mkdocs.yml`; `edit_uri` is still set, which is what powers the "edit this page" pencil. If you uncomment `repo_url`, the source link block in the header partial will activate.
