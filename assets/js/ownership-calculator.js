(function () {
  var root = document.getElementById("ownership-calculator");
  if (!root) return;

  // Figures from the MrTicTocTalk True Cost Breakdown video: official US prices checked Nov 18, 2026;
  // WatchCharts estimated private sale and 1 year sales volume as of Nov 17, 2026.
  var examples = [
    { id: "s1-field-auto", sc: "1", scenario: "1, buy at official retail", name: "Seiko 5 Sports Field automatic SRPG29", purchase: 315, service: 176, resale: 202, sales: 125, note: "Official retail $315, official 4R service $176. Lowest illustrative ownership cost in scenario 1." },
    { id: "s1-prx-chrono", sc: "1", scenario: "1, buy at official retail", name: "Tissot PRX quartz chronograph T1374171105100", purchase: 525, service: 200, resale: 428, sales: 6, note: "This estimated resale rests on only 6 reported sales in one year, and WatchCharts market data for this reference only starts in September 2026. Treat the result as thin data." },
    { id: "s1-field-gmt", sc: "1", scenario: "1, buy at official retail", name: "Seiko 5 Sports Field GMT SSK023", purchase: 450, service: 176, resale: 326, sales: 484, note: "Official retail $450, official 4R service $176. Much more reported market activity than the chronograph." },
    { id: "s1-prx-quartz", sc: "1", scenario: "1, buy at official retail", name: "Tissot PRX 40 mm quartz T1374101103100", purchase: 450, service: 130, resale: 209, sales: 421, note: "In scenario 1, this cheaper retail watch can cost more to own than the chronograph." },
    { id: "s1-hamilton", sc: "1", scenario: "1, buy at official retail", name: "Hamilton Intra Matic Auto Chrono H38416111", purchase: 2645, service: 370, resale: 1474, sales: 71, note: "Official retail $2,645. Official complete automatic chronograph service $370." },
    { id: "s2-prx-quartz", sc: "2", scenario: "2, buy at today's estimated private sale", name: "Tissot PRX 40 mm quartz T1374101103100", purchase: 209, service: 130, resale: 209, sales: 421, note: "In this simplified case the illustrative cost equals the complete service bill." },
    { id: "s2-field-auto", sc: "2", scenario: "2, buy at today's estimated private sale", name: "Seiko 5 Sports Field automatic SRPG29", purchase: 202, service: 176, resale: 202, sales: 125, note: "Tied with the Field GMT: the illustrative cost equals the official 4R service." },
    { id: "s2-field-gmt", sc: "2", scenario: "2, buy at today's estimated private sale", name: "Seiko 5 Sports Field GMT SSK023", purchase: 326, service: 176, resale: 326, sales: 484, note: "Tied with the Field automatic: the illustrative cost equals the official 4R service." },
    { id: "s2-prx-chrono", sc: "2", scenario: "2, buy at today's estimated private sale", name: "Tissot PRX quartz chronograph T1374171105100", purchase: 428, service: 200, resale: 428, sales: 6, note: "Still sits on a 6 sale estimate. Not a forecast of a later sale." },
    { id: "s2-hamilton", sc: "2", scenario: "2, buy at today's estimated private sale", name: "Hamilton Intra Matic Auto Chrono H38416111", purchase: 1474, service: 370, resale: 1474, sales: 71, note: "Illustrative cost equals the official complete automatic chronograph service." }
  ];
  var SHORT = {
    "Tissot PRX quartz chronograph T1374171105100": "PRX chronograph",
    "Tissot PRX 40 mm quartz T1374101103100": "PRX 40 mm quartz",
    "Seiko 5 Sports Field automatic SRPG29": "Field automatic",
    "Seiko 5 Sports Field GMT SSK023": "Field GMT",
    "Hamilton Intra Matic Auto Chrono H38416111": "Hamilton"
  };

  var purchaseEl = document.getElementById("calc-purchase");
  var serviceEl = document.getElementById("calc-service");
  var resaleEl = document.getElementById("calc-resale");
  var feePctEl = document.getElementById("calc-fee-pct");
  var feeFlatEl = document.getElementById("calc-fee-flat");
  var resultEl = document.getElementById("calc-result");
  var sensEl = document.getElementById("calc-sens");
  var exampleBox = document.getElementById("calc-examples");

  function money(n) {
    var abs = Math.abs(n);
    var s = "$" + abs.toLocaleString("en-US", { minimumFractionDigits: (Math.round(abs * 100) % 100 === 0) ? 0 : 2, maximumFractionDigits: 2 });
    return n < 0 ? "minus " + s : s;
  }
  function num(el, optional) {
    var raw = String(el.value).replace(/[$,\s]/g, "");
    if (raw === "" && optional) return 0;
    var v = parseFloat(raw);
    return isFinite(v) && v >= 0 ? v : null;
  }
  function netSale(gross, pct, flat) { return gross * (1 - pct / 100) - flat; }
  function costText(c) { return c < 0 ? "a gain of " + money(-c) : money(c); }

  function compute() {
    var p = num(purchaseEl), s = num(serviceEl), r = num(resaleEl), pct = num(feePctEl, true), flat = num(feeFlatEl, true);
    if (p === null || s === null || r === null || pct === null || flat === null || pct > 100) {
      resultEl.innerHTML = "Enter a purchase price, a service cost, and an expected resale value in US dollars. Selling fees are optional (0 to 100 percent, plus any flat fee).";
      sensEl.innerHTML = "";
      return;
    }
    var net = netSale(r, pct, flat);
    var cost = p + s - net;
    var feeLine = (pct > 0 || flat > 0)
      ? " Selling fees: " + pct + " percent" + (flat > 0 ? " plus " + money(flat) : "") + ", so net resale is " + money(net) + "."
      : "";
    resultEl.innerHTML = (cost < 0 ? "Illustrative net ownership result: " : "Illustrative net ownership cost: ") + costText(cost) + "." +
      '<span class="calc-formula">' + money(p) + " purchase plus " + money(s) + " service minus " + money(net) + " net resale equals " + costText(cost) + "." + feeLine +
      " Illustrative, not a prediction.</span>";
    var rows = [0, 10, 20].map(function (d) {
      var gross = p * (1 - d / 100);
      var c = p + s - netSale(gross, pct, flat);
      return "<tr><td>Sell " + d + " percent below purchase</td><td>" + money(gross) + "</td><td>" + costText(c) + "</td></tr>";
    }).join("");
    sensEl.innerHTML = "<table><thead><tr><th>Hypothetical resale</th><th>Sale price</th><th>Net ownership cost</th></tr></thead><tbody>" + rows + "</tbody></table>" +
      '<p class="calc-note">Hypothetical examples, not predictions of future market prices. Your selling fees, if entered, are applied to each sale price.</p>';
  }

  function loadExample(ex, btn) {
    purchaseEl.value = ex.purchase;
    serviceEl.value = ex.service;
    resaleEl.value = ex.resale;
    feePctEl.value = 0;
    feeFlatEl.value = 0;
    var buttons = exampleBox.querySelectorAll("button");
    for (var i = 0; i < buttons.length; i++) buttons[i].setAttribute("aria-pressed", "false");
    if (btn) btn.setAttribute("aria-pressed", "true");
    var note = document.getElementById("calc-example-note");
    if (note) note.textContent = ex.name + ", scenario " + ex.scenario + ". " + ex.note + " WatchCharts reported sales, past year: " + ex.sales + ".";
    compute();
  }

  examples.forEach(function (ex) {
    var btn = document.createElement("button");
    btn.type = "button";
    btn.setAttribute("aria-pressed", "false");
    btn.textContent = (SHORT[ex.name] || ex.name) + ", scenario " + ex.sc;
    btn.addEventListener("click", function () { loadExample(ex, btn); });
    exampleBox.appendChild(btn);
  });

  [purchaseEl, serviceEl, resaleEl, feePctEl, feeFlatEl].forEach(function (el) {
    el.addEventListener("input", compute);
    el.addEventListener("change", compute);
  });

  loadExample(examples[0], exampleBox.querySelector("button"));
})();
