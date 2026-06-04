def generar_allocator(contexto):
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

    return {
        "Liquidez": "35%",
        "CER": "50%",
        "Cobertura dólar": "15%",
    }
