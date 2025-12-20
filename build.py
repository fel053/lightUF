from backend.fetch_uf import obtener_uf
from backend.generate_pages import (
    generar_tabla,
    generar_htmls_estaticos,
    generar_html_humano
)
from backend.generate_sitemap import generar_sitemap
from backend.generate_robots import generar_robots
from backend.generate_index import generar_index

BASE_URL = "https://ufsimple.cl"


def build():
    uf_valor, fecha = obtener_uf()

    tabla = generar_tabla(uf_valor)

    generar_htmls_estaticos(tabla, fecha, BASE_URL)
    generar_html_humano(tabla, uf_valor)

    generar_sitemap(tabla, BASE_URL)
    generar_robots(BASE_URL)
    generar_index()


if __name__ == "__main__":
    build()
