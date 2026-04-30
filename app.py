from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='.')
CORS(app)

# 📁 Base dir (importante para Render)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 🧠 DATOS
DATOS = [
    {
        "ID": 1,
        "Fecha": "2026-04-28",
        "Hora de inicio": "2026-04-28T07:00:00",
        "Hora final": "2026-04-28T08:30:00",
        "Proyecto": "Gondola Mill",
        "Ensamble": "Stub Sill",
        "Nave": "Nave 1",
        "Lote": "R42455",
        "Tema": "Liberacion",
        "Motivo del tema": "Normal",
        "Comentario": "1",
        "Pieza ID": "PIEZA-0001"
    }
]

# 🔹 API
@app.route('/datos')
def datos():
    return jsonify(DATOS)

# 🔹 HTML principal
@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'dashboard_supervisor.html')

# 🔹 Logo (por si acaso)
@app.route('/logo.png')
def logo():
    return send_from_directory(BASE_DIR, 'logo.png')

if __name__ == '__main__':
    app.run()
