# Website inputs

All editable public content is in `profile.json`. The builder escapes the text and creates ordinary HTML; no frontend framework or database is required.

## Already filled from your resume

- Name, current role/company, Bengaluru location, and short biography.
- Email, LinkedIn, and the GitHub account from this repository's remote.
- Oracle, Zomato, and OYO experience, IIT Roorkee education, and technical skills.
- Public summaries of engineering work, Codex-assisted development, incident investigation, and reusable test harnesses.

Phone number, detailed operational metrics, private source links, and the full resume PDF are omitted from the first version. The original resume is not copied into this repository.

## Inputs you can add

| Input | Where to edit | Required? |
|---|---|---|
| Biography and preferred headline | `bio`, `tagline`, `title` | Already filled; review the wording. |
| Public contact/social links | `email`, `github`, `linkedin` | Already filled; review before publishing. |
| Profile photograph | `assets/chandan_tilicho_background.jpeg`; `photo.path`, `photo.alt`, `photo.width`, and `photo.height` | Tilicho photo selected by the owner and included. |
| Public project, writing, or demo links | Each `work` item's `url` | Optional. Only add links you can share publicly. |
| Downloadable resume | Put a public-safe PDF under `assets/`; set `resume.path` and `resume.label` | Optional. Remove any details you do not want public first. |
| Detailed project metrics | Relevant `work` summaries | Optional, after checking the details are appropriate for public sharing. |
| Domain | `site_url` and GitHub Pages custom-domain settings | Optional. The default github.io URL is free. |
| Publishing configuration | Repository visibility and Settings → Pages | Needed to make the website live. |

Keep the `privacy` fields in sync with your publication choices. They document the intended public scope; they are not a substitute for reviewing files. Everything under `assets/` is included in the public site build. Do not place private documents there.

Use `systems` or `developer-tools` for a work item's `category`. The filters use these values. New items do not need images or links. Leave optional paths and URLs empty rather than adding placeholder links.
