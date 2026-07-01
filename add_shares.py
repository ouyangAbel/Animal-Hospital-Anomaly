import os, re

base_dir = r'C:\Users\tulia\animal-hospital-anomaly-guides'

# Read the share bar template from boss-fight-guide
with open(os.path.join(base_dir, 'article-boss-fight-guide.html'), 'r', encoding='utf-8') as f:
    boss_content = f.read()

# Extract share bar
pattern = r'(<!-- Share Bar -->.*?</div>)'
match = re.search(pattern, boss_content, re.DOTALL)
share_bar = match.group(1) if match else None

print(f'Share bar found: {bool(share_bar)}')

# Get all anomaly pages
anomaly_pages = [f for f in os.listdir(base_dir) if f.startswith('anomaly-') and f.endswith('.html')]
print(f'Found {len(anomaly_pages)} anomaly pages')

# Get all article pages
article_pages = ['article-boss-fight-guide.html', 'article-how-to-survive.html', 'article-sanity-management.html', 'article-sanity-recovery-tips.html', 'article-treatment-workflow.html']

for page in article_pages + anomaly_pages:
    if page == 'article-boss-fight-guide.html':
        continue  # Skip the template page
        
    filepath = os.path.join(base_dir, page)
    if not os.path.exists(filepath):
        print(f'Skipping {page} (not found)')
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if share bar already exists
    if 'share-bar' in content:
        print(f'{page}: share bar already exists')
        continue
    
    # Find the closing </article> tag and insert share bar before it
    # Look for the pattern: </div>\n      </article>
    pattern = r'(</div>\s*</article>)'
    replacement = share_bar + r'\1'
    new_content = re.sub(pattern, replacement, content, count=1)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'{page}: share bar added')
    else:
        print(f'{page}: failed to add share bar')

print('Done!')
