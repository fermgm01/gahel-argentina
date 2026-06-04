from pathlib import Path
import os


def _load_dotenv_manually(env_path):
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()

        if not line or line.startswith("#") or "=" not in line:
            continue

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key and key not in os.environ:
            os.environ[key] = value


def load_environment():
    """
    Carga .env desde la raíz del proyecto, incluso si el script se ejecuta
    desde otra carpeta.
    """

    root = Path(__file__).resolve().parents[1]
    env_path = root / ".env"

    try:
        from dotenv import load_dotenv
        load_dotenv(env_path)
    except Exception:
        _load_dotenv_manually(env_path)

    return env_path


def get_env(name, default=None):
    return os.getenv(name, default)
