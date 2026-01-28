from flask import Flask, render_template, jsonify
import sqlite3
import random
import unicodedata

app = Flask(__name__)

DB_PATH = "citas.db"


def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


def obtener_cita_aleatoria():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT id, cita, autor, año, idioma
        FROM citas
        WHERE cita IS NOT NULL
          AND autor IS NOT NULL
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


@app.route("/cita")
def cita():
    fila = obtener_cita_aleatoria()
    if not fila:
        return jsonify({"error": "No hay citas en la base de datos"}), 404

    id_, cita_txt, autor, anio, idioma = fila
    anio_str = str(anio) if anio is not None else ""

    return {
        "cita_original": cita_txt,
        "cita_norm": normalizar(cita_txt),
        "autor_original": autor,
        "autor_norm": normalizar(autor),
        "anio_original": anio_str,
        "anio_norm": normalizar(anio_str),
        "idioma": idioma
    }


if __name__ == "__main__":
    app.run(debug=True)
