try {
  const saved = localStorage.getItem('portfolio-theme');
  const theme = saved === 'light' || saved === 'dark' ? saved : (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  document.documentElement.dataset.theme = theme;
} catch { /* CSS keeps the site readable when storage is unavailable. */ }
