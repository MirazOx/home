import os
import re
import json

ROOT_DIR = "/Users/miraz/.gemini/antigravity/scratch/miraz-redesign"

def make_relative(url, file_level):
    if not url:
        return url
    if url.startswith("//"):
        return url
    if url.startswith("http:") or url.startswith("https:") or url.startswith("mailto:") or url.startswith("tel:"):
        return url
    if not url.startswith("/"):
        return url
        
    prefix = ""
    if file_level > 0:
        prefix = "../" * file_level
        
    path = url[1:]
    if not path:
        return prefix + "index.html"
        
    if path.endswith("/"):
        path += "index.html"
        
    return prefix + path

def transform_json_value(value, file_level):
    if isinstance(value, str):
        if value.startswith("/") and not value.startswith("//"):
            return make_relative(value, file_level)
        return value
    elif isinstance(value, list):
        return [transform_json_value(item, file_level) for item in value]
    elif isinstance(value, dict):
        return {key: transform_json_value(val, file_level) for key, val in value.items()}
    return value

def process_html_file(filepath):
    # Determine level relative to ROOT_DIR
    rel_dir = os.path.relpath(os.path.dirname(filepath), ROOT_DIR)
    if rel_dir == ".":
        file_level = 0
    else:
        file_level = len(rel_dir.split(os.sep))
        
    print(f"Processing: {filepath} (Level {file_level})")
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
        
    # 1. Replace HTML attributes starting with / (excluding //)
    # Regex matches: href|src|data-full|action = " /... " or ' /... '
    attr_pattern = re.compile(r'(href|src|data-full|action)=["\'](/[^/][^"\']*|/)["\']')
    
    def attr_replacer(match):
        attr_name = match.group(1)
        url = match.group(2)
        rel_url = make_relative(url, file_level)
        return f'{attr_name}="{rel_url}"'
        
    html = attr_pattern.sub(attr_replacer, html)
    
    # 2. Parse and update <script type="application/json"> blocks
    json_script_pattern = re.compile(r'(<script\s+type=["\']application/json["\']\s+id=["\'][^"\']+["\']\s*>)(.*?)(</script>)', re.DOTALL)
    
    def json_replacer(match):
        start_tag = match.group(1)
        json_content = match.group(2)
        end_tag = match.group(3)
        try:
            data = json.loads(json_content)
            transformed_data = transform_json_value(data, file_level)
            new_json_content = json.dumps(transformed_data, ensure_ascii=False)
            return start_tag + new_json_content + end_tag
        except Exception as e:
            print(f"  WARNING: Failed to parse JSON script tag in {filepath}: {str(e)}")
            return match.group(0)
            
    html = json_script_pattern.sub(json_replacer, html)
    
    # 3. Handle fetch fallbacks if any hardcoded absolute paths exist in JS script blocks
    # Replace fetch('/content/...') with fetch('../content/...') or similar
    js_fetch_pattern = re.compile(r"fetch\(['\"](/content/[^'\"]+)['\"]\)")
    
    def js_fetch_replacer(match):
        url = match.group(1)
        rel_url = make_relative(url, file_level)
        return f"fetch('{rel_url}')"
        
    html = js_fetch_pattern.sub(js_fetch_replacer, html)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"  Successfully processed: {filepath}")

def main():
    html_files = []
    for root, dirs, files in os.walk(ROOT_DIR):
        if ".git" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
                
    print(f"Found {len(html_files)} HTML files to process.")
    for file in html_files:
        process_html_file(file)
        
    print("\nAll HTML files successfully made portable!")

if __name__ == "__main__":
    main()
