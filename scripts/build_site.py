from pathlib import Path
import re
import shutil

import markdown


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "_site"
ASSET_EXTENSIONS = {".css", ".js"}
CSS_SOURCE = ROOT / "assets" / "course-ui.css"


SKIP_DIRS = {".git", ".github", "_site", "scripts", "__pycache__"}


def clean_site() -> None:
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)


def page_title(markdown_text: str, fallback: str) -> str:
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def rewrite_links(html: str) -> str:
    return re.sub(r'href="([^"#?]+)\.md([^"]*)"', r'href="\1.html\2"', html)


def css_href_for(output_file: Path) -> str:
    relative = Path("../" * (len(output_file.relative_to(SITE).parents) - 1))
    css_path = relative / "assets" / "course-ui.css"
    return css_path.as_posix()


def rel_root_for(output_file: Path) -> str:
    return "../" * (len(output_file.relative_to(SITE).parents) - 1)


def add_login_gate(html: str, target: Path) -> str:
    if target.name == "login.html" or "data-require-login=" in html:
        return html

    rel_root = rel_root_for(target)
    script = f'    <script src="{rel_root}assets/user-session.js" defer></script>\n'

    if "user-session.js" not in html:
        html = re.sub(r"(</head>)", script + r"\1", html, count=1, flags=re.IGNORECASE)

    body_attrs = f'<body data-require-login="true" data-login-url="{rel_root}login.html"'
    html = re.sub(r"<body\b", body_attrs, html, count=1, flags=re.IGNORECASE)
    return html


def render_markdown(source: Path, target: Path) -> None:
    text = source.read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["toc", "fenced_code", "sane_lists"])
    body = rewrite_links(body)
    title = page_title(text, source.stem.replace("_", " "))
    css_href = css_href_for(target)
    rel_root = rel_root_for(target)

    html = f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title} | Generative AI Course</title>
    <link rel="stylesheet" href="{css_href}">
    <script src="{rel_root}assets/user-session.js" defer></script>
  </head>
  <body data-require-login="true" data-login-url="{rel_root}login.html">
    <header class="site-header">
      <nav class="nav-shell" aria-label="Course navigation">
        <a class="brand" href="{rel_root}index.html">Generative AI Course</a>
        <div class="nav-links">
          <a href="{rel_root}index.html#modules">Modules</a>
          <a href="{rel_root}Foundation_week1/README.html">Foundation Week 1</a>
          <a href="https://www.linkedin.com/in/abhinav-kanduri-a943b9353/">LinkedIn</a>
          <span class="user-chip" data-user-chip hidden></span>
          <button class="nav-button" type="button" data-logout hidden>Logout</button>
        </div>
      </nav>
    </header>
    <main class="markdown-page">
{body}
    </main>
    <footer class="site-footer">
      <p>Created by Abhinav Kanduri for knowledge transfer only.</p>
      <a href="https://www.linkedin.com/in/abhinav-kanduri-a943b9353/">Connect on LinkedIn</a>
    </footer>
  </body>
</html>
"""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html, encoding="utf-8")


def copy_static_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    if source.suffix.lower() == ".html":
        text = source.read_text(encoding="utf-8")
        text = rewrite_links(text)
        text = add_login_gate(text, target)
        target.write_text(text, encoding="utf-8")
    else:
        shutil.copy2(source, target)


def build() -> None:
    clean_site()

    if CSS_SOURCE.exists():
        copy_static_file(CSS_SOURCE, SITE / "assets" / "course-ui.css")

    for source in ROOT.rglob("*"):
        if not source.is_file() or should_skip(source):
            continue

        rel = source.relative_to(ROOT)
        if source.suffix.lower() == ".md":
            render_markdown(source, (SITE / rel).with_suffix(".html"))
        elif source.suffix.lower() in {".html", ".pdf", ".png", ".jpg", ".jpeg", ".webp", ".svg"} | ASSET_EXTENSIONS:
            copy_static_file(source, SITE / rel)


if __name__ == "__main__":
    build()
    print(f"Built site at {SITE}")
