import os, re
base = r"C:\Users\tulia\animal-hospital-anomaly-guides"

# Fix boss-guides.html head
path = os.path.join(base, "boss-guides.html")
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Fix broken og:title (missing "A")
text = text.replace(
    '<meta property="og:title" content="nimal Hospital Anomaly Events',
    '<meta property="og:title" content="Animal Hospital Anomaly Events'
)

# Fix second corrupted og:title -> should be og:description
old = 'favicon.webp">>\n  <meta property="og:title" content="andle every timed emergency'
new = 'favicon.webp">\n  <meta property="og:description" content="Handle every timed emergency'
text = text.replace(old, new)

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("Fixed boss-guides.html OG tags")

# Fix article-boss-fight-guide.html - check and fix if needed
path2 = os.path.join(base, "article-boss-fight-guide.html")
with open(path2, "r", encoding="utf-8") as f:
    text2 = f.read()

# Fix the broken og:title with literal backtick escape pattern
if "og:title\" c" in text2:
    bad_start = text2.find("og:title\" c")
    bad_end = text2.find("ontent=\"", bad_start) + 9
    actual_content_start = text2.find('"', bad_end) + 1
    actual_content_end = text2.find('"', actual_content_start)
    actual_content = text2[actual_content_start:actual_content_end]
    # Rebuild clean og:title
    clean_og = f'  <meta property="og:title" content="{actual_content}">\n  <link rel="icon" type="image/webp" href="/images/favicon.webp">'
    # Remove corrupted block and insert clean
    block_end = text2.find("/>", actual_content_end)
    block_end = text2.find(">", block_end) + 1
    text2 = text2[:bad_start-1] + clean_og + text2[block_end:]
    with open(path2, "w", encoding="utf-8") as f:
        f.write(text2)
    print("Fixed article-boss-fight-guide.html OG tags")
else:
    print("article-boss-fight-guide.html OG tags look OK")
