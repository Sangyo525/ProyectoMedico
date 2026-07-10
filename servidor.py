from flask import Flask, render_template, request
import json
import os

# Configuramos las rutas de forma absoluta
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

DB_FILE = os.path.join(base_dir, "historial_medico.json")

def cargar_datos():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

@app.route('/paciente')
def ver_paciente():
    cedula = request.args.get('cedula')
    
    if not cedula:
        return "Falta el número de cédula en la petición.", 400
        
    datos = cargar_datos()
    paciente = datos.get(cedula)
    
    if not paciente:
        return "<h1>Error: Paciente no encontrado en el sistema.</h1>", 404
        
    return render_template('ficha.html', cedula=cedula, paciente=paciente)

if __name__ == '__main__':
    # Lee el puerto que asigne el servidor de internet o usa el 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)