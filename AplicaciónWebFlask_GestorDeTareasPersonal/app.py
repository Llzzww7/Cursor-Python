#--------aplicación web : to-do list--------

#----Configuración inicial del proyecto-----

#Creamos entorno virtual python3 -m venv venv e instalamos Flask

from flask import Flask, request, redirect, render_template

#--- Crear la estructura de datos----
#  Lista global de tareas: [{ "id": int, "texto": str, "completada": bool }, ...]
tareas = []
_next_id = 1

def agregar_tarea(texto):
    global _next_id
    tarea = {"id": _next_id, "texto": texto, "completada": False}
    tareas.append(tarea)
    _next_id += 1
    return tarea["id"]

def completar_tarea(id):
    for t in tareas:
        if t["id"] == id:
            t["completada"] = True
            return True
    return False

app = Flask(__name__)

#Definición de la ruta principal para mostrar tareas.
@app.route('/')
def index():
    # Ordenar tareas: incompletas primero, luego completadas
    tareas_ordenadas = sorted(tareas, key=lambda t: t['completada'])
    return render_template('index.html', tareas=tareas_ordenadas)

#Ahora la ruta para agregar:
@app.route('/agregar', methods=['POST'])
def agregar():
    texto_tarea = request.form.get('texto_tarea')
    if texto_tarea:
        agregar_tarea(texto_tarea)
    return redirect('/')

#Y la ruta para marcar como completada:
@app.route('/completar/<int:id>')
def completar(id):
    completar_tarea(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)