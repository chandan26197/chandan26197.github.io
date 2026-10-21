#!/usr/bin/env python3
"""Build the site and check real links, assets, and public output."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
from build import build

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.references = []
        self.headings = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            if attrs["id"] in self.ids:
                raise ValueError("Duplicate element ID")
            self.ids.add(attrs["id"])
        if tag == "h1":
            self.headings += 1
        for attribute in ["href", "src"]:
            if attrs.get(attribute):
                self.references.append(attrs[attribute])

output = build()
content = (output / "index.html").read_text()
page = Page()
page.feed(content)
assert page.headings == 1, "Expected one accessible page title"
for reference in page.references:
    parsed = urlparse(reference)
    if reference.startswith("#"):
        assert reference[1:] in page.ids, f"Broken section link: {reference}"
    elif parsed.scheme:
        assert parsed.scheme in {"https", "mailto"}, f"Unsafe external link: {reference}"
    else:
        assert not reference.startswith("/"), "Asset path will break under a project subpath"
        assert (output / unquote(parsed.path)).is_file(), f"Missing asset: {reference}"
assert "oraclecorp.com" not in content, "Internal company link in public page"
assert "oracleiaas.com" not in content, "Internal company link in public page"
for file in output.rglob("*"):
    assert not file.is_symlink(), f"Unexpected public symlink: {file}"
assert not (output / "inputs").exists(), "Raw inputs should not be published as site files"
assert not (output / ".git").exists(), "Git metadata should not be published"
print(f"Passed: build, {len(page.references)} links/assets, heading IDs, project-subpath paths, and public-output checks.")
