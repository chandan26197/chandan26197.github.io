# Personal portfolio website

A static portfolio with responsive layouts, light and dark themes, project filters, keyboard navigation, and print styles. The site builds with Python's standard library and deploys through GitHub Actions.

## Local preview

Requires Python 3.9 or newer.

```sh
python3 scripts/check.py
python3 -m http.server 8080 --directory _site
```

Open `http://localhost:8080`. Rebuild after changing content, templates, or styles.

## Project structure

| Path | Purpose |
|---|---|
| `inputs/profile.json` | Website content and publication URL. |
| `templates/index.html` | HTML template. |
| `assets/` | Public styles, scripts, and images. |
| `scripts/build.py` | Static site generator. |
| `scripts/check.py` | Build, link, asset, and output checks. |
| `scripts/browser-check.cjs` | Optional browser and interaction checks. |
| `.github/workflows/pages.yml` | Build and GitHub Pages deployment workflow. |
| `_site/` | Generated website, excluded from Git. |

## GitHub Pages deployment

1. Open the repository's **Settings → Pages**.
2. Under **Build and deployment → Source**, select **GitHub Actions**.
3. Commit and push website changes to `main`.
4. Check **Actions → Check and publish portfolio** for the deployment result and published URL.

The workflow uploads only the generated `_site/` directory. Deployment uses GitHub's built-in workflow token.

GitHub Pages uses different default addresses for account and project websites:

| Repository name | Website address |
|---|---|
| `<username>.github.io` | `https://<username>.github.io/` |
| Any other repository name | `https://<username>.github.io/<repository>/` |

Set `site_url` in `inputs/profile.json` to the intended address. After renaming a repository, update the local Git remote as well. See [GitHub Pages site types](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) and [publishing configuration](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Updating the site

Edit the content, template, or assets, then run:

```sh
python3 scripts/check.py
```

Review the local preview before committing and pushing changes. Files under `assets/` are included in the published website.

## Optional browser checks

Requires Node.js and Playwright:

```sh
npm install --no-save --no-package-lock playwright
npx playwright install chromium --only-shell
python3 scripts/check.py
node scripts/browser-check.cjs
```

These checks cover project filters, theme persistence, mobile overflow, content without JavaScript, and keyboard navigation. Screenshots are written to the operating system's temporary directory. Browser-test dependencies are not required to build or publish the website.

## License

See [LICENSE](LICENSE).
