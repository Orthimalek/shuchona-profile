from scholarly import scholarly

# Google Scholar ID for Shuchona Malek Orthi
scholar_id = "BDil2hgAAAAJ"

# Fetch author profile and publications
author = scholarly.search_author_id(scholar_id)
author = scholarly.fill(author, sections=["publications"])

publications = author.get("publications", [])[:10]

# Build styled HTML cards for each publication
html_output = ""
for pub in publications:
    pub = scholarly.fill(pub)
    bib   = pub.get("bib", {})
    title = bib.get("title", "Untitled")
    venue = bib.get("venue", bib.get("journal", ""))
    year  = bib.get("pub_year", "")
    url   = pub.get("pub_url", "#")

    html_output += f'''      <div class="pub-card">
        <div class="pub-meta">
          <span class="badge badge-pub">Published</span>
          <span class="pub-year">{year}</span>
        </div>
        <h3><a href="{url}" target="_blank">{title}</a></h3>
        <div class="pub-venue">{venue}</div>
      </div>\n'''

# Read index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace content between markers
start_marker = "<!-- START_PUBLICATIONS -->"
end_marker   = "<!-- END_PUBLICATIONS -->"

if start_marker in content and end_marker in content:
    start_idx = content.index(start_marker) + len(start_marker)
    end_idx   = content.index(end_marker)
    updated   = content[:start_idx] + "\n" + html_output + "      " + content[end_idx:]

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"✅ {len(publications)} publications injected into index.html")
else:
    print("❌ Could not find publication markers in index.html")
