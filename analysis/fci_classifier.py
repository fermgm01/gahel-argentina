CATEGORIAS = {

    "MONEY MARKET / LIQUIDEZ": [

        "MONEY",

        "LIQUIDEZ",

        "AHORRO",

        "T+0",

        "T0",

        "MARKET",

        "PESOS",

        "CUENTA"

    ],

    "DÓLAR": [

        "DOLAR",

        "DÓLAR",

        "USD",

        "HARD",

        "LINKED",

        "LATAM",

        "USA",

        "GLOBAL"

    ],

    "CER / INFLACIÓN": [

        "CER",

        "IPC",

        "INFLACION",

        "INFLACIÓN",

        "INDEX",

        "AJUSTE",

        "CERES",

        "REAL"

    ],

    "RENTA FIJA GENERAL": [

        "RENTA",

        "PLUS",

        "BONOS",

        "FIJA",

        "DEUDA",

        "INCOME",

        "SHORT",

        "MEDIANO",

        "LARGO"

    ],

    "ACCIONES": [

        "ACCIONES",

        "EQUITY",

        "VARIABLE",

        "MERV",

        "BURSATIL",

        "VALUE",

        "GROWTH",

        "SMALL",

        "CAP"

    ],

    "BALANCEADO": [

        "BALANCE",

        "MIXTO",

        "MIX",

        "MULTI",

        "ESTRATEGIA",

        "RETORNO"

    ]

}

MAPEO_DIRECTO = {

    "DELTA": "RENTA FIJA GENERAL",

    "QUINQUELA": "RENTA FIJA GENERAL",

    "GAINVEST": "RENTA FIJA GENERAL",

    "SCHRODER": "BALANCEADO",

    "GALILEO": "BALANCEADO",

    "COMPASS": "BALANCEADO",

    "CONSULATIO": "BALANCEADO",

    "SBS": "RENTA FIJA GENERAL",

    "PELLEGRINI": "MONEY MARKET / LIQUIDEZ",

    "SUPERFONDO": "MONEY MARKET / LIQUIDEZ"

}

def clasificar_fondo(nombre):

    nombre = nombre.upper()

    for clave, categoria in MAPEO_DIRECTO.items():

        if clave in nombre:

            return categoria

    coincidencias = {}

    for categoria, palabras in CATEGORIAS.items():

        coincidencias[categoria] = 0

        for palabra in palabras:

            if palabra in nombre:

                coincidencias[categoria] += 1

    mejor_categoria = max(

        coincidencias,

        key=coincidencias.get

    )

    if coincidencias[mejor_categoria] == 0:

        return "SIN CLASIFICAR"

    return mejor_categoria