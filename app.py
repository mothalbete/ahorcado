from flask import Flask, render_template, jsonify
import sqlite3
import random
import unicodedata

app = Flask(__name__)

def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def obtener_cancion_aleatoria():
    conn = sqlite3.connect("canciones.db")
    c = conn.cursor()

    c.execute("""
        SELECT id, letra_cancion, titulo, artista, idioma
        FROM canciones
        WHERE letra_cancion IS NOT NULL
          AND titulo IS NOT NULL
          AND artista IS NOT NULL
          AND idioma IS NOT NULL
    """)

    filas = c.fetchall()
    conn.close()

    if not filas:
        return None

    return random.choice(filas)



@app.route("/")
def index():
    return render_template("game.html")

@app.route("/cancion")
def cancion():
    fila = obtener_cancion_aleatoria()
    if not fila:
        return jsonify({"error": "No hay canciones en la base de datos"}), 404

    id, letra, titulo, artista, idioma = fila

    return {
        "letra_original": letra,
        "letra_norm": normalizar(letra),
        "titulo_original": titulo,
        "titulo_norm": normalizar(titulo),
        "artista_original": artista,
        "artista_norm": normalizar(artista),
        "idioma": idioma
    }


# 🔥 ESTE BLOQUE ES IMPRESCINDIBLE
if __name__ == "__main__":
    app.run(debug=True)
