import datetime
import os
import sqlite3

DB_PATH = "/data/database.db"

# Garantir que o diretório existe
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT
    )
''')

timestamp = datetime.datetime.now().isoformat()
cursor.execute("INSERT INTO logs (timestamp) VALUES (?)", (timestamp,))
conn.commit()

print(f"Log inserido: {timestamp}")

cursor.execute("SELECT * FROM logs")
rows = cursor.fetchall()
print(f"Total de logs no banco: {len(rows)}")
for row in rows:
    print(row)

conn.close()
