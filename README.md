# Moon & Pearl Lutherie

A responsive static website for Justin Benson's Los Angeles lutherie workshop. Original brand artwork, actual instrument and workshop photography, instrument studies, and practical shop notes.

## Structure

- `index.html`: homepage, workshop detail selector, shop introduction, contact.
- `cream-electric.html`, `custom-inlays.html`, `maple-stock.html`: instrument and material studies.
- `gallery.html`: selected Instagram reels with a click-to-load player and direct-link fallback.
- `notes.html`: summaries of workshop posts from the supplied Instagram recording.
- `styles.css`, `script.js`: shared styles and progressive enhancement.
- `assets/`: local logo, photographs, favicon, and licensed Public Sans font.
- `tools/build.py`: creates the static Sites package from root source.

No framework, installation, database, or runtime service is required. All page content and navigation work without JavaScript. JavaScript enables the three-way detail selector and updates the footer year. Without JavaScript the shaping detail remains visible.

## Preview and validate

Serve the root with any static server, for example `python3 -m http.server 8000`.

Run `python3 tools/check.py` to check local pages, assets, fragments, and navigation. Run `node --check script.js` for JavaScript syntax. Run `python3 tools/build.py` to prepare the ignored `dist/` directory for Sites.

## Hosting

GitHub Pages can continue serving the repository root from `main`. No workflow or build step is required for GitHub Pages. `.nojekyll` prevents Jekyll processing. Relative links support repository-path hosting.

The private Sites version uses `dist/` and the project identity in `.openai/hosting.json`. Packaging does not publish the public GitHub Pages site.

## Content

See `ASSETS.md` for origins. Photographs are from the owner's existing public website. The logo was exported from the supplied Illustrator artwork, retaining the lettering as paths.

Contact links use `moonandpearllutherie@gmail.com` and `@moonandpearl.lutherie`, as published on the existing website. North Hollywood is the published shop location. Historical service pricing has not been republished as current pricing.

Study descriptions avoid invented dates, serial numbers, availability, and performance specifications. Instagram summaries link to the account because individual post permalinks were not present in the recording.

## Updating

Edit root HTML and shared CSS/JavaScript. Replace photographs in `assets/` with suitable originals and update alt text. Run the checks and rebuild before saving another Sites version. Do not edit `dist/` separately.
