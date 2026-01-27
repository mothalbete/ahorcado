import sqlite3

conn = sqlite3.connect("canciones.db")
c = conn.cursor()

c.execute("""
CREATE TABLE canciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    letra_cancion TEXT NOT NULL,
    titulo TEXT NOT NULL,
    artista TEXT NOT NULL,
    idioma TEXT DEFAULT 'desconocido',
    created_at TEXT,
    updated_at TEXT
);
""")

conn.commit()
conn.close()

print("✔ Base de datos creada correctamente con columna 'idioma'.")
