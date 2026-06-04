import subprocess
import time

from core.logger import registrar_log


def run_forever(interval_seconds=3600):
    while True:
        try:
            registrar_log("Watchdog ejecutando Gahel.")
            subprocess.run(["python", "-m", "core.main"], check=False)
        except Exception as error:
            registrar_log(f"Watchdog detectó error: {error}")
        time.sleep(interval_seconds)


if __name__ == "__main__":
    run_forever()
