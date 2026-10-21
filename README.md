# Chandan Kashyap — personal website

A personal software-engineering portfolio with a short biography, selected engineering work, experience, education, skills, and contact links. The layout takes inspiration from the profile-led structure of [Yash Kant's website](https://yashkant.github.io/); the implementation and content here are original.

The site includes responsive layouts, a persistent light/dark theme, work filters, keyboard navigation, and a print stylesheet. All profile content remains visible when JavaScript is disabled. Fonts and assets are local; there is no database, tracking script, paid hosting dependency, or API key.

## Current state

The local site is ready to preview. The intended project-site URL is:

**https://chandan26197.github.io/personal_webpage/**

This URL is not a claim that deployment has completed. GitHub Pages must be enabled and the source pushed before the site is live. On initial inspection, the remote was reachable over SSH, but GitHub's unauthenticated repository API returned 404. Repository visibility and Pages availability need checking in the signed-in GitHub account.

## Preview locally

Requires Python 3.9 or newer. No pip or npm dependencies are needed to build or serve the site.

```sh
python3 scripts/check.py
python3 -m http.server 8080 --directory _site
```

Open **http://localhost:8080**. After editing inputs or styles, run `python3 scripts/check.py` again and reload the page.

## Inputs to review

See [the input checklist](inputs/README.md) and edit [inputs/profile.json](inputs/profile.json).

Your name, role, email, LinkedIn, work summaries, employment history, education, and skills are already filled. Your selected Tilicho profile photo is included. Optional additions are public project links, a public-safe resume PDF, and a custom domain. The first version omits the phone number, full resume PDF, and detailed operational metrics.

## Publish with free GitHub Pages

GitHub Pages supports public repositories on GitHub Free. Private-repository support depends on the account plan. Use a public repository if you want this setup on GitHub Free. See [GitHub Pages availability and URL types](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).

1. Review the public inputs and all files under `assets/`.
2. In `chandan26197/personal_webpage`, confirm the repository is public for GitHub Free hosting. Changing visibility is an owner decision; the setup has not changed it.
3. In **Settings → Pages → Build and deployment → Source**, select **GitHub Actions**. See [GitHub's configuration steps](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).
4. Commit and push the website sources to `main` when you are ready:

   ```sh
   git add README.md VERIFICATION.md .gitignore .github assets inputs scripts templates
   git commit -m "Add personal engineering portfolio"
   git push origin main
   ```

5. Watch **Actions → Check and publish portfolio**. The workflow builds and checks the site, uploads only `_site/`, and deploys it to the `github-pages` environment.
6. Once the deploy job succeeds, open the URL shown in that job. Check the homepage, mobile layout, profile links, filters, and theme toggle. The expected URL is `https://chandan26197.github.io/personal_webpage/`.

If the source has already been pushed after enabling Pages, use **Actions → Check and publish portfolio → Run workflow**. No personal access token is needed in this repository; deployment uses GitHub's built-in workflow token.

To use `https://chandan26197.github.io/` without the project suffix, use a repository named `chandan26197.github.io` and change `site_url`. A custom domain is optional and can cost money; it is not needed here.

## Source map

| Path | Purpose |
|---|---|
| `inputs/profile.json` | Editable public content and profile links. |
| `inputs/README.md` | All supplied and optional inputs. |
| `templates/index.html` | Semantic, server-rendered HTML template. |
| `assets/site.css` | Layout, themes, responsive behavior, and print styling. |
| `assets/site.js` | Progressive enhancement for themes and work filters. |
| `assets/theme-init.js` | Applies the saved theme before the page renders. |
| `assets/favicon.svg` | Original initials favicon. |
| `scripts/build.py` | Standard-library static site generator. |
| `scripts/check.py` | Build, link, asset, and public-output checks. |
| `scripts/browser-check.cjs` | Optional desktop/mobile and interaction checks using Playwright. |
| `.github/workflows/pages.yml` | PR checks and GitHub Pages deployment from `main`. |
| `_site/` | Generated public website; ignored by Git. |

## Updating the website

Change `inputs/profile.json`, then run `python3 scripts/check.py`. Preview and review the result. Commit and push to `main` to publish the next version. Template and stylesheet changes use the same workflow.

This repository stores only public-ready summaries and site source. Keep private resumes, employer documents, credentials, and internal source outside the repository. The existing MIT license is retained.

## Optional browser checks

The basic site needs only Python. To repeat the optional browser checks, install Node.js and the Playwright test dependency locally:

```sh
npm install --no-save --no-package-lock playwright
npx playwright install chromium --only-shell
python3 scripts/check.py
node scripts/browser-check.cjs
```

The check exercises filters, theme persistence, mobile overflow, no-JavaScript content, and keyboard navigation. Screenshots go to the operating system's temporary directory, not the published website. Review the dependency before installing it. These optional tools are not needed by visitors or the Pages build.
