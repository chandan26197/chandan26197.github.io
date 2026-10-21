const themeButton = document.querySelector('[data-theme-toggle]');
function describeTheme() {
  const dark = document.documentElement.dataset.theme === 'dark';
  themeButton.textContent = dark ? 'Light mode' : 'Dark mode';
  themeButton.setAttribute('aria-label', dark ? 'Switch to light color theme' : 'Switch to dark color theme');
  themeButton.setAttribute('aria-pressed', String(dark));
}
if (themeButton) {
  themeButton.hidden = false;
  describeTheme();
  themeButton.addEventListener('click', () => {
    document.documentElement.dataset.theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('portfolio-theme', document.documentElement.dataset.theme); } catch {}
    describeTheme();
  });
}
const filters = document.querySelector('[data-work-filters]');
if (filters) {
  filters.hidden = false;
  filters.addEventListener('click', event => {
    const button = event.target.closest('button[data-filter]');
    if (!button) return;
    filters.querySelectorAll('button').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    let visible = 0;
    document.querySelectorAll('[data-work-category]').forEach(item => {
      item.hidden = button.dataset.filter !== 'all' && item.dataset.workCategory !== button.dataset.filter;
      if (!item.hidden) visible++;
    });
    document.querySelector('[data-work-status]').textContent = `${visible} projects shown`;
  });
}
