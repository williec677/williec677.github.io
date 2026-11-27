(() => {
  const vault = document.getElementById('vault');
  const prefix = 'mrtictoctalk:' + vault.dataset.store + ':v1:';
  const form = document.getElementById('watch-entry');
  const list = document.getElementById('watch-list');
  const status = document.getElementById('vault-status');
  const template = document.getElementById('watch-template');
  const cancel = document.getElementById('cancel-edit');
  const money = new Intl.NumberFormat('en-US', {style: 'currency', currency: 'USD'});
  let editing = null;

  const amount = cents => money.format(cents / 100);
  const validCost = value => Number.isSafeInteger(value) && value >= 0 && value <= 999999999900;
  function resetForm() {
    editing = null;
    form.reset();
    form.elements.watchName.setCustomValidity('');
    document.getElementById('entry-title').textContent = 'Add a watch';
    cancel.hidden = true;
  }

  function edit(record) {
    editing = record;
    const {name, purchase, expenses, valuation} = record.watch;
    form.elements.watchName.setCustomValidity('');
    form.elements.watchName.value = name;
    form.elements.purchase.value = (purchase / 100).toFixed(2);
    form.elements.expenses.value = (expenses / 100).toFixed(2);
    form.elements.valuation.value = valuation === null ? '' : (valuation / 100).toFixed(2);
    document.getElementById('entry-title').textContent = 'Edit watch';
    cancel.hidden = false;
    form.elements.watchName.focus();
  }

  function remove(record) {
    if (!window.confirm('Remove ' + record.watch.name + ' from this browser’s register?')) return;
    try {
      if (localStorage.getItem(record.key) !== record.raw) {
        status.textContent = 'This entry changed in another tab. Review the latest entry before removing it.';
      } else {
        localStorage.removeItem(record.key);
        status.textContent = 'Watch removed.';
      }
      if (editing && editing.key === record.key) resetForm();
      render();
      document.getElementById('register-title').focus();
    } catch {
      status.textContent = 'This browser could not remove the entry.';
    }
  }

  function render() {
    const records = [];
    let unreadable = false;
    try {
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (!key || !key.startsWith(prefix)) continue;
        const raw = localStorage.getItem(key);
        let watch;
        try { watch = JSON.parse(raw); } catch { unreadable = true; continue; }
        if (!watch || typeof watch.name !== 'string' || !validCost(watch.purchase) ||
            !validCost(watch.expenses) || !(watch.valuation === null || validCost(watch.valuation))) {
          unreadable = true;
          continue;
        }
        records.push({key, raw, watch});
      }
    } catch {
      status.textContent = 'Browser storage is unavailable. Allow site storage to use the Vault.';
      form.hidden = true;
      document.getElementById('register-empty').hidden = true;
      return;
    }
    records.sort((a, b) => a.watch.name.localeCompare(b.watch.name) || a.key.localeCompare(b.key));
    list.replaceChildren();
    let cost = 0, value = 0, valued = 0;
    for (const record of records) {
      const watch = record.watch;
      const entry = template.content.firstElementChild.cloneNode(true);
      entry.querySelector('h3').textContent = watch.name;
      const cells = entry.querySelectorAll('dd');
      cells[0].textContent = amount(watch.purchase);
      cells[1].textContent = amount(watch.expenses);
      cells[2].textContent = watch.valuation === null ? 'Not entered' : amount(watch.valuation);
      entry.querySelector('[data-edit]').addEventListener('click', () => edit(record));
      entry.querySelector('[data-remove]').addEventListener('click', () => remove(record));
      list.append(entry);
      cost += watch.purchase + watch.expenses;
      if (watch.valuation !== null) { value += watch.valuation; valued++; }
    }
    form.hidden = false;
    document.getElementById('register-empty').hidden = records.length > 0 || unreadable;
    document.getElementById('watch-count').textContent = records.length;
    document.getElementById('collection-cost').textContent = amount(cost);
    document.getElementById('collection-value').textContent = valued ? amount(value) : '—';
    document.getElementById('valuation-count').textContent =
      records.length ? valued + ' of ' + records.length + ' valued' : '';
    if (unreadable) status.textContent = 'Some saved entries could not be read. Totals include readable entries only.';
  }

  form.elements.watchName.addEventListener('input', () => form.elements.watchName.setCustomValidity(''));
  form.addEventListener('submit', event => {
    event.preventDefault();
    const fields = form.elements;
    const name = fields.watchName.value.trim();
    if (!name) {
      fields.watchName.setCustomValidity('Enter a watch name or reference.');
      fields.watchName.reportValidity();
      return;
    }
    const cents = field => Math.round((field.valueAsNumber || 0) * 100);
    const watch = {name, purchase: cents(fields.purchase), expenses: cents(fields.expenses),
      valuation: fields.valuation.value === '' ? null : cents(fields.valuation)};
    try {
      if (editing && localStorage.getItem(editing.key) !== editing.raw) {
        status.textContent = 'This entry changed in another tab. Cancel this edit and reopen the latest entry.';
        render();
        return;
      }
      const key = editing ? editing.key : prefix + crypto.randomUUID();
      localStorage.setItem(key, JSON.stringify(watch));
      status.textContent = name + ' saved in this browser.';
    } catch {
      status.textContent = 'The watch could not be saved. Check browser storage and available space.';
      return;
    }
    resetForm();
    render();
  });
  cancel.addEventListener('click', () => {
    resetForm();
    form.elements.watchName.focus();
  });
  window.addEventListener('storage', event => {
    if (!event.key || event.key.startsWith(prefix)) render();
  });
  vault.hidden = false;
  render();
})();
