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
        "Hora de inicio": "2026-04-28T06:10:00",
        "Hora final": "2026-04-28T06:28:00",
        "Proyecto": "Gondola Mill",
        "Ensamble": "Stub Sill",
        "Nave": "Nave 1",
        "Lote": "R42455",
        "Tema": "Paro",
        "Motivo del tema": "SEGURIDAD",
        "Comentario": "Platica de 5 minutos",
        "Pieza ID": "79216f5b-5810-4930-88ef-9a03aea2eefb"
    },
    {
        "ID": 2,
        "Fecha": "2026-04-28",
        "Hora de inicio": "2026-04-28T06:43:00",
        "Hora final": "2026-04-28T08:28:00",
        "Proyecto": "FlatCar",
        "Ensamble": "Bolster",
        "Nave": "Nave 1",
        "Lote": "R42420",
        "Tema": "Liberacion",
        "Motivo del tema": "Normal",
        "Comentario": "0.5",
        "Pieza ID": "0ebe89e9-72eb-46af-9635-72c90b6ac464"
    },
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
