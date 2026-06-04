import os
import requests

from core.config_loader import load_environment


def _get_telegram_config():
    load_environment()

    token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "").strip()
    allowed = os.getenv("TELEGRAM_ALLOWED_CHAT_IDS", "").strip()
    send_enabled = os.getenv("SEND_TELEGRAM", "true").lower().strip()

    return token, chat_id, allowed, send_enabled


def enviar_mensaje(mensaje):
    token, chat_id, allowed, send_enabled = _get_telegram_config()

    if send_enabled in ("false", "0", "no"):
        print("Telegram desactivado por SEND_TELEGRAM=false")
        return False

    if not token:
        print("Telegram no enviado: falta TELEGRAM_BOT_TOKEN en .env")
        return False

    if not chat_id:
        print("Telegram no enviado: falta TELEGRAM_CHAT_ID en .env")
        return False

    if allowed:
        allowed_ids = [x.strip() for x in allowed.split(",") if x.strip()]
        if chat_id not in allowed_ids:
            print("Telegram no enviado: TELEGRAM_CHAT_ID no está autorizado.")
            return False

    url = f"https://api.telegram.org/bot{token}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": mensaje
    }

    try:
        response = requests.post(url, data=payload, timeout=20)

        if response.status_code == 200:
            print("Telegram enviado correctamente.")
            return True

        print(f"Telegram no enviado: {response.status_code} - {response.text}")
        return False

    except Exception as error:
        print(f"Telegram no enviado por error: {error}")
        return False
