from flask import Flask, render_template, jsonify, send_from_directory
import sqlite3
import random
import unicodedata
import os

app = Flask(__name__)

DB_PATH = "citas.db"

# === SISTEMA DE CITAS SIN REPETICIÓN ===
citas_disponibles = []


def normalizar(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


def cargar_citas_desde_bd():
    """Carga todas las citas válidas desde la base de datos."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        SELECT id, cita, autor, año, idioma, video_url
        FROM citas
        WHERE cita IS NOT NULL
          AND autor IS NOT NULL
          AND idioma IS NOT NULL
    """)

    filas = c.fetchall()
    conn.close()
    return filas


def obtener_cita_aleatoria():
    """
    Devuelve una cita aleatoria sin repetir.
    Cuando se agotan todas, recarga el pool.
    """
    global citas_disponibles

    # Si no hay citas cargadas o ya se usaron todas, recargar
    if not citas_disponibles:
        citas_disponibles = cargar_citas_desde_bd()

        if not citas_disponibles:
            return None

    # Elegir una cita aleatoria del pool
    fila = random.choice(citas_disponibles)

    # Eliminarla para evitar repeticiones
    citas_disponibles.remove(fila)

    return fila


@app.route("/")
def index():
    return render_template("game.html")


@app.route("/cita")
def cita():
    fila = obtener_cita_aleatoria()
    if not fila:
        return jsonify({"error": "No hay citas en la base de datos"}), 404

    id_, cita_txt, autor, anio, idioma, video_filename = fila
    anio_str = str(anio) if anio is not None else ""

    # Construir URL completa del vídeo
    video_url = None
    if video_filename:
        video_url = f"/videos/{video_filename}"

    return {
        "cita_original": cita_txt,
        "cita_norm": normalizar(cita_txt),
        "autor_original": autor,
        "autor_norm": normalizar(autor),
        "anio_original": anio_str,
        "anio_norm": normalizar(anio_str),
        "idioma": idioma,
        "video_url": video_url
    }


# Ruta para servir vídeos desde /uploads/videos/
@app.route("/videos/<path:filename>")
def videos(filename):
    return send_from_directory(os.path.join(app.root_path, "uploads/videos"), filename)


if __name__ == "__main__":
    app.run(debug=True)
