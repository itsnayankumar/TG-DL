from os import getenv
from dotenv import load_dotenv
from pathlib import Path
import socket

if Path("config.env").exists():
    load_dotenv("config.env")

def get_local_ip(port: int) -> str:
    """Dynamically detects the local Wi-Fi IP address inside Termux."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return f"http://{ip}:{port}"
    except Exception:
        return f"http://127.0.0.1:{port}"

class Telegram:
    API_ID = int(getenv("API_ID", "0"))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    PORT = int(getenv("PORT", 8080))
    SESSION_STRING = getenv("SESSION_STRING", "")
    
    # Auto-detects local IP if BASE_URL is not set in config.env
    _base_url_env = getenv("BASE_URL", "").rstrip('/')
    BASE_URL = _base_url_env if _base_url_env else get_local_ip(PORT)
    
    DATABASE_URL = getenv("DATABASE_URL", "")
    AUTH_CHANNEL = [channel.strip() for channel in getenv("AUTH_CHANNEL", "").split(",") if channel.strip()]
    THEME = getenv("THEME", "quartz").lower()
    USERNAME = getenv("USERNAME", "admin")
    PASSWORD = getenv("PASSWORD", "admin")
    ADMIN_USERNAME = getenv("ADMIN_USERNAME", "surfTG")
    ADMIN_PASSWORD = getenv("ADMIN_PASSWORD", "surfTG")
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '10'))
    MULTI_CLIENT = getenv('MULTI_CLIENT', 'False')
    HIDE_CHANNEL = getenv('HIDE_CHANNEL', 'False')