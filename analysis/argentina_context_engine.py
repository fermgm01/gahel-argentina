def analizar_contexto_argentina(data, senal_fci):
    dolar = data.get("dolar", {})
    macro = data.get("macro", {})

    brecha = float(dolar.get("brecha", 0) or 0)
    inflacion = macro.get("inflacion_esperada", "media")
    tasa_real = macro.get("tasa_real", "neutral")
    categoria = senal_fci.get("categoria_dominante", "")
    porcentaje = float(senal_fci.get("porcentaje_dominante", 0) or 0)

    regimen = "NEUTRO"
    lectura = []

    if categoria == "MONEY MARKET / LIQUIDEZ" and porcentaje >= 35:
        regimen = "DEFENSIVO"
        lectura.append("El mercado está priorizando liquidez de corto plazo.")

    if brecha < 2:
        lectura.append("No hay estrés cambiario fuerte.")
    elif brecha >= 5:
        regimen = "TENSIÓN CAMBIARIA"
        lectura.append("La brecha empieza a marcar tensión cambiaria.")

    if inflacion == "alta":
        lectura.append("La inflación sostiene valor en instrumentos CER, pero sin agresividad.")

    if tasa_real == "positiva":
        lectura.append("La tasa real positiva favorece posiciones cortas y líquidas.")

    if not lectura:
        lectura.append("El mercado no muestra una señal dominante clara.")

    return {
        "regimen": regimen,
        "lectura": " ".join(lectura),
        "categoria_dominante": categoria,
        "porcentaje_dominante": porcentaje,
    }
