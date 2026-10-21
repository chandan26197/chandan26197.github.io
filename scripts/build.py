#!/usr/bin/env python3
"""Build a portable static portfolio using only Python's standard library."""
import argparse
import html
import json
import shutil
from datetime import date
from pathlib import Path
from string import Template
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]

def text(value):
    return html.escape(str(value), quote=True)

def link(value):
    if urlparse(value).scheme not in {"https", "mailto"}:
        raise ValueError(f"Use an HTTPS or mailto link: {value}")
    return text(value)

def local_asset(value):
    candidate = (ROOT / value).resolve()
    if not candidate.is_relative_to(ROOT / "assets") or not candidate.is_file():
        raise ValueError("Public photos and resumes must be existing files under assets/")
    return text(value)

def build(output=ROOT / "_site"):
    profile = json.loads((ROOT / "inputs/profile.json").read_text())
    for key in ["name", "title", "company", "email", "github", "linkedin", "site_url", "bio", "work", "experience"]:
        if not profile.get(key):
            raise ValueError(f"Missing profile input: {key}")
    output = Path(output)
    if output.exists():
        if output.resolve() != (ROOT / "_site").resolve():
            raise ValueError("Only the generated _site directory may be replaced")
        shutil.rmtree(output)
    output.mkdir(parents=True)
    shutil.copytree(ROOT / "assets", output / "assets")
    values = {key: text(value) for key, value in profile.items() if isinstance(value, str)}
    values["github"] = link(profile["github"])
    values["linkedin"] = link(profile["linkedin"])
    values["site_url"] = link(profile["site_url"])
    values["source_url"] = "https://github.com/chandan26197/chandan26197.github.io"
    values["display_name"] = "<br>".join(text(part) for part in profile["name"].split(" ", 1))
    values["bio"] = "".join(f"<p>{text(p)}</p>" for p in profile["bio"])
    values["focus"] = "".join(f"<li>{text(p)}</li>" for p in profile["focus"])
    values["resume_link"] = ""
    if profile["resume"].get("path"):
        values["resume_link"] = f'<span aria-hidden="true">/</span><a href="{local_asset(profile["resume"]["path"])}">{text(profile["resume"]["label"])}</a>'
    values["portrait"] = ""
    if profile["photo"].get("path"):
        if not profile["photo"].get("alt"):
            raise ValueError("A profile photo needs descriptive alt text")
        photo_width = int(profile["photo"].get("width", 400))
        photo_height = int(profile["photo"].get("height", 400))
        if photo_width <= 0 or photo_height <= 0:
            raise ValueError("Photo dimensions must be positive")
        values["portrait"] = f'<img class="portrait" src="{local_asset(profile["photo"]["path"])}" alt="{text(profile["photo"]["alt"])}" width="{photo_width}" height="{photo_height}">'
    work = []
    for number, item in enumerate(profile["work"], 1):
        if item["category"] not in {"systems", "developer-tools"}:
            raise ValueError("Unknown work category")
        title = text(item["title"])
        if item.get("url"):
            title = f'<a href="{link(item["url"])}">{title}</a>'
        tags = "".join(f"<li>{text(tag)}</li>" for tag in item["tags"])
        work.append(f'<article class="work-item" data-work-category="{text(item["category"])}"><span class="work-number" aria-hidden="true">{number:02}</span><div><p class="work-label">{text(item["label"])}</p><h3>{title}</h3><p class="work-summary">{text(item["summary"])}</p><ul class="tags" aria-label="Technologies">{tags}</ul></div></article>')
    values["work"] = "".join(work)
    values["work_count"] = str(len(profile["work"]))
    values["experience"] = "".join(f'<article class="experience-item"><h3>{text(item["company"])}</h3><p class="period">{text(item["period"])}</p><p class="role">{text(item["role"])}</p><p class="detail">{text(item["detail"])}</p></article>' for item in profile["experience"])
    for key, value in profile["education"].items():
        values["education_period" if key == "period" else key] = text(value)
    values["skills"] = "".join(f'<dt>{text(group["group"])}</dt><dd>{text(" · ".join(group["items"]))}</dd>' for group in profile["skills"])
    values["year"] = str(date.today().year)
    content = Template((ROOT / "templates/index.html").read_text()).substitute(values)
    (output / "index.html").write_text(content)
    (output / ".nojekyll").touch()
    (output / "robots.txt").write_text(f'User-agent: *\nAllow: /\nSitemap: {profile["site_url"]}sitemap.xml\n')
    (output / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{text(profile["site_url"])}</loc></url></urlset>\n')
    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    print(f"Built {build()}")
