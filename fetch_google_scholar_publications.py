from scholarly import scholarly

# Google Scholar ID for Shuchona Malek Orthi
scholar_id = "BDil2hgAAAAJ"

# Fetch author profile and publications
author = scholarly.search_author_id(scholar_id)
author = scholarly.fill(author, sections=["publications"])

publications = author.get("publications", [])[:7]

# Build the HTML content
html_output = "<ul>\n"
for pub in publications:
    pub = scholarly.fill(pub)
    title = pub.get("bib", {}).get("title", "Untitled")
    url = pub.get("pub_url", "#")
    html_output += f'  <li><a href="{url}" target="_blank">{title}</a></li>\n'
html_output += "</ul>"

# Read index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace content between markers
start_marker = "<!-- START_PUBLICATIONS -->"
end_marker = "<!-- END_PUBLICATIONS -->"

if start_marker in content and end_marker in content:
    start_idx = content.index(start_marker) + len(start_marker)
    end_idx = content.index(end_marker)
    updated = content[:start_idx] + "\n" + html_output + "\n" + content[end_idx:]

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(updated)

    print("✅ Publications injected into index.html")
else:
    print("❌ Could not find publication markers in index.html")
