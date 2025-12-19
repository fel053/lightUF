import requests
from datetime import datetime
import locale


def obtener_uf():
    """
    Obtiene el valor de la UF del día desde mindicador.cl
    Retorna:
      - valor UF (float)
      - fecha formateada en español
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

    # Formato humano (ej: 17 de diciembre de 2025)
    try:
        locale.setlocale(locale.LC_TIME, "es_CL.UTF-8")
    except:
        pass  # por si el locale no está disponible en Windows

    fecha = fecha_dt.strftime("%d de %B de %Y")

    return valor, fecha
