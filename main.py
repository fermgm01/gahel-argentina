import os
import time
from datetime import datetime
from zoneinfo import ZoneInfo

from core.main import main as run_gahel_once


TIMEZONE = os.getenv("GAHEL_TIMEZONE", "America/Argentina/Buenos_Aires")
REPORT_HOUR = int(os.getenv("GAHEL_REPORT_HOUR", "9"))
REPORT_MINUTE = int(os.getenv("GAHEL_REPORT_MINUTE", "0"))
CHECK_EVERY_SECONDS = int(os.getenv("GAHEL_CHECK_EVERY_SECONDS", "60"))


def _now():
    return datetime.now(ZoneInfo(TIMEZONE))


def _today_key():
    return _now().strftime("%Y-%m-%d")


def _sent_file_path():
    return os.path.join("history", "last_cloud_report.txt")


def _already_sent_today():
    path = _sent_file_path()
    if not os.path.exists(path):
        return False
    with open(path, "r", encoding="utf-8") as file:
        last_sent = file.read().strip()
    return last_sent == _today_key()


def _mark_sent_today():
    os.makedirs("history", exist_ok=True)
    with open(_sent_file_path(), "w", encoding="utf-8") as file:
        file.write(_today_key())


def _should_run_now():
    current = _now()
    report_time = current.replace(hour=REPORT_HOUR, minute=REPORT_MINUTE, second=0, microsecond=0)
    return current >= report_time and not _already_sent_today()


def _seconds_until_next_check():
    current = _now()
    report_time_today = current.replace(hour=REPORT_HOUR, minute=REPORT_MINUTE, second=0, microsecond=0)
    if current < report_time_today:
        delta = report_time_today - current
        return max(30, min(int(delta.total_seconds()), CHECK_EVERY_SECONDS))
    return CHECK_EVERY_SECONDS


def run_cloud_worker():
    print("Gahel Argentina iniciado en modo nube 24/7.")
    print(f"Reporte programado: {REPORT_HOUR:02d}:{REPORT_MINUTE:02d} ({TIMEZONE})")

    while True:
        try:
            if _should_run_now():
                print("Ejecutando reporte diario de Gahel...")
                run_gahel_once()
                _mark_sent_today()
                print("Reporte diario ejecutado y marcado como enviado.")
            else:
                print("Esperando horario de reporte...")
        except Exception as error:
            print(f"ERROR EN WORKER GAHEL: {error}")

        time.sleep(_seconds_until_next_check())


if __name__ == "__main__":
    run_cloud_worker()
