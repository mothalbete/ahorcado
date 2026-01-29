import sqlite3
from datetime import datetime

DB_PATH = "citas.db"

def add_cita(cita, autor, año, idioma, video_url=None):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    now = datetime.utcnow().isoformat()

    c.execute("""
        INSERT INTO citas (cita, autor, año, idioma, video_url, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (cita, autor, año, idioma, video_url, now, now))

    conn.commit()
    conn.close()

    print(f"✔ Cita añadida: \"{cita[:40]}...\" - {autor} ({idioma})")


# ============================
# EJEMPLO DE CITA CON VÍDEO
# ============================

add_cita(
    cita="MIRA, COMO TE HAGAN PILLARLE TODO EL PUTO CARIÑO DEL MUNDO\n"
         "A ESTA NIÑA Y LA MATEN, LE PRENDO FUEGO A LAS OFICINAS DE ATLUS, EH.",
    autor="ALEXELCAPO",
    año="2023",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/
)


add_cita(
    cita="PERO, LOCO, ¿ME HE ROTO EL CUELLO! ¿EL RESTO DEL JUEGO ESTOY\n"
         "TUMBADO EN UN HOSPITAL Y SOY TETRAPLÉGICO? NOS HEMOS ROTO EL CUELLO.\n"
         "ME HE PARTIDO LA COLUMNA.",
    autor="ALEXELCAPO",
    año="2023",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="ES UN BUEN JUEGO, PERO SE JUNTA QUE ES UN BUEN JUEGO\n"
         "Y QUE MUCHA GENTE NO HA JUGADO NADA MÁS EN TODO EL AÑO, ¿VALE?",
    autor="ALEXELCAPO",
    año="2025",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="NO, ES UN COSPLAYER. GOOFY, HERMANO, HEMOS VISTO SOLO A\n"
         "PERSONAS CON LA PUTA BATA ESTA DE LOS COJONES. SON TODOS DEL MISMO\n"
         "Y TU: 'SERÁ ESTE... ¿ESTE SERÁ UNO DE ESOS?' NO, VIENE DE LA COMICON\n"
         "ME CAGO EN GOOFY, TE LO JURO, EH",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="EL PAVO CONTÁNDONOS TODO EL PUTO LORE Y GOOFY: NI PUTA IDEA\n"
         "YO SOY GOOFY.",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="— ¡NOS MATARÁN A TODOS!\n"
         "— Y CON RAZÓN. Y MERECIDO VA A SER",
    autor="ALEXELCAPO",
    año="2024",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="MIRA, YO SOY EL PADRE DE MULAN Y MI HIJA [...] VUELVE CON UN\n"
         "ADOLESCENTE, UN PATO Y LO QUE SEA QUE SEA GOOFY... YO LA ECHO DE\n"
         "CASA... Y LA MATO. POR SI ACASO",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="¡OH, NO! VA A DESTRUIR ESE PNG. CUIDADO. VIVE GENTE AHÍ",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="DONALD ES CONSCIENTE DE QUE EN CHINA EL PATO PEKÍN Y DEMÁS\n"
         "SE LO PUTO REVIENTAN, ¿NO? QUIERO DECIR: ¿ES CONSCIENTE DE LA\n"
         "COCINA ASIÁTICA EN GENERAL? ¿ALGUIEN LE HA INFORMADO?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="VAYA. 'NO TE TIENES QUE BASAR EN LAS APARIENCIAS. REALMENTE\n"
         "NO DOY TODO EL PUTO ASCO. SOY CANÓNICAMENTE PRECIOSA' POR LO TANTO EL\n"
         "MENSAJE SE PIERDE, PORQUE EL AUTÉNTICO MENSAJE SERÍA: 'SOY ASÍ' Y YA ESTÁ\n"
         " [...]¿LO ENTENDÉIS, NIÑOS? ¿LO QUE ES SER CANÓNICAMENTE ATRACTIVO?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="CHICO, ¿HAS ESTADO EN INTERNET... 10 SEGUNDOS? ¿TU SABES LA CANTIDAD\n"
         "DE PUTÍSIMOS FURROS QUE HAY EN INTERNET? ¿TU SABES LO QUE PAGA LA GENTE\n"
         "POR UN FURSUIT Y COMO SE CAGAN DENTRO DE ESOS TRAJES Y AUN ASÍ FOLLAN?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="¿PUEDO HACER QUE NO NAZCÁIS Y NO ME TRAICIONÉIS? ¿VAMOS TODOS JUNTOS\n"
         "A VER LA TRAICIÓN QUE ME HICISTÉIS EN EL PRIMER KINGDOM HEARTS? ¿LA VEMOS\n"
         "TODOS JUNTOS COMO UNA FAMILIA?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="¿DEBERÍA HABER LEÍDO LO QUE PONÍA?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="¡QUE DEJES DE METERTE EN EL AGUA CON LAS BOTAS! NO SOPORTO\n"
         "A NADIE. ¡NADIE! NO PUEDO CON ESTA GENTE",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="ESTE VA A SER EL JUEGO MÁS LARGO DE LA HISTORIA EN EL\n"
         "QUE UN ADOLESCENTE QUIERE FOLLAR Y SE PASA 57 HORAS INTANTÁNDOLO.",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="LA VERDAD ES QUE ES UN PERSONAJE COMPLETO, EH. SU ARCO\n"
         "DE PERSONAJE ES SER SECUESTRADA EN EL PRIMER JUEGO Y SER\n"
         "SECUESTRADA EN EL SEGUNDO JUEGO. ESPECTÁCULAR.",
    autor="ALEXELCAPO",

    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="¿SE LO EXPLICAMOS? ¿TENEMOS UNA CONVERSACIÓN CON ÉL? ROLLO:\n"
         "'VAIS A MORIR. LO ENTENDÉIS, ¿VERDAD?\n"
         "CANTAD TODO LO QUE QUERÁIS, ES INEVITABLE'",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="ME HACE GRACIA PORQUE ENTIENDO QUE AQUÍ LA COSA ES TIENES QUE\n"
         "CONSEGUIR QUE SE ENAMORE DE TI SIN HABLAR, ¿NO? PERO...\n"
         "¿URSULA SABE QUE ARIEL ES COMO... UNA MUJER SÚPER GUAPA?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="HA ROZAO EL BORDE Y EL TÍO: 'ME MUERO [...] UN PIXEL HA TOCADO\n"
         "MI ZAPATILLA MONSTRUOSAMENTE GRANDE DE PUTO CLOWN QUE LLEVO PUES\n"
         "ME TENGO QUE MORIR. ES JUSTO.'",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="HE PULSADO EL BOTÓN DE RODAR QUE ES EL MISMO QUE EL DE BLOQUEAR\n" \
    "PERO SI TE MUEVES UN PUTO PIXEL SORA DICE: 'ME TIRO DE CABEZA\n" \
    "Y QUE ME MATE, COÑO'",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="¿OS DAIS CUENTA QUE OS ESTOY GRITANDO 'AUXILIO' CON TODAS LAS\n"
         "DECISIONES QUE TOMO?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="HOMBRE, UNA GRAN EXPLOSIÓN, UNA ROCA, TU PEGÁNDOLE CON LA ESPADA\n"
         "UN TÍO MUY GORDO...",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="O SEA, HA SIDO DOS VECES TAPTADA, QUE ESO ES\n"
         "COMO UNA ALUNACIÓN DEL RAPTO, O SEA: YA NO\n"
         "ESTÁ RAPTADA, ¿NO?",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="Y AHORA EL TÍO SALE, CON TODA SU POLLA DE RATA\n"
         "SALE DE AHÍ COMO: '¿QUÉ HA PASADO? SE ME CUIDAN'",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="REALMENTE ES COMO WORDLBUILDING, PORQUE CLARO,\n"
         "EN ESTOS MUNDOS LA PEÑA TIENE LOS PIES GIGANTES,\n"
         "LAS MANOS GRANDES Y POR LO TANTO, LOS POLOS DE ESTE MUNDO\n"
         "TIENEN MÁS PALO, PORQUE SINO NO PODRÍAN COGERLOS.",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="— KINGDOM HEARTS\n"
         "— DOS",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="SOY UN DADO. ES QUE QUE NO SÉ CÓMO EXPLICARLO\n"
         "DE OTRA MANERA. SOY UN DADO [...] ¡SOY UNA CARTA!\n"
         "¡SOY UNA CARTA AHORA!¿PUEDO SER SORA EN ALGÚN MOMENTO!",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
)

add_cita(
    cita="¡Y A TOMAR POR EL CULO! ¿QUÉ ES UN GIÓN?\n"
         "NADIE LO SABE. CUALQUIER COSA PODRÍA HABER PASADO.\n"
         "ESA ES LA EXPLICACIÓN.",
    autor="ALEXELCAPO",
    año="2022",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)

add_cita(
    cita="LO HE PENSADO LARGO Y TENDIDO Y ME GUSTARÍA QUE\n"
         "UN AVIÓN SE ESTRELLARA AHÍ. UN AVIÓN QUE POR CASUALIDAD\n"
         "LLEVA NAPALM. O SEA YO SALDRÍA A APLAUDIR.",
    autor="ALEXELCAPO",
    año="2023",
    idioma="ESPAÑOL",
    video_url=""   # ← archivo dentro de /uploads/videos/

)
