import requests


def obtener_fci_renta_fija():
    url = "https://api.argentinadatos.com/v1/finanzas/fci/rentaFija/ultimo"

    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        datos = response.json()
        return datos if isinstance(datos, list) else []
    except Exception:
        return []


if __name__ == "__main__":
    fondos = obtener_fci_renta_fija()
    print("Cantidad de fondos:", len(fondos))
    if fondos:
        print("Primer fondo:")
        print(fondos[0])
