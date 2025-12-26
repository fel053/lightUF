from pathlib import Path


def generar_tabla(uf_valor, max_uf=5000):
    """
    Genera una tabla UF -> CLP precalculada.
    Esta tabla actúa como nuestra 'base de datos'.
    """
    tabla = {}
    for uf in range(1, max_uf + 1):
        tabla[uf] = round(uf * uf_valor)
    return tabla


def generar_htmls_estaticos(tabla, fecha, base_url, uf_valor):
    """
    Genera una página HTML estática por cada valor de UF.
    Estas páginas son las que Google indexa.
    """
    template = Path("templates/uf_static.html").read_text(encoding="utf-8")

    for uf, clp in tabla.items():
        canonical = f"{base_url}/uf/{uf}/"

        html = (
            template
            .replace("{{UF}}", str(uf))
            .replace("{{CLP}}", f"{clp:,}".replace(",", "."))
            .replace("{{FECHA}}", fecha)
            .replace("{{CANONICAL_URL}}", canonical)
            # 👉 número PURO para JS
            .replace("{{UF_VALOR_NUM}}", str(uf_valor))
            # 👉 texto humano para footer
            .replace(
                "{{UF_VALOR_HUMANO}}",
                f"{round(uf_valor):,}".replace(",", ".")
            )
        )

        output_dir = Path(f"output/uf/{uf}")
        output_dir.mkdir(parents=True, exist_ok=True)

        (output_dir / "index.html").write_text(
            html,
            encoding="utf-8"
        )


def generar_html_humano(tabla, uf_valor):
    """
    Genera la página de exploración humana (/uf/index.html).
    Esta página NO es indexable y solo redirige.
    """
    template = Path("templates/uf_human.html").read_text(encoding="utf-8")

    html = (
        template
        # 👉 número PURO para la calculadora JS
        .replace("{{UF_VALOR_NUM}}", str(uf_valor))
        # 👉 texto humano visible
        .replace(
            "{{UF_VALOR_HUMANO}}",
            f"{round(uf_valor):,}".replace(",", ".")
        )
    )

    output_dir = Path("output/uf")
    output_dir.mkdir(parents=True, exist_ok=True)

    (output_dir / "index.html").write_text(
        html,
        encoding="utf-8"
    )
