import requests
from datetime import datetime


MESES_ES = [
    "enero", "febrero", "marzo", "abril", "mayo", "junio",
    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
]


def obtener_uf():
    """
    Obtiene el valor de la UF del día desde mindicador.cl
    Retorna:
      - valor UF (float)
      - fecha formateada en español (ej: 26 de diciembre de 2025)
    """

    url = "https://mindicador.cl/api/uf"

    r = requests.get(url, timeout=10)
    r.raise_for_status()

    data = r.json()
    registro = data["serie"][0]

    valor = registro["valor"]
    fecha_raw = registro["fecha"]

    # Convertimos fecha ISO a objeto datetime
    fecha_dt = datetime.fromisoformat(
        fecha_raw.replace("Z", "")
    )

    # Fecha en español SIN locale
    fecha = (
        f"{fecha_dt.day} de "
        f"{MESES_ES[fecha_dt.month - 1]} de "
        f"{fecha_dt.year}"
    )

    return valor, fecha
