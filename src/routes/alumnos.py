from flask import Blueprint, render_template
import src.controllers.alumnos.MateriasController

# Crear un blueprint
alumnos_bp = Blueprint("alumnos", __name__, template_folder="../views")


# Definir rutas dentro del blueprint

@alumnos_bp.route("/alumnos")
def index():
    materias = src.controllers.alumnos.MateriasController.obtener_materias()
    return render_template("alumnos/inicio.html", materia = materias)
    
@alumnos_bp.route("/alumnos/materias")
def materias():
    return render_template("alumnos/materias.html")

@alumnos_bp.route("/alumnos/Kardex")
def kardex():
    return render_template("alumnos/Kardex.html")

@alumnos_bp.route("/alumnos/Horarios")
def horarios():
    return render_template("alumnos/Horarios.html")

@alumnos_bp.route("/alumnos/Historial")
def historial():
    return render_template("alumnos/Historial.html")    
