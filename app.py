from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

# Configuración de conexión a MySQL (ajusta según tus datos)
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "root",
    "database": "gestor_db"
}

# Simulación de una "base de datos" de cursos para validar horarios
cursos_db = {
    "123": "MJ 8-10",
    "345": "MJ 8-10",
    "543": "WV 10-12",
    "876": "LW 2-4",
    "987": "LW 2-4"
}

def obtener_horario(codigo):
    """Simula la obtención del horario de un curso a partir de su código."""
    return cursos_db.get(codigo)

def insertar_matricula(cursos_seleccionados):
    """
    Inserta una matrícula en la tabla 'matriculados'.
    Se asume que la tabla 'matriculados' tiene un campo 'id' AUTO_INCREMENT y 
    un campo 'cursos' para guardar los códigos matriculados (puedes adaptarlo según tus necesidades).
    """
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # Ejemplo: guarda los códigos de los cursos como un string separado por comas.
        cursos_str = ",".join(cursos_seleccionados)
        query = "INSERT INTO matriculados (cursos) VALUES (%s)"
        cursor.execute(query, (cursos_str,))
        conn.commit()
        nuevo_id = cursor.lastrowid  # ID generado automáticamente
        cursor.close()
        conn.close()
        return nuevo_id
    except mysql.connector.Error as err:
        print(f"Error al insertar matrícula: {err}")
        return None

@app.route('/confirmar_matricula', methods=['POST'])
def confirmar_matricula():
    data = request.get_json()
    cursos_seleccionados = data.get("cursos_seleccionados", [])
    
    horarios = {}
    for codigo in cursos_seleccionados:
        horario = obtener_horario(codigo)
        if not horario:
            return jsonify({"error": f"No se encontró el curso con código {codigo}"}), 400
        if horario in horarios:
            return jsonify({
                "error": f"¡ERROR!<br>Los cursos {horarios[horario]} y {codigo} tienen el mismo horario: {horario}."
            }), 400
        horarios[horario] = codigo

    # Si no hay conflictos, se inserta la matrícula en la base de datos.
    nuevo_id = insertar_matricula(cursos_seleccionados)
    if nuevo_id is None:
        return jsonify({"error": "Error al registrar la matrícula."}), 500

    return jsonify({"mensaje": f"Matrícula confirmada. Su ID de matrícula es {nuevo_id}."}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
