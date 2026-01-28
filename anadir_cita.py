import sqlite3
from datetime import datetime

DB_PATH = "citas.db"

def add_cita(cita, autor, año, idioma):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    now = datetime.utcnow().isoformat()

    c.execute("""
        INSERT INTO citas (cita, autor, año, idioma, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (cita, autor, año, idioma, now, now))

    conn.commit()
    conn.close()

    print(f"✔ Cita añadida: \"{cita[:40]}...\" - {autor} ({idioma})")


# ============================
# AQUÍ VAN TUS CITAS
# ============================

add_cita(
    cita="MI BURRITO SABANERO",
    autor="LUA",
    año="2025",
    idioma="ESPAÑOL"
)
