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

add_cita(
    cita="ES UN BUEN JUEGO, PERO SE JUNTA QUE ES UN BUEN JUEGO\n"
    "Y QUE MUCHA GENTE NO HA JUGADO NADA MÁS EN TODO EL AÑO, ¿VALE?",
    autor="ALEXELCAPO",
    año="2025",
    idioma="ESPAÑOL"
)

add_cita(
    cita="NO, ES UN COSPLAYER. GOOFY, HERMANO, HEMOS VISTO SOLO A" \
    "PERSONAS CON LA PUTA BATA ESTA DE LOS COJONES. SON TODOS DEL MISMO" \
    "Y TU: 'SERÁ ESTE... ¿ESTE SERÁ UNO DE ESOS?' NO, VIENE DE LA COMICON" \
    "ME CAGO EN GOOFY, TE LO JURO, EH",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL"
)

add_cita(
    cita="EL PAVO CONTÁNDONOS TODO EL PUTO LORE Y GOOFY: NI PUTA IDEA" \
    "YO SOY GOOFY.",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL"
)

add_cita(
    cita="— ¡NOS MATARÁN A TODOS!" \
    "— Y CON RAZÓN. Y MERECIDO VA A SER",
    autor="ALEXELCAPO",
    año="2024",
    idioma="ESPAÑOL"
)

add_cita(
    cita="MIRA, YO SOY EL PADRE DE MULAN Y MI HIJA [...] VUELVE CON UN " \
    "ADOLESCENTE, UN PATO Y LO QUE SEA QUE SEA GOOFY... YO LA ECHO DE " \
    "CASA... Y LA MATO. POR SI ACASO",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL"
)

add_cita(
    cita="¡OH, NO! VA A DESTRUIR ESE PNG. CUIDADO. VIVE GENTE AHÍ",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL"
)

add_cita(
    cita="DONALD ES CONSCIENTE DE QUE EN CHINA EL PATO PEKÍN Y DEMÁS" \
    "SE LO PUTO REVIENTAN, ¿NO? QUIERO DECIR: ¿ES CONSCIENTE DE LA"\
    "COCINA ASIÁTICA EN GENERAL? ¿ALGUIEN LE HA INFORMADO?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL"
)

add_cita(
    cita="VAYA. 'NO TE TIENES QUE BASAR EN LAS APARIENCIAS. REALMENTE" \
    "NO DOY TODO EL PUTO ASCO. SOY CANÓNICAMENTE PRECIOSA' POR LOTANTO" \
    "MENSAJE SE PIERDE, PORQUE EL AUTÉNTICO MENSAJE SERÍA: SOY ASÍ Y YA ESTÁ" \
    " [...]¿LO ENTENDÉIS, NIÑOS? ¿LO QUE ES SER CANÓNICAMENTE ATRACTIVO?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL"
)

add_cita(
    cita="CHICO, ¿HAS ESTADO EN INTERNET... 10 SEGUNDOS? ¿TU SABES LA CANTIDAD" \
    "DE PUTÍSIMOS FURROS QUE HAY EN INTERNET? ¿TU SABES LO QUE PAGA LA GENTE"\
    "POR UN FURSUIT Y COMO SE CAGAN DENTRO DE ESOS TRAJES Y AUN ASÍ FOLLAN?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL"
)

add_cita(
    cita="CHICO, ¿HAS ESTADO EN INTERNET... 10 SEGUNDOS? ¿TU SABES LA CANTIDAD" \
    "DE PUTÍSIMOS FURROS QUE HAY EN INTERNET? ¿TU SABES LO QUE PAGA LA GENTE"\
    "POR UN FURSUIT Y COMO SE CAGAN DENTRO DE ESOS TRAJES Y AUN ASÍ FOLLAN?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL"
)