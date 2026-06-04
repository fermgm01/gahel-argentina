from analysis.fci_analyzer import analizar_universo_fci


def generar_inteligencia_mercado():
    resumen = analizar_universo_fci()

    insights = []
    for categoria, datos in resumen.items():
        insights.append({
            "categoria": categoria,
            "cantidad_fondos": datos.get("cantidad", 0),
            "patrimonio_total": datos.get("patrimonio_total", 0),
        })

    insights_ordenados = sorted(
        insights,
        key=lambda x: x["patrimonio_total"],
        reverse=True,
    )

    patrimonio_total = sum(item["patrimonio_total"] for item in insights_ordenados)

    for item in insights_ordenados:
        item["porcentaje_mercado"] = round(
            (item["patrimonio_total"] / patrimonio_total) * 100,
            2,
        ) if patrimonio_total > 0 else 0

    dominante = insights_ordenados[0] if insights_ordenados else {
        "categoria": "SIN DATOS",
        "cantidad_fondos": 0,
        "patrimonio_total": 0,
        "porcentaje_mercado": 0,
    }

    return {
        "ranking": insights_ordenados,
        "dominante": dominante,
    }


if __name__ == "__main__":
    inteligencia = generar_inteligencia_mercado()
    print("CATEGORÍA DOMINANTE:")
    print(inteligencia["dominante"])
