from pathlib import Path

def generar_index():
    html = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url=/uf/">
  <title>UF hoy</title>
</head>
<body>
</body>
</html>
"""
    Path("output/index.html").write_text(html, encoding="utf-8")
