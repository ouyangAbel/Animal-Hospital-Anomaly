import json
import os

base_dir = r'C:\Users\tulia\animal-hospital-anomaly-guides'

nav_html = """  <nav class="navbar" role="navigation" aria-label="Main navigation">
    <div class="container">
      <a href="index.html" class="navbar-logo" aria-label="Home">
        <span class="navbar-logo-main">Animal Hospital Anomaly Guides</span>
        <span class="navbar-logo-sub">Full Walkthrough & Game Tips</span>
      </a>
      <button class="navbar-toggle" aria-label="Toggle navigation menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
      <div class="navbar-menu">
        <a href="index.html">Home</a>
        <a href="character-guides.html">Character Guides</a>
        <a href="mission-walkthroughs.html">Mission Walkthroughs</a>
        <a href="boss-guides.html">Boss Guides</a>
        <a href="equipment-guides.html">Equipment &amp; Build Guides</a>
        <a href="all-articles.html">All Articles</a>
      </div>
    </div>
  </nav>"""

footer_html = """  <footer class="site-footer">
    <div class="container">
      <p class="footer-copyright">&copy; 2026 Animal Hospital Anomaly Guides | All Rights Reserved</p>
      <div class="footer-links">
        <a href="privacy-policy.html">Privacy Policy</a>
        <a href="about-us.html">About Us</a>
        <a href="contact-us.html">Contact Us</a>
        <a href="sitemap.xml">Sitemap</a>
      </div>
    </div>
  </footer>

  <!-- Back to Top -->
  <button class="back-to-top" aria-label="Back to top">&#8593;</button>

  <script src="script.js"></script>
</body>
</html>"""

with open(os.path.join(base_dir, 'items.json'), 'r', encoding='utf-8') as f:
    items = json.load(f)

for item in items:
    title = item['title']
    slug = item['id']
    tag = item['tag']
    desc = item['desc'].replace('&quot;', '"').replace('&apos;', "'")
    filename = f'anomaly-{slug}.html'
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Animal Hospital Anomaly Guide</title>
  <meta name="description" content="{title} anomaly in Animal Hospital Anomaly: detection methods, warning signs, and counter-strategies.">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://yourdomain.com/{filename}">
  <link rel="stylesheet" href="style.css">
</head>
<body>
{nav_html}
  <main class="main-content">
    <div class="container">
      <div class="ad-placeholder ad-placeholder-top" aria-label="Advertisement"></div>
    </div>

    <header class="page-header">
      <div class="container">
        <div class="breadcrumb">
          <a href="index.html">Home</a><span>/</span><a href="character-guides.html">Character Guides</a><span>/</span><span class="current">{title}</span>
        </div>
        <h1>{title}</h1>
        <p class="subtitle">Detection methods, warning signs, and counter-strategies for {title} in Animal Hospital Anomaly.</p>
      </div>
    </header>

    <div class="container">
      <article class="guide-article">
        <header class="guide-article-header">
          <span class="guide-article-tag">{tag}</span>
          <div class="guide-article-meta">
            <span>Category: Character Guides</span>
          </div>
        </header>
        <div class="guide-article-body">
          <p>{desc}</p>

          <div class="inner-links">
            <h4>Back to Character Guides</h4>
            <ul>
              <li><a href="character-guides.html">All Anomalies &amp; Enemies</a></li>
              <li><a href="boss-guides.html">Events &amp; Emergencies</a></li>
              <li><a href="equipment-guides.html">Items &amp; Shop Upgrades</a></li>
              <li><a href="article-how-to-survive.html">How to Survive: 14 Reflex-Level Tips</a></li>
            </ul>
          </div>
        </div>
      </article>

      <div class="ad-placeholder ad-placeholder-bottom" aria-label="Advertisement"></div>
    </div>
  </main>
{footer_html}"""
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print(f'Created {len(items)} anomaly pages')
