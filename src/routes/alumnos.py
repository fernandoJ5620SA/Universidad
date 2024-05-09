from flask import Blueprint, render_template

# Crear un blueprint
alumnos_bp = Blueprint("alumnos", __name__, template_folder="../views")


# Definir rutas dentro del blueprint

@alumnos_bp.route("/alumnos")
def index():
    return render_template("alumnos/inicio.html")
    
@alumnos_bp.route("/alumnos/materias")
def index():
    return render_template("alumnos/materias.html")

@alumnos_bp.route("/alumnos/Kardex")
def index():
    return render_template("alumnos/Kardex.html")

@alumnos_bp.route("/alumnos/Horarios")
def index():
    return render_template("alumnos/Horarios.html")

@alumnos_bp.route("/alumnos/Historial")
def index():
    return render_template("alumnos/Historial.html")    
