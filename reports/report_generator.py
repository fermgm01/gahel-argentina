from datetime import datetime


def _dedupe(items):
    vistos = set()
    salida = []
    for item in items or []:
        if item and item not in vistos:
            salida.append(item)
            vistos.add(item)
    return salida


def generate_report(data, analysis, cambios=None, inteligencia_fci=None):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    dolar = data.get("dolar", {})
    riesgo = analysis.get("riesgo", "MEDIO")
    score = analysis.get("score_riesgo", 0)
    estrategia = analysis.get("estrategia", {})
    recomendacion = analysis.get("recomendacion", "")
    contexto = analysis.get("contexto", {})
    motivos = _dedupe(analysis.get("motivos", []))
    cambios = _dedupe(cambios or [])
    inteligencia_fci = inteligencia_fci or []
    dominante = inteligencia_fci[0] if inteligencia_fci else None

    if riesgo == "BAJO":
        conclusion = "🟢 Contexto controlado. Mantener equilibrio."
    elif riesgo == "MEDIO":
        conclusion = "🟡 Mercado defensivo. Prudencia y liquidez."
    else:
        conclusion = "🔴 Riesgo alto. Priorizar defensa."

    reporte = f"""SITUACIÓN HOY — {fecha}

CONCLUSIÓN:
{conclusion}

QUÉ CAMBIÓ:
"""

    for cambio in cambios:
        reporte += f"- {cambio}\n"

    reporte += "\nLECTURA DEL MERCADO:\n"
    reporte += f"- Brecha MEP/oficial: {dolar.get('brecha')}%.\n"

    if dominante:
        reporte += (
            f"- FCI dominante: {dominante.get('categoria')} "
            f"({dominante.get('porcentaje_mercado')}%).\n"
        )

    regimen = contexto.get("regimen")
    lectura_contexto = contexto.get("lectura")
    if regimen:
        reporte += f"- Régimen argentino: {regimen}.\n"
    if lectura_contexto:
        reporte += f"- {lectura_contexto}\n"

    for motivo in motivos[:2]:
        if motivo != lectura_contexto:
            reporte += f"- {motivo}\n"

    reporte += "\nPOSICIONAMIENTO SUGERIDO:\n"
    for categoria, porcentaje in estrategia.items():
        reporte += f"- {categoria}: {porcentaje}\n"

    reporte += f"\nACCIÓN SUGERIDA:\n{recomendacion}\n"

    reporte += f"\nDATOS TÉCNICOS:\n- Riesgo: {riesgo}\n- Score: {score}\n- Oficial: ${dolar.get('oficial')}\n- MEP: ${dolar.get('mep')}\n- CCL: ${dolar.get('ccl')}\n"

    return reporte.strip()
