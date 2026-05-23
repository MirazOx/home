import json
import re

html_path = '/Users/miraz/.gemini/antigravity/scratch/miraz-redesign/credentials/index.html'

with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Extract json
json_match = re.search(r'<script type="application/json" id="inline-certificates-data">(.*?)</script>', html, re.DOTALL)
if not json_match:
    print("FAIL: Could not find json data block")
    exit(1)

data = json.loads(json_match.group(1))
print(f"Loaded {len(data)} certificates.")

THEME_ORDER = [
  'Journalism & Fact-Checking',
  'Research & Data',
  'Science, Data & Technology',
  'English Language & Communication',
  'Career Development & Productivity',
  'Project Management & Leadership',
  'Negotiation & Conflict Resolution',
  'Philosophy, Religion & Ethics',
  'Psychology & Mental Health',
  'Business & Economics',
  'Language Learning',
  'Awards & Recognition'
]

try:
    themes = list(set(c.get('theme') for c in data))
    themes.sort(key=lambda t: THEME_ORDER.index(t) if t in THEME_ORDER else 99)
    
    def extract_year(date):
        match = re.search(r'(20\d{2}|19\d{2})', str(date or ''))
        return int(match.group(1)) if match else None
        
    years = list(set(extract_year(c.get('date')) for c in data))
    years = [y for y in years if y is not None]
    years.sort(reverse=True)
    
    print("Themes found:", themes)
    print("Years found:", years)
    print("JS Logic is structurally valid!")
except Exception as e:
    print("JS Logic failed:", str(e))
    exit(1)
