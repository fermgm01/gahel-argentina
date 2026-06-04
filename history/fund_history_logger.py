import csv

import os

from datetime import datetime

ARCHIVO = "historial_fondos.csv"

def guardar_historial_fondos(comparacion):

    archivo_existe = os.path.exists(ARCHIVO)

    with open(ARCHIVO, mode="a", newline="", encoding="utf-8") as archivo:

        columnas = [

            "fecha_registro",

            "fondo",

            "categoria",

            "fecha_dato",

            "vcp",

            "patrimonio",

            "ranking_categoria",

            "cantidad_categoria",

            "interpretacion",

            "promedio_vcp_categoria"

        ]

        writer = csv.DictWriter(archivo, fieldnames=columnas)

        if not archivo_existe:

            writer.writeheader()

        for item in comparacion:

            writer.writerow({

                "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

                "fondo": item.get("fondo"),

                "categoria": item.get("categoria"),

                "fecha_dato": item.get("fecha"),

                "vcp": item.get("vcp"),

                "patrimonio": item.get("patrimonio"),

                "ranking_categoria": item.get("ranking_categoria"),

                "cantidad_categoria": item.get("cantidad_categoria"),

                "interpretacion": item.get("interpretacion"),

                "promedio_vcp_categoria": item.get("promedio_vcp_categoria")

            })