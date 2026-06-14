#!/usr/bin/env python3
"""Convert the India semiconductor research markdown into a styled PDF."""
import markdown
from weasyprint import HTML

SRC = "india-semiconductor-market-research.md"
OUT = "India-Semiconductor-Market-Research.pdf"

with open(SRC, encoding="utf-8") as fh:
    md_text = fh.read()

html_body = markdown.markdown(
    md_text,
    extensions=["tables", "fenced_code", "toc", "sane_lists"],
)

css = """
@page {
    size: A4;
    margin: 1.8cm 1.6cm 2cm 1.6cm;
    @bottom-center {
        content: "India Semiconductor Market — Research Brief  •  Page " counter(page) " of " counter(pages);
        font-size: 8pt; color: #888;
    }
}
body {
    font-family: "Helvetica Neue", Arial, sans-serif;
    font-size: 10pt; line-height: 1.5; color: #1a1a1a;
}
h1 { font-size: 21pt; color: #0b3d5c; border-bottom: 3px solid #0b3d5c;
     padding-bottom: 6px; margin-top: 0; }
h2 { font-size: 14.5pt; color: #0b3d5c; margin-top: 22px;
     border-bottom: 1px solid #cdd9e1; padding-bottom: 3px; }
h3 { font-size: 11.5pt; color: #15598a; margin-top: 16px; }
p, li { font-size: 10pt; }
em { color: #444; }
strong { color: #0b2a3d; }
code { background: #eef2f5; padding: 1px 4px; border-radius: 3px;
       font-family: "Courier New", monospace; font-size: 8.8pt; }
table { border-collapse: collapse; width: 100%; margin: 10px 0;
        font-size: 8.6pt; }
th { background: #0b3d5c; color: #fff; text-align: left; padding: 5px 7px;
     border: 1px solid #0b3d5c; }
td { padding: 5px 7px; border: 1px solid #cdd9e1; vertical-align: top; }
tr:nth-child(even) td { background: #f4f7f9; }
hr { border: none; border-top: 1px solid #d5dde2; margin: 18px 0; }
a { color: #15598a; text-decoration: none; word-break: break-all; }
blockquote { border-left: 3px solid #c0392b; background: #fcefee;
             margin: 10px 0; padding: 6px 12px; color: #5a2a26; }
ul, ol { margin: 6px 0 6px 0; padding-left: 20px; }
li { margin: 2px 0; }
"""

full_html = f"<html><head><meta charset='utf-8'><style>{css}</style></head><body>{html_body}</body></html>"
HTML(string=full_html).write_pdf(OUT)
print(f"Wrote {OUT}")
