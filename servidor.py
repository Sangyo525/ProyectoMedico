from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)

def cargar_datos():
    with open('historial_medico.json', 'r', encoding='utf-8') as archivo:
        return json.load(archivo)

@app.route('/paciente')
def obtener_paciente():
    # Ahora leemos el parámetro 'ficha' desde el enlace del QR
    id_ficha = request.args.get('ficha')
    datos = cargar_datos()
    
    # Buscamos si esa ficha existe en nuestra base de datos
    paciente = datos.get(id_ficha)
    
    if paciente:
        return render_template('ficha.html', paciente=paciente, ficha=id_ficha)
    else:
        return "<h3>Error: Código de ficha médica no registrado o inválido.</h3>", 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)