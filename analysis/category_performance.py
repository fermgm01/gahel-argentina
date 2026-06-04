from analysis.fund_history_analyzer import analizar_variacion_vcp

def comparar_performance_categoria():

    resultados = analizar_variacion_vcp()

    if not resultados:

        return []

    categorias = {}

    for item in resultados:

        fondo = item.get("fondo", "")

        variacion = item.get("variacion_pct", 0)

        # Por ahora agrupamos Champaquí separado.

        # Luego lo conectamos con categoría real.

        categoria = "CHAMPAQUI" if "CHAMPA" in fondo.upper() else "OTROS"

        if categoria not in categorias:

            categorias[categoria] = []

        categorias[categoria].append(variacion)

    resumen = []

    for categoria, variaciones in categorias.items():

        promedio = round(sum(variaciones) / len(variaciones), 4)

        resumen.append({

            "categoria": categoria,

            "promedio_variacion": promedio,

            "cantidad": len(variaciones)

        })

    return resumen

if __name__ == "__main__":

    resumen = comparar_performance_categoria()

    print("\nPERFORMANCE POR CATEGORÍA:\n")

    if not resumen:

        print("Todavía no hay suficiente histórico.")

    for item in resumen:

        print(f"Categoría: {item['categoria']}")

        print(f"Variación promedio: {item['promedio_variacion']}%")

        print(f"Cantidad fondos: {item['cantidad']}")
