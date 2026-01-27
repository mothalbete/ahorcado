import sqlite3
from datetime import datetime

DB_PATH = "canciones.db"

def add_song(letra, titulo, artista, idioma):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    now = datetime.utcnow().isoformat()

    c.execute("""
        INSERT INTO canciones (letra_cancion, titulo, artista, idioma, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (letra, titulo, artista, idioma, now, now))

    conn.commit()
    conn.close()

    print(f"✔ Canción añadida: {titulo} - {artista} ({idioma})")


# ============================
# AQUÍ VAN TUS CANCIONES
# ============================

add_song(
    letra="Que no tengo un puto duro pa' salir de aquí\n"
    "Y que todos mis amigos se van a morir\n"
    "De inanición, mi generación está en quiebra\n",
    titulo="Adulta y Funcional\n",
    artista="Rakky Riper",
    idioma="español"
)

add_song(
    letra="The witchcraft, the medicine, the spells and the injections\n"
    "The harvest, the needle, protect me from evil\n"
    "The magic and the misery, madness and the mystery\n"
    "Oh what has it done to me\n"
    "Everybody scream",
    titulo="Everybody Scream",
    artista="Florence + The Machine",
    idioma="inglés"
)

add_song(
    letra="Yo ya me pensaba que me andabas ghosteando\n" 
    "Y andabas en penal por homicidio voluntario\n" 
    "Tienes problemitas con la ley y no me importa\n" 
    "Si soy la primera que mataría a ese idiota\n",
    titulo="TU NOVIO ES SUBNORMAL",
    artista="Kalipotxo",
    idioma="español"
)

add_song(
    letra="I'm a moth, can't anyone see\n"
    "What a pretty butterfly I could have been?\n"
    "I'm a moth, can't anyone see\n"
    "What a pretty butterfly, I could have been?\n"
    "Mommy, does dad love me?\n"
    "It's hard to stay in touch, love is electric\n"
    "'Cause it hurts so much",
    titulo="I'm a Moth",
    artista="LIA LIA",
    idioma="inglés"
)

add_song(
    letra="Mor, tú que me ves, dame un lugar\n"
    "Te pinto el cielo en nubes a bordar\n"
    "Regaré las flores de este jardín\n"
    "Cuando titiles en la bóveda, yo siento\n"
    "Que aunque pase el sol\n"
    "Me faltas tú\n"
    "Me encadenas",
    titulo="El Lago del Alma",
    artista="Rojuu",
    idioma="español"
)

add_song(
    letra="Tu padre es un alcohólico, tu madre es narcisista\n"
    "Así que ponte el cinturón, mi niña, y disfruta la vista\n"
    "Que tu vida no será bonita como un cuento de hadas\n"
    "No le creas al Mickey Mouse que nomás te dice mamadas",
    titulo="QUERIDA AMALIA",
    artista="BRUSES",
    idioma="español"
)

add_song(
    letra="I'm a fucking downer when I talk with the mass\n"
    "Like, oh fuck, another left trash\n"
    "Thinking just 'cuz of her we can overthrow the upper class\n"
    "That's a fact\n"
    "Anarconnasse",
    titulo="ANARCONNASSE",
    artista="Changeline",
    idioma="inglés"
)

add_song(
    letra="When I see you again as a stranger or a friend\n"
    "I will give you a kiss from the past\n"
    "I will send you away, hoping you'll be okay\n"
    "With a piece of your heart living in mine\n"
    "I don't feel love anymore",
    titulo="A potion For Love",
    artista="AURORA",
    idioma="inglés"
)

add_song(
    letra="Puedo verte, puedo amarte\n"
    "Pero sé que sin escudo vo'a matarme\n"
    "Vo'a a matarme\n"
    "Ya no sé ni cuánta vida tengo\n"
    "Mato en la Nintendo\n"
    "Egos que no entiendo\n"
    "Y por favor",
    titulo="Voy a Morir",
    artista="Luna Ki",
    idioma="español"
)

add_song(
    letra="Arróupame arquiño vello\n"
    "Arróupame arco corado\n"
    "Reventar vellas cadeas\n"
    "Dos amores presidiarios\n"
    "Reventar vellas cadeas\n"
    "Dos amores presidiarios\n"
    "Para que queres o pelo?\n"
    "Se non o sabes peinare",
    titulo="Pano Corado",
    artista="Tanxugueiras",
    idioma="galego"
)

add_song(
    letra="Más duro que un diamante\n"
    "Échame un gapo pa' que entre mejor\n"
    "Lo intento que me lo hagan como tú pero es imposible bebé\n"
    "Madre mía madre mía con la niña\n"
    "Tú me asustas más que una película de terror\n"
    "Das miedo eres una asesina\n"
    "He tomao' penicilina pa' curar este dolor",
    titulo="Préndeme en Gasolina",
    artista="BAJOCERO X",
    idioma="español"
)

add_song(
    letra="Protect trans kids\n"
    "They are welcome in this space\n"
    "Queerness is beautiful\n"
    "No matter what they say\n"
    "Let's all groove\n"
    "But we gotta give it up for the T\n"
    "We're queer, it's undeniable\n"
    "Sexy and unstoppable",
    titulo="Don't Forget the T",
    artista="Josh Tenor",
    idioma="inglés"
)

add_song(
    letra="Akasaka sad\n"
    "'Cause I'm a sucker, sucker, so I suffer\n"
    "Akasaka Sawayama\n"
    "Just like my mother\n"
    "Akasaka sad\n"
    "'Cause I'm a sucker, sucker, so I suffer\n"
    "Akasaka Sawayama\n"
    "Just like my father\n"
    "Akasaka sad, I guess I'll be sad",
    titulo="Akasaka Sad",
    artista="Rina Sawayama",
    idioma="inglés"
)

add_song(
    letra="Feed us your girls, the wolves shout out\n"
    "Feed us the ones with curves, the ones without\n"
    "Feed us your girls from plate to mouth\n"
    "Honey, you're the entrée when you dress like that\n",
    titulo="Feed Us Your Girls",
    artista="Lydia the Bard",
    idioma="inglés"
)

add_song(
    letra="Y si yo te espero, ¿cuánto vas a tardar?\n"
    "¿Cuánto vas a tardar? ¿Cuánto vas a tardar?\n"
    "Esperando señales, la vida se me va\n"
    "La vida se me va, la vida se me va\n"
    "Y si robo un Tesla y me lo llevo a pasear\n"
    "Dime qué va a pasar, dime qué va a pasar\n"
    "Pero lo que disfruto es quedarme sola\n"
    "Es quedarme sola, es quedarme sola",
    titulo="Sola",
    artista="Saramalacara",
    idioma="español"
)

add_song(
    letra="And another soul is stealing your thunder\n"
    "And I know you're bringing me down\n"
    "Like a roller coaster is doing you thunder\n"
    "And I know you waiting me down\n"
    "The phone is ringing, the clock keeps ticking to let me out",
    titulo="Let Me Out",
    artista="Dover",
    idioma="inglés"
)

add_song(
    letra="Shuts up, on TikTok\n"
    "Looking at the famous girls with their followers\n"
    "Ugly crying in my bed, like 'What the fuck?\n"
    "Why do I rate myself a two when I'm five star?'",
    titulo="I Don't Like Myself",
    artista="girli",
    idioma="inglés"
)

add_song(
    letra="I didn't wanna leave you low\n"
    "Drove the car off the road\n"
    "I hope you get some time to grow\n"
    "You're not a ghost, you're in my head (Head)\n"
    "I will always love you (Love you)\n"
    "I'll love you forever (Ever)\n"
    "Even when we're not together\n"
    "I will always love you (Love you)",
    titulo="forever",
    artista="Charli XCX",
    idioma="inglés"
)

add_song(
    letra="Then I went up to the floor and made everybody scared\n"
    "I was on some kinda shit for which no one had prepared\n"
    "I was dancing in a way that made them fear for their lives\n"
    "I could only boogie down as they were pulling out their knives",
    titulo="STR333TLAMPS",
    artista="ElyOtto",
    idioma="inglés"
)

add_song(
    letra="I think that it's cute that you care\n"
    "It's alright, baby, don't waste your prayers\n"
    "I'm not in the mood for saving, I'm too busy misbehaving\n"
    "Why don't you just call me a fag?",
    titulo="Boygirl",
    artista="Pollyanna",
    idioma="inglés"
)

add_song(
    letra="I'm a parasocial anti-totalist anomaly\n"
    "I just started laughing when a nonce got a tattoo of me\n"
    "Throwing up on the internet\n"
    "Putting the noise to bed\n"
    "Thinking it's time for a rest",
    titulo="GROWING UP ON THE INTERNET",
    artista="NOAHFINNCE",
    idioma="inglés"
)

add_song(
    letra="Y él con su pelota y yo en tu habitación\n"
    "Los dos botando pero no con la misma intención\n"
    "Y tanto botar botar, me va a romper cabrón\n"
    "Cómo le explico a mi mama que no es uno son dos",
    titulo="Un Buen Tipo Para Tu Hijo",
    artista="BRÜNNE ROMEO",
    idioma="español"
)

add_song(
    letra="Soy un amante del caos\n"
    "Salgo del antro malherido\n"
    "Con el labio partido\n"
    "Y con el brazo apoyao en mi nena\n"
    "Yo nunca en creído en Dio'\n"
    "Pero cada noche le pido\n"
    "Pa que a la flaquita mía\n"
    "Nunca le falte na aunque muera",
    titulo="Mi nena",
    artista="Walls",
    idioma="español"
)

add_song(
    letra="I'm the bitch your daddy wanna die for\n"
    "You the bitch he told me was an eyesore\n"
    "Life's a game, but I still got the high score\n"
    "Now watch me do a line on the dashboard",
    titulo="Spencer Needs A Ladder",
    artista="That Kid",
    idioma="inglés"
)

add_song(
    letra="Lo mejor de trabajar es no trabajar\n"
    "El piti que me echo pa' descansar\n"
    "Yo ya he trabaja'o pa to'a mi vida\n"
    "Habiendo echa'o unas cuantas vendimias\n"
    "Me da igual tu puta empresa\n"
    "Me comes la polla con lubricante de fresa\n"
    "Y es que soy un vago, me gusta demasia'o\n"
    "Tocarme los cojones después de un Colacao",
    titulo="Trabajar? una Mierda",
    artista="Nerve Agent",
    idioma="español"
)

add_song(
    letra="Mamita mía\n"
    "No he contesta'o, llevo to' el mes sin batería\n"
    "Pesando en ti, camino solo por Gran Vía\n"
    "Estuve con más, pero no tienen tu energía\n"
    "Mamita mía (Yeah)\n"
    "Mamita mía\n"
    "Desde que no estás, tengo a otras hoes detrás mía\n"
    "Tú besando otras bocas, pero no la mía\n"
    "Y me llamas todavía, ah",
    titulo="Mamita Mía",
    artista="Alandes",
    idioma="español"
)

add_song(
    letra="Cuando miro tus historias me pongo a llorar\n"
    "Porque esas fotos que subes las hace otro man\n"
    "Porque ya no me despierto viendo tu whatsapp\n"
    "Con un enlace de perritos por el instagram",
    titulo="GUSTARLE A TU ABUELA",
    artista="pobre lucca",
    idioma="español"
)

add_song(
    letra="Kuando salimos siempre kieren pegarnos\n"
    "Igual por marikones o por andar liando\n"
    "Y eske yo pienso ke soy txabal formal\n"
    "Pero toni calienta y me pongo anormal",
    titulo="Txorigorri",
    artista="Malakias",
    idioma="¿español?"
)

add_song(
    letra="Fui pa' tu distrito, te traté bonito\n"
    "Tu cora me lo choré y no lo vo'a devolver (Oh, no)\n"
    "Ya vivo contigo, y esto es lo que siento\n"
    "No tengo motivos pa' de nuevo enloquecer\n"
    "El mundo es sombrío, tú eres mi alivio\n"
    "Tu sonrisa lo malo puede desvanecer",
    titulo="Miss Galaxia 2.2",
    artista="Mda",
    idioma="español"
)

add_song(
    letra="Sé que si me acerco vas a querer verme a solas\n"
    "Si pruebas mi boca va a saber a gominolas\n"
    "Yo te hago cosquillas, baby como Coca Cola\n"
    "Vienes a la ducha\n"
    "Quieres verme ya sin ropa",
    titulo="aventura en el crucero",
    artista="María Escarmiento",
    idioma="español"
)

add_song(
    letra="Bebemos en el porche, lo hacemos en el coche\n"
    "Y baby, es que esta noche, es noche de derroche\n"
    "Pasamos por su puerta, le rayamos el Porsche\n"
    "La disco está siniestra, estamos en la cresta",
    titulo="noch3 d3 d3rroch3",
    artista="Fran Laoren",
    idioma="español"
)

add_song(
    letra="No digas que no, que son cosas mías\n"
    "Que esta sensación es una tontería\n"
    "Porque antes me hablabas siempre que podías\n"
    "Y ahora un día bueno es que me des los buenos días\n"
    "Dime si al hablar me trabo demasiado\n"
    "Dime si mi cuarto olía mucho a cerrado\n"
    "Dime si se te hizo raro cuando nos besamos\n"
    "Vale, puede que esto último lo haya soñado",
    titulo="Las Chicas Me Ignoran",
    artista="Vau Boy",
    idioma="español"
)

add_song(
    letra="Un alien en mi terraza\n"
    "Me estaba dando la brasa, me dijo:\n"
    "'La vida terrestre te tiene ataca'\"\n"
    "'La fibra óptica ya no te va'\n"
    "Superficie granulada\n"
    "Qué grima me da\n"
    "Un cráter, un mechero\n"
    "Saturno tiene gas",
    titulo="Universo",
    artista="Las Bistecs",
    idioma="español"
)

add_song(
    letra="This system has to come\n"
    "With way better shit than racism\n"
    "Hatism or Hate Islam\n"
    "Better check up on the baptism\n"
    "If you don't give a fuck that's skepticism\n"
    "If you do give a shit that's whack to some\n"
    "If you got a brain let's practice em\n"
    "Is it tic for tac\n"
    "Getting back at em",
    titulo="Talk",
    artista="M.I.A.",
    idioma="inglés"
)
# Y así todas las que quieras...
