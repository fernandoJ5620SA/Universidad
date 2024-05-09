from flask import Blueprint, render_template

# Crear un blueprint
alumnos_bp = Blueprint("alumnos", __name__, template_folder="../views")


# Definir rutas dentro del blueprint

@alumnos_bp.route("/alumnos")
def alumnos():
    return render_template("alumnos/inicio.html")
    
@alumnos_bp.route("/alumnos/materias")
def alumnos_materias():
    return render_template("alumnos/materias.html")

@alumnos_bp.route("/alumnos/Kardex")
def alumnos_kardex():
    return render_template("alumnos/Kardex.html")

@alumnos_bp.route("/alumnos/Horarios")
def alumnos_horarios():
    return render_template("alumnos/Horarios.html")

@alumnos_bp.route("/alumnos/Historial")
def alumnos_historial():
    return render_template("alumnos/Historial.html")    
