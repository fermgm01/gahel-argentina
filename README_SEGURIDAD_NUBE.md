# Seguridad y nube — Gahel Argentina v1.6

## Antes de subir a Railway / Render

1. Copiar `.env.example` como `.env`.
2. Pegar un token nuevo de Telegram.
3. Completar `TELEGRAM_CHAT_ID`.
4. Completar `TELEGRAM_ALLOWED_CHAT_IDS`.
5. No subir `.env` a GitHub.

## Variables necesarias en la nube

- TELEGRAM_BOT_TOKEN
- TELEGRAM_CHAT_ID
- TELEGRAM_ALLOWED_CHAT_IDS
- SEND_TELEGRAM
- GAHEL_ENV

## Comando de ejecución

```bash
python -m core.main
```

## Seguridad básica incluida

- Token fuera del código.
- Chat autorizado.
- Manejo de errores en Telegram.
- Logs persistentes.
- Watchdog base.
- Fallback si falla FCI.

## No incluido por decisión actual

- CEDEARs.
- Mercado internacional.
- USA.
