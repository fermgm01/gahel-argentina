# Agente Financiero Nivel 2

Agente automatizado para análisis financiero diario en Argentina.

## Objetivo

Generar un informe diario sobre:
- Dólar oficial, MEP, CCL y blue
- Bonos CER: TX26, TZX26/T2X
- Fondos: Champaquí Cobertura y Champaquí Ahorro Pesos
- Riesgo macro argentino
- Estrategia sugerida de cartera

## Flujo diario

1. Buscar datos de mercado
2. Calcular señales
3. Evaluar riesgo
4. Aplicar reglas de decisión
5. Generar reporte
6. Enviar resumen por Telegram, WhatsApp o email

## Archivos

- `config.json`: activos, fondos y parámetros del usuario
- `main.py`: ejecuta el agente
- `data_sources.py`: módulo para conectar APIs o cargar datos manuales
- `decision_engine.py`: reglas de decisión
- `report_generator.py`: genera el informe diario
- `example_report.txt`: ejemplo de salida
