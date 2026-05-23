import json
import os

root_dir = "/Users/miraz/.gemini/antigravity/scratch/miraz-redesign"
json_path = os.path.join(root_dir, "content/articles.json")
html_path = os.path.join(root_dir, "archive/index.html")

print("Reading articles.json...")
with open(json_path, "r", encoding="utf-8") as f:
    articles_data = json.load(f)

json_content = json.dumps(articles_data, ensure_ascii=False)

print("Reading archive/index.html...")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Inline the JSON block before '<script>'
inline_block = f'<script type="application/json" id="inline-articles-data">{json_content}</script>\n<script>'
html = html.replace("<script>", inline_block, 1)

# 2. Replace the fetch catch fallback logic
old_fetch_block = """fetch('/content/articles.json?v=15')
  .then(response => {
    if (!response.ok) throw new Error('Could not load archive');
    return response.json();
  })
  .then(data => {
    ALL_ARTICLES = data;
    hydrateFilters(data);
    renderArchive();
  })
  .catch(() => {
    document.getElementById('count').textContent = 'Archive loads when the site is served over HTTP.';
  });"""

new_fetch_block = """fetch('/content/articles.json?v=15')
  .then(response => {
    if (!response.ok) throw new Error('Could not load archive');
    return response.json();
  })
  .then(data => {
    ALL_ARTICLES = data;
    hydrateFilters(data);
    renderArchive();
  })
  .catch(() => {
    const dataEl = document.getElementById('inline-articles-data');
    if (dataEl) {
      try {
        const data = JSON.parse(dataEl.textContent);
        ALL_ARTICLES = data;
        hydrateFilters(data);
        renderArchive();
      } catch (e) {
        document.getElementById('count').textContent = 'Archive failed to load.';
      }
    } else {
      document.getElementById('count').textContent = 'Archive loads when the site is served over HTTP.';
    }
  });"""

if old_fetch_block in html:
    html = html.replace(old_fetch_block, new_fetch_block)
    print("Successfully replaced fetch block.")
else:
    # Alternative match just in case spacing differs slightly
    print("WARNING: Exact old fetch block not found. Trying flexible replacement...")
    # We will search using regex
    import re
    pattern = re.compile(r"fetch\('/content/articles\.json.*?\}\);", re.DOTALL)
    if pattern.search(html):
        html = pattern.sub(new_fetch_block, html)
        print("Successfully replaced fetch block via regex.")
    else:
        print("ERROR: Fetch block not found in html!")
        exit(1)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Archive inlining successfully completed!")
