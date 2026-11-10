(function () {
  var body = document.querySelector(".post-body");
  if (!body) return;
  var headings = body.querySelectorAll("h2");
  if (headings.length < 3) return;
  var nav = document.createElement("nav");
  nav.className = "toc";
  nav.setAttribute("aria-label", "In this article");
  var kicker = document.createElement("p");
  kicker.className = "kicker";
  kicker.textContent = "In this article";
  var list = document.createElement("ol");
  for (var i = 0; i < headings.length; i++) {
    var hx = headings[i];
    if (!hx.id) hx.id = "section-" + (i + 1);
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.href = "#" + hx.id;
    a.textContent = hx.textContent;
    li.appendChild(a);
    list.appendChild(li);
  }
  nav.appendChild(kicker);
  nav.appendChild(list);
  body.parentNode.insertBefore(nav, body);
})();
