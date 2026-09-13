"""Check the real Jekyll output and the legacy articles it must preserve."""
import hashlib
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

SOURCE = Path(__file__).resolve().parents[1]
DESTINATION = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
REPORT = json.loads((SOURCE / "migration-report.json").read_text(encoding="utf-8"))
POSTS = json.loads((SOURCE / "_data/legacy_posts.json").read_text(encoding="utf-8"))

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])

errors = []
for route in ["index.html", "blog/index.html", "blog/legacy/index.html", "404.html", "sitemap.xml", "assets/css/main.css", "assets/js/main.min.js", "images/profile.jpg", *REPORT["article_paths"]]:
    if not (DESTINATION / route).is_file():
        errors.append(f"Missing output: {route}")

for name, expected in REPORT["assets"].items():
    # License remains in the repository; Jekyll intentionally excludes it.
    if name == "LICENSE":
        continue
    target = DESTINATION / name
    if not target.is_file():
        errors.append(f"Missing legacy asset: {name}")
    elif hashlib.sha256(target.read_bytes()).hexdigest() != expected:
        normalized = REPORT.get("text_asset_hashes", {}).get(name)
        if not normalized or hashlib.sha256(target.read_bytes().replace(b"\r\n", b"\n")).hexdigest() != normalized:
            errors.append(f"Changed legacy asset: {name}")

if (DESTINATION / "blog/index.html").is_file():
    parser = Links()
    parser.feed((DESTINATION / "blog/index.html").read_text(encoding="utf-8"))
    actual = {unquote(urlsplit(url).path) for url in parser.links}
    for post in POSTS:
        if post["url"] not in actual:
            errors.append(f"Blog omits an existing listed post: {post['title']}")

if (DESTINATION / "index.html").is_file():
    homepage = (DESTINATION / "index.html").read_text(encoding="utf-8")
    if "About me" not in homepage or 'id="research"' not in homepage:
        errors.append("Root URL is not the academic homepage")
    for placeholder in ["Your Name", "Red Brick University", "none@example.org", "PS_CX0AAAAAJ"]:
        if placeholder in homepage:
            errors.append(f"Unreplaced template profile: {placeholder}")
    if "{%" in homepage or "{{" in homepage:
        errors.append("Unrendered Liquid in homepage")

if errors:
    print("\n".join(errors))
    raise SystemExit(1)
print(f"Verified academic homepage, {len(POSTS)} indexed posts, {len(REPORT['article_paths'])} preserved article pages, and {len(REPORT['assets'])-1} original assets.")
