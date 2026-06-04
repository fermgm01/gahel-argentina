from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
LOG_DIR = ROOT_DIR / "logs"
LOG_FILE = LOG_DIR / "agent_logs.txt"


def registrar_log(mensaje):
    LOG_DIR.mkdir(exist_ok=True)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{fecha}] {mensaje}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as archivo:
        archivo.write(linea)
