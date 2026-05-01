/* Cate Freight tiny site script — mobile nav + smooth focus only. */
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        nav.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // dynamic year insertion if any element has data-year
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // Prefill the quote form from URL params (used by the homepage microform)
  if (location.pathname.indexOf('/quote') === 0) {
    var p = new URLSearchParams(location.search);
    var map = {
      booking: 'line',
      container_size: 'container_size',
      terminal: 'terminal',
      delivery_zip: 'delivery_zip'
    };
    Object.keys(map).forEach(function (key) {
      var val = p.get(key);
      if (!val) return;
      var el = document.getElementsByName(map[key])[0];
      if (!el) return;
      if (el.tagName === 'SELECT') {
        // pick the option whose text or value contains val (case-insensitive)
        var v = val.toLowerCase();
        for (var i = 0; i < el.options.length; i++) {
          var t = (el.options[i].text || '').toLowerCase();
          var o = (el.options[i].value || '').toLowerCase();
          if (t === v || o === v || t.indexOf(v) > -1) { el.selectedIndex = i; break; }
        }
      } else {
        el.value = val;
      }
    });
  }
})();
