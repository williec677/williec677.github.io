(function () {
  var input = document.getElementById("search-input") || document.querySelector(".site-search input[name='q']");
  var items = document.querySelectorAll("#search-results .search-item");
  var status = document.getElementById("search-status");
  if (!items.length) return;

  function currentQuery() {
    if (input && input.value) return input.value.trim();
    try {
      return new URLSearchParams(window.location.search).get("q") || "";
    } catch (e) {
      return "";
    }
  }

  function apply() {
    var q = currentQuery().toLowerCase();
    if (input && !input.value && q) input.value = q;
    var shown = 0;
    for (var i = 0; i < items.length; i++) {
      var hay = (items[i].getAttribute("data-search") || "").toLowerCase();
      var ok = !q || hay.indexOf(q) !== -1;
      items[i].hidden = !ok;
      if (ok) shown += 1;
    }
    if (status) {
      if (!q) status.textContent = "Browse every article, or type to filter.";
      else if (shown === 0) status.textContent = "No articles matched that search.";
      else status.textContent = shown + (shown === 1 ? " article found." : " articles found.");
    }
  }

  if (input) {
    input.addEventListener("input", apply);
  }
  apply();
})();
