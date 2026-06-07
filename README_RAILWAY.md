# Deploy Railway — Gahel Argentina v1.9

## Comando de inicio
python main.py

## Funcionamiento
Gahel queda activo 24/7 en Railway y envía un solo reporte diario a las 09:00 AM de Argentina.

## Variables obligatorias en Railway
TELEGRAM_BOT_TOKEN
TELEGRAM_CHAT_ID
TELEGRAM_ALLOWED_CHAT_IDS
SEND_TELEGRAM=true
GAHEL_ENV=production
GAHEL_DEBUG=false

## Variables de horario
GAHEL_TIMEZONE=America/Argentina/Buenos_Aires
GAHEL_REPORT_HOUR=9
GAHEL_REPORT_MINUTE=0
GAHEL_CHECK_EVERY_SECONDS=60

## Importante
No subir .env a GitHub.
Las variables reales se cargan en Railway → Variables.
