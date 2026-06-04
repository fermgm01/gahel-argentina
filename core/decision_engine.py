def _macro_value(data):
    macro = data.get("macro", {})
    inflacion = macro.get("inflacion_esperada", "media")
    tasa_real = macro.get("tasa_real", "neutral")
    return inflacion, tasa_real


def calcular_score_riesgo(data, senal_fci, contexto):
    dolar = data.get("dolar", {})
    brecha = float(dolar.get("brecha", 0) or 0)
    mep = float(dolar.get("mep", 0) or 0)
    oficial = float(dolar.get("oficial", 0) or 0)
    inflacion, tasa_real = _macro_value(data)

    score = 0

    if brecha < 2:
        score += 1
    elif brecha < 5:
        score += 2
    else:
        score += 4

    if inflacion == "alta":
        score += 1
    elif inflacion == "media":
        score += 1.5
    else:
        score += 0.5

    if tasa_real == "positiva":
        score += 1
    elif tasa_real == "negativa":
        score += 0.5

    if oficial and abs(mep - oficial) > 100:
        score += 2
    else:
        score += 1

    score += float(senal_fci.get("ajuste_riesgo", 0) or 0)

    if contexto.get("regimen") == "TENSIÓN CAMBIARIA":
        score += 2
    elif contexto.get("regimen") == "DEFENSIVO":
        score += 1

    return round(score, 2)


def definir_riesgo(score):
    if score <= 3:
        return "BAJO"
    if score <= 5:
        return "MEDIO"
    return "ALTO"


def generar_estrategia(riesgo, contexto):
    regimen = contexto.get("regimen", "NEUTRO")

    if regimen == "DEFENSIVO":
        return {
            "Liquidez": "45%",
            "CER": "40%",
            "Cobertura dólar": "15%",
        }

    if regimen == "TENSIÓN CAMBIARIA":
        return {
            "Liquidez": "40%",
            "CER": "30%",
            "Cobertura dólar": "30%",
        }

    if riesgo == "BAJO":
        return {
            "Liquidez": "35%",
            "CER": "50%",
            "Cobertura dólar": "15%",
        }

    if riesgo == "MEDIO":
        return {
            "Liquidez": "45%",
            "CER": "40%",
            "Cobertura dólar": "15%",
        }

    return {
        "Liquidez": "50%",
        "CER": "25%",
        "Cobertura dólar": "25%",
    }


def generar_motivos(data, senal_fci, contexto):
    dolar = data.get("dolar", {})
    brecha = float(dolar.get("brecha", 0) or 0)
    inflacion, tasa_real = _macro_value(data)
    motivos = []

    if brecha < 2:
        motivos.append("Dólar estable y sin estrés cambiario fuerte.")
    elif brecha >= 5:
        motivos.append("La brecha cambiaria empieza a mostrar tensión.")

    if senal_fci.get("senal") == "preferencia_liquidez":
        motivos.append("El mercado FCI está priorizando liquidez.")

    if inflacion == "alta":
        motivos.append("CER sigue teniendo valor, pero no para aumentar agresivamente.")

    if tasa_real == "positiva":
        motivos.append("La tasa favorece posiciones cortas y defensivas.")

    lectura = contexto.get("lectura")
    if lectura:
        motivos.append(lectura)

    # quitar duplicados sin perder orden
    vistos = set()
    limpios = []
    for motivo in motivos:
        if motivo not in vistos:
            limpios.append(motivo)
            vistos.add(motivo)

    return limpios[:4]


def generar_recomendacion(riesgo, contexto):
    regimen = contexto.get("regimen", "NEUTRO")

    if regimen == "DEFENSIVO":
        return (
            "Mantener liquidez alta. No aumentar CER agresivamente. "
            "Sostener cobertura dólar moderada."
        )

    if regimen == "TENSIÓN CAMBIARIA":
        return (
            "Reducir exposición larga en pesos. Aumentar cobertura dólar "
            "y priorizar liquidez."
        )

    if riesgo == "BAJO":
        return (
            "Mantener cartera balanceada. CER sigue razonable, con cobertura parcial."
        )

    if riesgo == "ALTO":
        return (
            "Priorizar defensa: liquidez alta, menor CER y mayor cobertura dólar."
        )

    return (
        "Mantener prudencia. Evitar aumentar riesgo hasta que el mercado salga "
        "del modo defensivo."
    )


def analyze_market(data, senal_fci, contexto=None):
    contexto = contexto or {}
    score = calcular_score_riesgo(data, senal_fci, contexto)
    riesgo = definir_riesgo(score)
    estrategia = generar_estrategia(riesgo, contexto)
    motivos = generar_motivos(data, senal_fci, contexto)
    recomendacion = generar_recomendacion(riesgo, contexto)

    return {
        "riesgo": riesgo,
        "score_riesgo": score,
        "estrategia": estrategia,
        "motivos": motivos,
        "recomendacion": recomendacion,
        "contexto": contexto,
    }
