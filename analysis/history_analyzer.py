import csv

import os

ARCHIVO_HISTORIAL = "historial_reportes.csv"

def analizar_cambios_actuales(data, analysis):

    if not os.path.exists(ARCHIVO_HISTORIAL):

        return ["Sin histórico previo."]

    with open(

        ARCHIVO_HISTORIAL,

        mode="r",

        encoding="utf-8"

    ) as archivo:

        filas = list(csv.DictReader(archivo))

    if len(filas) < 2:

        return ["Aún no hay suficiente histórico para comparar."]

    anterior = filas[-2]

    cambios = []

    dolar_actual = data.get("dolar", {})

    brecha_actual = float(

        dolar_actual.get("brecha", 0)

    )

    brecha_anterior = float(

        anterior.get("brecha", 0)

    )

    if brecha_actual > brecha_anterior:

        cambios.append(

            "📈 Subió la brecha cambiaria."

        )

    elif brecha_actual < brecha_anterior:

        cambios.append(

            "📉 Bajó la brecha cambiaria."

        )

    score_actual = float(

        analysis.get("score_riesgo", 0)

    )

    score_anterior = float(

        anterior.get("score_riesgo", 0)

    )

    if score_actual > score_anterior:

        cambios.append(

            "⚠️ Aumentó el riesgo general."

        )

    elif score_actual < score_anterior:

        cambios.append(

            "✅ Disminuyó el riesgo general."

        )

    oficial_actual = float(

        dolar_actual.get("oficial", 0)

    )

    oficial_anterior = float(

        anterior.get("oficial", 0)

    )

    if oficial_actual > oficial_anterior:

        cambios.append(

            "💵 Subió el dólar oficial."

        )

    elif oficial_actual < oficial_anterior:

        cambios.append(

            "💵 Bajó el dólar oficial."

        )

    if not cambios:

        cambios.append(

            "Sin cambios relevantes respecto al registro anterior."

        )

    return cambios