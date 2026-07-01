/**
 * Animal Hospital Anomaly Guides - Main JavaScript
 * Handles: Mobile hamburger menu, FAQ accordions, active nav state
 */

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Mobile Hamburger Menu ---------- */
  const toggle = document.querySelector('.navbar-toggle');
  const menu = document.querySelector('.navbar-menu');

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      toggle.classList.toggle('active');
      menu.classList.toggle('active');
    });

    // Close menu when a link is clicked
    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        toggle.classList.remove('active');
        menu.classList.remove('active');
      });
    });

    // Close menu when clicking outside
    document.addEventListener('click', function (e) {
      if (!toggle.contains(e.target) && !menu.contains(e.target)) {
        toggle.classList.remove('active');
        menu.classList.remove('active');
      }
    });
  }

  /* ---------- FAQ Accordion ---------- */
  document.querySelectorAll('.faq-question').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const item = btn.closest('.faq-item');
      const isActive = item.classList.contains('active');

      // Close all other FAQ items
      document.querySelectorAll('.faq-item.active').forEach(function (openItem) {
        if (openItem !== item) {
          openItem.classList.remove('active');
        }
      });

      // Toggle current item
      item.classList.toggle('active', !isActive);
    });
  });

  /* ---------- Set Active Nav Link ---------- */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.navbar-menu a').forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === currentPage) {
      link.classList.add('active');
    }
  });

  /* ---------- Back to Top Button ---------- */
  const backToTop = document.querySelector('.back-to-top');
  if (backToTop) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 300) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    });
    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ---------- Share - Copy Link ---------- */
  document.querySelectorAll('.share-btn-copy').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var url = btn.getAttribute('data-url') || window.location.href;
      navigator.clipboard.writeText(url).then(function () {
        btn.classList.add('share-btn-copied');
        btn.querySelector('.share-btn-text').textContent = 'Copied!';
        setTimeout(function () {
          btn.classList.remove('share-btn-copied');
          btn.querySelector('.share-btn-text').textContent = 'Copy Link';
        }, 2000);
      });
    });
  });

  /* ---------- Latest Guides: Fetch from all-articles.html ---------- */
  (function loadLatestGuides() {
    var container = document.getElementById('latest-guides-container');
    if (!container) return;

    // Show loading state
    container.innerHTML = '<p style="text-align:center;color:var(--color-muted);">Loading latest guides...</p>';

    fetch('all-articles.html')
      .then(function (res) {
        if (!res.ok) throw new Error('Failed to load');
        return res.text();
      })
      .then(function (html) {
        var parser = new DOMParser();
        var doc = parser.parseFromString(html, 'text/html');
        var items = doc.querySelectorAll('.article-list .article-item');
        var cards = '';

        // Take first 3 articles
        var limit = Math.min(6, items.length);
        for (var i = 0; i < limit; i++) {
          var item = items[i];
          var tag = item.querySelector('.article-item-tag');
          var link = item.querySelector('.article-item-content a');
          var h3 = item.querySelector('.article-item-content h3');
          var p = item.querySelector('.article-item-content p');
          var time = item.querySelector('time');

          var tagText = tag ? tag.textContent.trim() : '';
          var linkHref = link ? link.getAttribute('href') : '#';
          var title = h3 ? h3.textContent.trim() : '';
          var desc = p ? p.textContent.trim() : '';
          var datetime = time ? time.getAttribute('datetime') : '';
          var dateText = time ? time.textContent.trim() : '';

          cards += '<article class="card">' +
            '<span class="card-tag">' + tagText + '</span>' +
            '<h3><a href="' + linkHref + '">' + title + '</a></h3>' +
            '<p>' + desc + '</p>' +
            '<span class="card-meta"><time datetime="' + datetime + '">' + dateText + '</time></span>' +
            '</article>';
        }

        if (cards) {
          container.innerHTML = cards;
        } else {
          container.innerHTML = '<p style="text-align:center;color:var(--color-muted);">No guides found. Check back soon.</p>';
        }
      })
      .catch(function () {
        container.innerHTML = '<p style="text-align:center;color:var(--color-muted);">Unable to load latest guides. Please visit <a href="all-articles.html">All Articles</a>.</p>';
      });
  })();


});
