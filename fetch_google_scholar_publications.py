
from scholarly import scholarly

# Google Scholar ID for Shuchona Malek Orthi
scholar_id = "BDil2hgAAAAJ"

# Fetch author profile
author = scholarly.search_author_id(scholar_id)
author = scholarly.fill(author, sections=["publications"])

# Extract top 7 recent publications
publications = author.get("publications", [])[:7]

html_output = "<ul>\n"
for pub in publications:
    pub = scholarly.fill(pub)
    title = pub.get("bib", {}).get("title", "Untitled")
    url = pub.get("pub_url", "#")
    html_output += f'  <li><a href="{url}" target="_blank">{title}</a></li>\n'
html_output += "</ul>"

# Save HTML snippet
with open("research_publications.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("✅ HTML snippet saved as 'research_publications.html'")
