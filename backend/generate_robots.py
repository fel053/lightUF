from pathlib import Path

def generar_robots(base_url: str):
    """
    Genera robots.txt para el sitio UF.
    - Permite indexar páginas /uf/{n}/
    - Bloquea la página humana /uf/index.html
    - Declara el sitemap
    """

    robots_txt = f"""User-agent: *
Allow: /uf/
Disallow: /uf/index.html

Sitemap: {base_url}/sitemap.xml
"""

    output_path = Path("output/robots.txt")

    print("→ Guardando robots.txt en:", output_path.resolve())

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(robots_txt.strip(), encoding="utf-8")

    print("✔ robots.txt generado correctamente")


if __name__ == "__main__":
    # En local puedes dejar localhost
    generar_robots("http://localhost:5500")
