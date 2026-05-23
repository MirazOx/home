import os
import re

ROOT_DIR = "/Users/miraz/.gemini/antigravity/scratch/miraz-redesign/"
BEYOND_DIR = os.path.join(ROOT_DIR, "beyond")

STANDARD_NAV = """<!-- ═══════════════ NAV ═══════════════ -->
<nav class="nav-modern" id="siteNav">
  <div class="nav-inner">
    <a href="/" class="nav-brand">MIRAZ</a>

    <button class="nav-hamburger" id="navHamburger" aria-label="Toggle navigation" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>

    <div class="nav-main" id="navMain">
      <a href="/research/">Research</a>
      <a href="/academic/">Academic</a>
      <a href="/writing/">Reportage</a>
      <a href="/interventions/">Interventions</a>
      <a href="/about/">About</a>
    </div>

    <div class="nav-actions">
      <button class="theme-toggle" id="themeToggle" type="button" aria-label="Toggle theme">
        <span class="toggle-track">
          <span class="toggle-thumb">
            <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
            <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"></circle><line x1="12" y1="2" x2="12" y2="4"></line><line x1="12" y1="20" x2="12" y2="22"></line><line x1="4.93" y1="4.93" x2="6.34" y2="6.34"></line><line x1="17.66" y1="17.66" x2="19.07" y2="19.07"></line><line x1="2" y1="12" x2="4" y2="12"></line><line x1="20" y1="12" x2="22" y2="12"></line><line x1="4.93" y1="19.07" x2="6.34" y2="17.66"></line><line x1="17.66" y1="6.34" x2="19.07" y2="4.93"></line></svg>
          </span>
        </span>
      </button>
    </div>
  </div>
</nav>"""

STANDARD_FOOTER = """<footer>
  <div class="container-wide">
    <p class="footer-text">© 2026 Md. Miraz Hossain · Dhaka, Bangladesh</p>
    <div class="footer-links">
      <a href="mailto:miraz8395@gmail.com">email</a>
      <a href="https://www.linkedin.com/in/miraz-hossain-a6b278180/" target="_blank" rel="noopener">linkedin</a>
      <a href="https://x.com/Miraz8395" target="_blank" rel="noopener">x</a>
      <a href="https://signal.me/#eu/ylklb4x-Gx18h3DzQjtP-vHmFn4lwtTe9dqiCG3wpY0onLpReQBBxoRr0dsrwCoA" target="_blank" rel="noopener">signal</a>
      <a href="/about/">about</a>
    </div>
  </div>
</footer>"""

def process_html_file(file_path):
    print(f"Processing: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace Nav
    # Match <nav class="nav-modern" id="siteNav"> ... </nav> across multiple lines
    nav_pattern = re.compile(r'<nav class="nav-modern" id="siteNav">.*?</nav>', re.DOTALL)
    if nav_pattern.search(content):
        content = nav_pattern.sub(STANDARD_NAV, content)
    else:
        print(f"WARNING: Nav not found in {file_path}")

    # Replace Footer
    # Match <footer> ... </footer> across multiple lines
    footer_pattern = re.compile(r'<footer>.*?</footer>', re.DOTALL)
    if footer_pattern.search(content):
        content = footer_pattern.sub(STANDARD_FOOTER, content)
    else:
        print(f"WARNING: Footer not found in {file_path}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully updated: {file_path}")

def main():
    # 1. Update index.html in subfolders
    for root, dirs, files in os.walk(BEYOND_DIR):
        for file in files:
            if file == "index.html" and root != BEYOND_DIR:
                file_path = os.path.join(root, file)
                process_html_file(file_path)

    # 2. Update the legacy files at the root of beyond/ just in case they are served
    for file in os.listdir(BEYOND_DIR):
        if file.endswith(".html") and file != "index.html":
            file_path = os.path.join(BEYOND_DIR, file)
            process_html_file(file_path)

if __name__ == "__main__":
    main()
