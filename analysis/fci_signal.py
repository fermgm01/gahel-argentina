def generar_senal_fci(inteligencia_fci):
    patrimonio_total = sum(
        item.get("patrimonio_total", 0) or 0
        for item in inteligencia_fci
    )

    if patrimonio_total <= 0:
        return {
            "senal": "sin_datos",
            "mensaje": "No hay datos suficientes de FCI.",
            "ajuste_riesgo": 0,
            "categoria_dominante": "SIN DATOS",
            "porcentaje_dominante": 0,
        }

    porcentajes = {}
    for item in inteligencia_fci:
        categoria = item.get("categoria", "SIN CLASIFICAR")
        patrimonio = item.get("patrimonio_total", 0) or 0
        porcentajes[categoria] = round((patrimonio / patrimonio_total) * 100, 2)

    categoria_dominante = max(porcentajes, key=porcentajes.get)
    porcentaje_dominante = porcentajes.get(categoria_dominante, 0)

    liquidez = porcentajes.get("MONEY MARKET / LIQUIDEZ", 0)
    dolar = porcentajes.get("DÓLAR", 0)
    cer = porcentajes.get("CER / INFLACIÓN", 0)
    renta_fija = porcentajes.get("RENTA FIJA GENERAL", 0)

    if dolar >= 25:
        return {
            "senal": "cobertura_dolar_fuerte",
            "mensaje": "Alta preferencia del mercado por cobertura dólar.",
            "ajuste_riesgo": 1,
            "categoria_dominante": categoria_dominante,
            "porcentaje_dominante": porcentaje_dominante,
        }

    if liquidez >= 35:
        return {
            "senal": "preferencia_liquidez",
            "mensaje": "El mercado muestra preferencia importante por liquidez.",
            "ajuste_riesgo": 0.5,
            "categoria_dominante": categoria_dominante,
            "porcentaje_dominante": porcentaje_dominante,
        }

    if cer >= 15:
        return {
            "senal": "interes_cer",
            "mensaje": "El mercado muestra interés relevante en fondos CER.",
            "ajuste_riesgo": -0.5,
            "categoria_dominante": categoria_dominante,
            "porcentaje_dominante": porcentaje_dominante,
        }

    if renta_fija >= 40:
        return {
            "senal": "preferencia_renta_fija",
            "mensaje": "El mercado favorece renta fija tradicional.",
            "ajuste_riesgo": 0.25,
            "categoria_dominante": categoria_dominante,
            "porcentaje_dominante": porcentaje_dominante,
        }

    return {
        "senal": "neutral",
        "mensaje": "El mercado FCI no muestra una señal dominante.",
        "ajuste_riesgo": 0,
        "categoria_dominante": categoria_dominante,
        "porcentaje_dominante": porcentaje_dominante,
    }
