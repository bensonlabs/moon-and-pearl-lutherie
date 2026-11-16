# Moon & Pearl Lutherie

A responsive static website for Justin Benson's Los Angeles lutherie workshop. Original brand artwork, actual instrument and workshop photography, instrument studies, and practical shop notes.

## Structure

- `index.html`: homepage, two selected projects, shop introduction, contact.
- `cream-electric.html`, `custom-inlays.html`, `maple-stock.html`: instrument and material studies.
- `gallery.html`: selected Instagram reels with an automatically loaded inline player and direct-link fallback.
- `notes.html`: summaries of workshop posts from the supplied Instagram recording.
- `styles.css`, `script.js`: shared styles and progressive enhancement.
- `assets/`: local logo, photographs, favicon, and licensed Public Sans body font and Jost heading font.
- `tools/build.py`: creates the static Sites package from root source.

No framework, installation, database, or runtime service is required. All page content and navigation work without JavaScript. JavaScript updates the footer year.

## Preview and validate

Serve the root with any static server, for example `python3 -m http.server 8000`.

Run `python3 tools/check.py` to check local pages, assets, fragments, navigation, canonicals, sitemap consistency, and indexing rules. Pass an optional directory, such as `python3 tools/check.py dist`, to check packaged output. Run `node --check script.js` for JavaScript syntax. Run `python3 tools/build.py` to validate source, prepare the ignored `dist/` directory for Sites, and validate the packaged output. A missing or incorrect canonical on a new indexable page fails the check and build.

## Hosting

GitHub Pages can continue serving the repository root from `main`. No workflow or build step is required for GitHub Pages. `.nojekyll` prevents Jekyll processing. Homepage links use `/` (and `/#section` for homepage anchors), targeting the custom-domain root. Other local links remain relative. For previews, serve the repository or `dist/` at the server root.

The private Sites version uses `dist/` and the project identity in `.openai/hosting.json`. Packaging does not publish the public GitHub Pages site.

## Content

See `ASSETS.md` for origins. Photographs are from the owner's existing public website. The logo was exported from the supplied Illustrator artwork, retaining the lettering as paths.

Contact links use `moonandpearl.lutherie@gmail.com` and `@moonandpearl.lutherie`, as published on the existing website. North Hollywood is the published shop location. Current owner-approved service prices are listed in the homepage Services & pricing section. Strings and parts are extra unless specified; estimates are confirmed after inspection. Floyd Rose and other double-locking tremolo systems are excluded.

Study descriptions avoid invented dates, serial numbers, availability, and performance specifications. Instagram summaries link to the account because individual post permalinks were not present in the recording.

## Updating

Edit root HTML and shared CSS/JavaScript. Replace photographs in `assets/` with suitable originals and update alt text. Run the checks and rebuild before saving another Sites version. Do not edit `dist/` separately.

## Project inquiries

`inquiry.html` accepts setup, repair, electronics, custom fretboard inlay, fretwork, and other neck inquiries. Complete guitar commissions are closed. Homepage availability and all navigation links point visitors toward this scope.

The form posts directly to FormSubmit, which delivers submissions to `moonandpearl.lutherie@gmail.com`. It works without JavaScript, keeps FormSubmit's default spam check, and uses a honeypot. Reference links are supported; there is no file upload. Successful submissions return to `inquiry-thanks.html`.

**Activation and delivery confirmed:** the owner activated FormSubmit and supplied a received test inquiry on September 6, 2026. Reply-to behavior has not been independently verified. A direct email fallback is visible on the form. Do not treat the thank-you page alone as evidence of email delivery.

The form uses an external email-delivery service; the static site itself needs no server or database. If the public domain changes, update the form's absolute `_next` redirect URL.

## Search discovery

`sitemap.xml` lists the seven public content and inquiry pages at the canonical HTTPS domain. The noindex inquiry thank-you page is excluded. Update the sitemap when adding or removing public pages. `robots.txt` allows crawling and advertises the sitemap. Both are included in the static build. No fabricated last-modified dates or priority values are used.

