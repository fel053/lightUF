from pathlib import Path
from datetime import date

def generar_sitemap(tabla_ufs, base_url):
    today = date.today().isoformat()

    urls = []
    for uf in tabla_ufs:
        urls.append(f"""
  <url>
    <loc>{base_url}/uf/{uf}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
""")

    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{''.join(urls)}
</urlset>
"""

    output_path = Path("output/sitemap.xml")

    print("→ Guardando sitemap en:", output_path.resolve())

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(sitemap.strip(), encoding="utf-8")

    print("✔ sitemap.xml generado correctamente")
