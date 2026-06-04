from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
HISTORY_DIR = ROOT_DIR / "history"
HISTORY_FILE = HISTORY_DIR / "historial_reportes.txt"


def save_report(report):
    HISTORY_DIR.mkdir(exist_ok=True)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(f"\n--- REPORTE {fecha} ---\n")
        file.write(report)
        file.write("\n")


def load_last_report():
    if not HISTORY_FILE.exists():
        return None

    contenido = HISTORY_FILE.read_text(encoding="utf-8")
    partes = [p.strip() for p in contenido.split("--- REPORTE ") if p.strip()]
    if not partes:
        return None
    return partes[-1]
