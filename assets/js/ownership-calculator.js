(() => {
  const form = document.getElementById('ownership-inputs');
  const money = new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'});
  const empty = document.getElementById('estimate-empty');
  const results = document.getElementById('estimate-values');
  function cents(name) {
    return Math.round((form.elements[name].valueAsNumber || 0) * 100);
  }
  form.addEventListener('input', () => {
    results.hidden = true;
    empty.hidden = false;
  });
  form.addEventListener('submit', event => {
    event.preventDefault();
    const years = form.elements.years.valueAsNumber;
    const gross = cents('purchase') + cents('once') + Math.round(cents('annual') * years);
    const resale = cents('resale');
    const net = gross - resale;
    document.getElementById('net-cost').textContent = money.format(net / 100);
    document.getElementById('gross-cost').textContent = money.format(gross / 100);
    document.getElementById('resale-result').textContent = money.format(resale / 100);
    document.getElementById('per-year').textContent = money.format(net / 100 / years);
    document.getElementById('estimate-gain').hidden = net >= 0;
    empty.hidden = true;
    results.hidden = false;
    const heading = document.getElementById('estimate-title');
    heading.focus({preventScroll: true});
    if (heading.getBoundingClientRect().bottom > window.innerHeight) {
      heading.scrollIntoView({block: 'start'});
    }
  });
  document.getElementById('calculator').hidden = false;
})();
