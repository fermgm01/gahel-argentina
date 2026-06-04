def calcular_riesgo_contextual(data, contexto):
    dolar = data.get("dolar", {})
    brecha = float(dolar.get("brecha", 0) or 0)
    regimen = contexto.get("regimen", "NEUTRO")

    score = 0

    if brecha < 2:
        score += 1
    elif brecha < 5:
        score += 2
    else:
        score += 4

    if regimen == "DEFENSIVO":
        score += 2
    elif regimen == "TENSIÓN CAMBIARIA":
        score += 4

    if score <= 3:
        return "BAJO", score
    if score <= 5:
        return "MEDIO", score
    return "ALTO", score
