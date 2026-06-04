import csv

import os

ARCHIVO = "historial_fondos.csv"

def leer_historial():

    if not os.path.exists(ARCHIVO):

        return []

    with open(

        ARCHIVO,

        mode="r",

        encoding="utf-8"

    ) as archivo:

        reader = csv.DictReader(archivo)

        return list(reader)

def obtener_registros_fondo(fondo, historial):

    registros = []

    for item in historial:

        if item.get("fondo") == fondo:

            registros.append(item)

    return registros

def interpretar_variacion(variacion):

    if variacion > 1:

        return "Mejora fuerte del fondo."

    elif variacion > 0:

        return "Mejora moderada del fondo."

    elif variacion == 0:

        return "Sin cambios relevantes."

    elif variacion > -1:

        return "Deterioro moderado del fondo."

    else:

        return "Deterioro fuerte del fondo."

def analizar_variacion_vcp():

    historial = leer_historial()

    fondos = set()

    for item in historial:

        fondos.add(item.get("fondo"))

    resultados = []

    for fondo in fondos:

        registros = obtener_registros_fondo(

            fondo,

            historial

        )

        if len(registros) < 2:

            continue

        anterior = registros[-2]

        actual = registros[-1]

        try:

            vcp_anterior = float(

                anterior.get("vcp", 0)

            )

            vcp_actual = float(

                actual.get("vcp", 0)

            )

            variacion = round(

                (

                    (

                        vcp_actual - vcp_anterior

                    ) / vcp_anterior

                ) * 100,

                4

            )

            interpretacion = interpretar_variacion(

                variacion

            )

            resultados.append({

                "fondo": fondo,

                "vcp_anterior": vcp_anterior,

                "vcp_actual": vcp_actual,

                "variacion_pct": variacion,

                "interpretacion": interpretacion

            })

        except:

            continue

    return resultados

if __name__ == "__main__":

    resultados = analizar_variacion_vcp()

    print("\nANÁLISIS HISTÓRICO DE PERFORMANCE:\n")

    if not resultados:

        print(

            "Todavía no hay suficiente histórico."

        )

    for item in resultados:

        print(f"Fondo: {item['fondo']}")

        print(f"VCP anterior: {item['vcp_anterior']}")

        print(f"VCP actual: {item['vcp_actual']}")

        print(

            f"Variación: "

            f"{item['variacion_pct']}%"

        )

        print(

            f"Lectura: "

            f"{item['interpretacion']}"

        )

        print()