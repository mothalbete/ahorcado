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
    cita="MIRA, COMO TE HAGAN PILLARLE TODO EL PUTO CARIÑO DEL MUNDO \n" 
    "A ESTA NIÑA Y LA MATEN, LE PRENDO FUEGO A LAS OFICINAS DE ATLUS, EH. ",
    autor="ALEXELCAPO",
    año="2023",
    idioma="ESPAÑOL"
)

add_cita(
    cita="PERO, LOCO, ¿ME HE ROTO EL CUELLO! ¿EL RESTO DEL JUEGO ESTOY\n " 
    "TUMBADO EN UN HOSPITAL Y SOY TETRAPLÉGICO? NOS HEMOS ROTO EL CUELLO.\n" 
    "ME HE PARTIDO LA COLUMNA.",
    autor="ALEXELCAPO",
    año="2023",
    idioma="ESPAÑOL"
)
