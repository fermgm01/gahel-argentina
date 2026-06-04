from data.fci_sources import obtener_fci_renta_fija

from analysis.fci_classifier import clasificar_fondo

def analizar_universo_fci():

    fondos = obtener_fci_renta_fija()

    resumen = {}

    for fondo in fondos:

        nombre = fondo.get("fondo", "")

        patrimonio = fondo.get("patrimonio", 0) or 0

        categoria = clasificar_fondo(nombre)

        if categoria not in resumen:

            resumen[categoria] = {

                "cantidad": 0,

                "patrimonio_total": 0,

                "fondos": []

            }

        resumen[categoria]["cantidad"] += 1

        resumen[categoria]["patrimonio_total"] += patrimonio

        resumen[categoria]["fondos"].append(fondo)

    return resumen

if __name__ == "__main__":

    resumen = analizar_universo_fci()

    print("\nRESUMEN UNIVERSO FCI CLASIFICADO:\n")

    for categoria, datos in resumen.items():

        print(f"Categoría: {categoria}")

        print(f"Cantidad de fondos: {datos['cantidad']}")

        print(f"Patrimonio total: {datos['patrimonio_total']}")

        print()