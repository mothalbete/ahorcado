import sqlite3

conn = sqlite3.connect("citas.db")
c = conn.cursor()

c.execute("""
CREATE TABLE citas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cita TEXT NOT NULL,
    autor TEXT NOT NULL,
    año INTEGER,
    idioma TEXT DEFAULT 'desconocido',
    video_url TEXT,              -- ← nueva columna para el vídeo
    created_at TEXT,
    updated_at TEXT
);
""")

conn.commit()
conn.close()

print("✔ Base de datos creada correctamente para citas con columna video_url.")
