import requests

def descargar_planilla_cafci():

    url = "https://api.pub.cafci.org.ar/estadisticas/informacion/diaria"

    try:

        response = requests.get(url, timeout=20)

        print("Status:", response.status_code)

        print("Tipo:", response.headers.get("content-type"))

        print("Tamaño:", len(response.content))

        with open("cafci_diaria.xlsx", "wb") as archivo:

            archivo.write(response.content)

        print("Planilla CAFCI descargada correctamente.")

    except Exception as e:

        print("ERROR CAFCI:", e)

if __name__ == "__main__":

    descargar_planilla_cafci()