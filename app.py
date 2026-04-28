from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite que el HTML pueda leer los datos

@app.route('/datos')
def datos():
    # Por ahora devuelve datos de prueba
    # Cuando autoricen Azure, aquí conectamos SharePoint real
    return jsonify([
        {
            "ID": 1,
            "Fecha": "2026-04-27",
            "Hora de inicio": "2026-04-27T07:00:00",
            "Hora final": "2026-04-27T08:30:00",
            "Proyecto": "Gondola Mill",
            "Ensamble": "Stub Sill",
            "Nave": "Nave 1",
            "Lote": "R42455",
            "Tema": "Liberacion",
            "Motivo del tema": "Normal",
            "Comentario": "1",
            "Pieza ID": "PIEZA-0001"
        }
    ])

@app.route('/')
def index():
    return "Backend Concarril funcionando ✅"

if __name__ == '__main__':
    app.run()
