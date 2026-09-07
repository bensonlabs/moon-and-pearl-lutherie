# Moon & Pearl Lutherie

A responsive static website for Justin Benson's Los Angeles lutherie workshop. Original brand artwork, actual instrument and workshop photography, instrument studies, and practical shop notes.

## Structure

- `index.html`: homepage, two selected projects, shop introduction, contact.
- `cream-electric.html`, `custom-inlays.html`, `maple-stock.html`: instrument and material studies.
- `gallery.html`: selected Instagram reels with an automatically loaded inline player and direct-link fallback.
- `notes.html`: summaries of workshop posts from the supplied Instagram recording.
- `styles.css`, `script.js`: shared styles and progressive enhancement.
- `assets/`: local logo, photographs, favicon, and licensed Public Sans font.
- `tools/build.py`: creates the static Sites package from root source.

No framework, installation, database, or runtime service is required. All page content and navigation work without JavaScript. JavaScript updates the footer year.

## Preview and validate

Serve the root with any static server, for example `python3 -m http.server 8000`.

Run `python3 tools/check.py` to check local pages, assets, fragments, and navigation. Run `node --check script.js` for JavaScript syntax. Run `python3 tools/build.py` to prepare the ignored `dist/` directory for Sites.

## Hosting

GitHub Pages can continue serving the repository root from `main`. No workflow or build step is required for GitHub Pages. `.nojekyll` prevents Jekyll processing. Relative links support repository-path hosting.

The private Sites version uses `dist/` and the project identity in `.openai/hosting.json`. Packaging does not publish the public GitHub Pages site.

## Content

See `ASSETS.md` for origins. Photographs are from the owner's existing public website. The logo was exported from the supplied Illustrator artwork, retaining the lettering as paths.

Contact links use `moonandpearl.lutherie@gmail.com` and `@moonandpearl.lutherie`, as published on the existing website. North Hollywood is the published shop location. Historical service pricing has not been republished as current pricing.

Study descriptions avoid invented dates, serial numbers, availability, and performance specifications. Instagram summaries link to the account because individual post permalinks were not present in the recording.

## Updating

Edit root HTML and shared CSS/JavaScript. Replace photographs in `assets/` with suitable originals and update alt text. Run the checks and rebuild before saving another Sites version. Do not edit `dist/` separately.

## Project inquiries

`inquiry.html` accepts custom fretboard inlay, fretwork, and other neck inquiries. Complete guitar commissions are closed. Homepage availability and all navigation links point visitors toward this scope.

The form posts directly to FormSubmit, which delivers submissions to `moonandpearl.lutherie@gmail.com`. It works without JavaScript, keeps FormSubmit's default spam check, and uses a honeypot. Reference links are supported; there is no file upload. Successful submissions return to `inquiry-thanks.html`.

**Activation and delivery confirmed:** the owner activated FormSubmit and supplied a received test inquiry on September 6, 2026. Reply-to behavior has not been independently verified. A direct email fallback is visible on the form. Do not treat the thank-you page alone as evidence of email delivery.

The form uses an external email-delivery service; the static site itself needs no server or database. If the public domain changes, update the form's absolute `_next` redirect URL.

## Search discovery

`sitemap.xml` lists the seven public content and inquiry pages at the canonical HTTPS domain. The noindex inquiry thank-you page is excluded. Update the sitemap when adding or removing public pages. `robots.txt` allows crawling and advertises the sitemap. Both are included in the static build. No fabricated last-modified dates or priority values are used.

Search Console requires owner verification in Google. Add the Domain property `moonandpearllutherie.com`, add Google's exact TXT verification value in Squarespace DNS without replacing existing records, and verify. Submit `https://moonandpearllutherie.com/sitemap.xml` in the property's Sitemaps screen. Publishing these files alone does not register the property or guarantee indexing.

## Homepage simplification

The homepage now presents an introduction, two selected projects (inlays first), the workshop, and inquiries. Decorative shop-note cards, the slogan strip, material-stock card, and detail selector were removed. The existing notes and maple-stock URLs remain available for old links, but are no longer promoted in the main navigation or homepage.

The owner corrected the published Gmail spelling to `moonandpearl.lutherie@gmail.com`. All email links and the form endpoint use that spelling. FormSubmit may request activation again for the updated endpoint; delivery to that endpoint has not yet been rechecked.
