import os
base = r'C:\Users\tulia\animal-hospital-anomaly-guides'
htmls = [f for f in os.listdir(base) if f.endswith('.html')]

for fname in sorted(htmls):
    path = os.path.join(base, fname)
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    if chr(10) in text.replace(chr(13), '') and '<meta pr' in text:
        idx = text.find('<meta pr')
        five = text[idx:idx+12]
        if five.endswith(chr(10)) or five.endswith(' '):
            print(f'BROKEN META: {fname} -> {repr(five)}')

print('Scan complete.')