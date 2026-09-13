(() => {
  const box = document.querySelector('.blog-search');
  const input = document.querySelector('#blog-search');
  if (!box || !input) return;
  box.hidden = false;
  const entries = [...document.querySelectorAll('.blog-entry')];
  const searchable = entries.map(entry => entry.textContent.toLocaleLowerCase());
  const update = () => {
    const words = input.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let count = 0;
    entries.forEach((entry, i) => {
      entry.hidden = !words.every(word => searchable[i].includes(word));
      if (!entry.hidden) count++;
    });
    document.querySelectorAll('.blog-year').forEach(heading => {
      heading.hidden = !entries.some(entry => entry.dataset.year === heading.textContent.trim() && !entry.hidden);
    });
    document.querySelector('#blog-result-count').textContent = words.length ? `找到 ${count} 篇文章` : `共 ${entries.length} 篇文章`;
    document.querySelector('#blog-no-results').hidden = count !== 0;
  };
  input.addEventListener('input', update);
  update();
})();
