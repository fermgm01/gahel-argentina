import requests

def obtener_dolarapi():

    try:

        response = requests.get(

            "https://dolarapi.com/v1/dolares",

            timeout=10

        )

        datos = response.json()

        resultado = {}

        for d in datos:

            casa = d.get("casa")

            venta = d.get("venta")

            if casa == "oficial":

                resultado["oficial"] = venta

            elif casa == "blue":

                resultado["blue"] = venta

            elif casa == "bolsa":

                resultado["mep"] = venta

            elif casa == "contadoconliqui":

                resultado["ccl"] = venta

        return resultado

    except Exception:

        return {}

def obtener_bluelytics():

    try:

        response = requests.get(

            "https://api.bluelytics.com.ar/v2/latest",

            timeout=10

        )

        data = response.json()

        oficial = data["oficial"]["value_sell"]

        blue = data["blue"]["value_sell"]

        return {

            "oficial": oficial,

            "blue": blue,

            "mep": round(oficial * 1.02, 2),

            "ccl": round(oficial * 1.05, 2)

        }

    except Exception:

        return {}

def elegir_fuente(dolarapi, bluelytics):

    if dolarapi.get("oficial") and dolarapi.get("mep"):

        return dolarapi, "DolarAPI"

    if bluelytics.get("oficial"):

        return bluelytics, "Bluelytics"

    return {

        "oficial": 0,

        "mep": 0,

        "ccl": 0,

        "blue": 0

    }, "Sin fuente"

def get_market_data():

    dolarapi = obtener_dolarapi()

    bluelytics = obtener_bluelytics()

    dolares, fuente = elegir_fuente(dolarapi, bluelytics)

    oficial = dolares.get("oficial", 0)

    mep = dolares.get("mep", 0)

    ccl = dolares.get("ccl", 0)

    blue = dolares.get("blue", 0)

    brecha = round(((mep - oficial) / oficial) * 100, 2) if oficial else 0

    return {

        "dolar": {

            "oficial": oficial,

            "mep": mep,

            "ccl": ccl,

            "blue": blue,

            "brecha": brecha,

            "fuente": fuente

        },

        "macro": {

            "inflacion_esperada": "alta",

            "tasa_real": "positiva"

        },

        "fondos": {

            "Champaquí Cobertura": {

                "riesgo": "medio"

            },

            "Champaquí Ahorro Pesos": {

                "riesgo": "bajo"

            }

        }

    }