Search Console requires owner verification in Google. Add the Domain property `moonandpearllutherie.com`, add Google's exact TXT verification value in Squarespace DNS without replacing existing records, and verify. Submit `https://moonandpearllutherie.com/sitemap.xml` in the property's Sitemaps screen. Publishing these files alone does not register the property or guarantee indexing.

## Homepage simplification

The homepage now presents an introduction, two selected projects (inlays first), the workshop, and inquiries. Decorative shop-note cards, the slogan strip, material-stock card, and detail selector were removed. The existing notes and maple-stock URLs remain available for old links, but are no longer promoted in the main navigation or homepage.

The owner corrected the published Gmail spelling to `moonandpearl.lutherie@gmail.com`. All email links and the form endpoint use that spelling. FormSubmit may request activation again for the updated endpoint; delivery to that endpoint has not yet been rechecked.

## Canonical URLs and indexing validation

Every indexable HTML source page declares exactly one absolute canonical in its head. The homepage uses `https://moonandpearllutherie.com/`; each other content page retains its existing `.html` path on that domain. There is no page generator or shared HTML template: `tools/build.py` copies the source HTML unchanged. When adding an indexable page, add its own canonical and sitemap entry, then run the checks. The inquiry thank-you page retains its existing `noindex` and stays out of the sitemap.

The public custom domain is served by GitHub Pages, as indicated by the repository hosting instructions, CNAME, and live GitHub response headers. The separate Sites configuration packages a preview; it does not control the public domain. GitHub Pages provides no repository-level server redirect rules for `/index.html` to `/`. Files such as `_redirects`, `.htaccess`, or `vercel.json` would not implement that redirect here. Both URLs therefore continue serving the same HTML, with the canonical selecting `/`. No JavaScript or meta-refresh redirect is added. DNS and hosting are unchanged.

The pre-change live audit confirmed that `/` and `/index.html` both returned 200 with identical HTML and no canonical. HTTP and HTTPS www requests ended at the HTTPS apex. The sitemap already contained the seven preferred URLs and robots.txt allowed crawling. These are observed conditions, not proof of which URLs caused the Search Console notification. Affected examples must be inspected in the verified property.

### Deployment and Google follow-up

Changes must be reviewed and approved before merging to `main`, since the documented GitHub Pages setup can publish that branch automatically. This fix does not deploy or change DNS. After approved deployment:

1. Check page source on the public homepage, `/index.html`, and all sitemap pages for the expected canonical. Check that public content remains 200, robots.txt allows crawling, the thank-you page remains noindex, and the sitemap contains only preferred URLs. Confirm the existing HTTP/www redirects still work.
2. Open the `moonandpearllutherie.com` property in Search Console. Go to **Indexing > Pages > Duplicate without user-selected canonical**. Open **Examples** and inspect each listed URL. If no examples are shown, check the failed validation details/history for sample URLs. Do not infer the affected set from the email.
3. In **URL Inspection**, expand **Page indexing** and compare **User-declared canonical** with **Google-selected canonical**, including the last crawl date. The indexed report may still show pre-deployment data. Use **Test live URL** and **View tested page > HTML** to confirm the served canonical; the live test does not establish Google's selected canonical.
4. If examples identify another duplicate source, investigate it before retrying. Once all affected examples are addressed, use **Validate fix** on the issue report, or **Start new validation** from the failed validation details if offered. Request indexing for important preferred URLs and confirm `https://moonandpearllutherie.com/sitemap.xml` is submitted.
5. Monitor Google's validation and canonical selection. An intentional alternate URL can remain excluded as **Alternate page with proper canonical tag**. Neither a successful live test nor this code change guarantees indexing or resolves the report by itself.

References: [Google canonical guidance](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls), [Page indexing report](https://support.google.com/webmasters/answer/7440203), and [URL Inspection](https://support.google.com/webmasters/answer/9012289).
