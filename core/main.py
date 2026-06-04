from core.config_loader import load_environment
load_environment()

from data.data_sources import get_market_data
from core.decision_engine import analyze_market
from reports.report_generator import generate_report
from automation.telegram_sender import enviar_mensaje
from history.history_logger import save_report, load_last_report
from core.logger import registrar_log
from analysis.market_intelligence import generar_inteligencia_mercado
from analysis.fci_signal import generar_senal_fci
from analysis.argentina_context_engine import analizar_contexto_argentina


def detectar_cambios(reporte_anterior, analysis):
    cambios = []

    if not reporte_anterior:
        return ["Aún no hay suficiente histórico para comparar."]

    riesgo_actual = analysis.get("riesgo")
    regimen_actual = (analysis.get("contexto") or {}).get("regimen")

    if f"Riesgo: {riesgo_actual}" not in reporte_anterior:
        cambios.append(f"El riesgo actual es {riesgo_actual}.")

    if regimen_actual and f"Régimen argentino: {regimen_actual}" not in reporte_anterior:
        cambios.append(f"El régimen actual es {regimen_actual}.")

    if not cambios:
        cambios.append("Sin cambios relevantes respecto al registro anterior.")

    return cambios


def main():
    try:
        registrar_log("Inicio de ejecución de Gahel Argentina.")

        data = get_market_data()
        inteligencia = generar_inteligencia_mercado()
        inteligencia_fci = inteligencia.get("ranking", []) if isinstance(inteligencia, dict) else inteligencia
        senal_fci = generar_senal_fci(inteligencia_fci)
        contexto = analizar_contexto_argentina(data, senal_fci)
        analysis = analyze_market(data, senal_fci, contexto)

        reporte_anterior = load_last_report()
        cambios = detectar_cambios(reporte_anterior, analysis)

        report = generate_report(data, analysis, cambios, inteligencia_fci)

        print(report)
        enviar_mensaje(report)
        save_report(report)

        registrar_log("Ejecución finalizada correctamente.")

    except Exception as error:
        registrar_log(f"ERROR GENERAL: {error}")
        raise


if __name__ == "__main__":
    main()
