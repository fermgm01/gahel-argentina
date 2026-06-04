from data.fci_sources import obtener_fci_renta_fija

from analysis.fci_classifier import clasificar_fondo

from history.fund_history_logger import guardar_historial_fondos

MIS_FONDOS = [

    "CHAMPA",

    "CHAMPAQUI",

    "CHAMPAQUÍ"

]

def interpretar_ranking(posicion, total):

    if posicion is None or total == 0:

        return "Sin ranking disponible."

    percentil = round((posicion / total) * 100, 2)

    if percentil <= 10:

        return "Fondo líder dentro de su categoría."

    elif percentil <= 25:

        return "Fondo relevante y bien posicionado."

    elif percentil <= 50:

        return "Fondo de posición media dentro de su categoría."

    else:

        return "Fondo marginal o con baja participación relativa."

def buscar_mis_fondos():

    fondos = obtener_fci_renta_fija()

    encontrados = []

    for fondo in fondos:

        nombre = fondo.get("fondo", "")

        for clave in MIS_FONDOS:

            if clave in nombre.upper():

                encontrados.append({

                    "fondo": nombre,

                    "categoria": clasificar_fondo(nombre),

                    "fecha": fondo.get("fecha"),

                    "vcp": fondo.get("vcp"),

                    "ccp": fondo.get("ccp"),

                    "patrimonio": fondo.get("patrimonio") or 0

                })

    return encontrados

def ranking_categoria(categoria):

    fondos = obtener_fci_renta_fija()

    comparables = []

    for fondo in fondos:

        nombre = fondo.get("fondo", "")

        if clasificar_fondo(nombre) == categoria:

            comparables.append({

                "fondo": nombre,

                "patrimonio": fondo.get("patrimonio") or 0,

                "vcp": fondo.get("vcp"),

                "fecha": fondo.get("fecha")

            })

    return sorted(

        comparables,

        key=lambda x: x["patrimonio"],

        reverse=True

    )

def calcular_promedio_vcp(comparables):

    vcps = []

    for fondo in comparables:

        vcp = fondo.get("vcp")

        if isinstance(vcp, (int, float)) and vcp > 0:

            vcps.append(vcp)

    if not vcps:

        return None

    return round(sum(vcps) / len(vcps), 4)

def comparar_champaqui_vs_mercado():

    mis_fondos = buscar_mis_fondos()

    resultado = []

    for mi_fondo in mis_fondos:

        categoria = mi_fondo.get("categoria")

        ranking = ranking_categoria(categoria)

        posicion = None

        for i, fondo in enumerate(ranking, start=1):

            if fondo["fondo"] == mi_fondo["fondo"]:

                posicion = i

                break

        promedio_vcp_categoria = calcular_promedio_vcp(ranking)

        resultado.append({

            "fondo": mi_fondo.get("fondo"),

            "categoria": categoria,

            "fecha": mi_fondo.get("fecha"),

            "vcp": mi_fondo.get("vcp"),

            "patrimonio": mi_fondo.get("patrimonio"),

            "ranking_categoria": posicion,

            "cantidad_categoria": len(ranking),

            "interpretacion": interpretar_ranking(posicion, len(ranking)),

            "promedio_vcp_categoria": promedio_vcp_categoria

        })

    return resultado

if __name__ == "__main__":

    comparacion = comparar_champaqui_vs_mercado()

    guardar_historial_fondos(comparacion)

    print("\nANÁLISIS CHAMPAQUÍ VS MERCADO:\n")

    if not comparacion:

        print("No se encontraron fondos Champaquí.")

    for item in comparacion:

        print(f"Fondo: {item['fondo']}")

        print(f"Categoría: {item['categoria']}")

        print(f"Fecha: {item['fecha']}")

        print(f"VCP: {item['vcp']}")

        print(f"Patrimonio: {item['patrimonio']}")

        print(

            f"Ranking categoría: "

            f"{item['ranking_categoria']} "

            f"de {item['cantidad_categoria']}"

        )

        print(f"Lectura: {item['interpretacion']}")

        print(f"Promedio VCP categoría: {item['promedio_vcp_categoria']}")

        print()

    print("Historial de fondos actualizado.")