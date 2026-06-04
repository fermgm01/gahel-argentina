def detectar_cambio_contexto(
    riesgo_actual,
    riesgo_anterior
):

    if riesgo_actual != riesgo_anterior:
        return (
            f"El riesgo cambió de "
            f"{riesgo_anterior} a "
            f"{riesgo_actual}."
        )

    return "Sin cambios relevantes."
