from flask import Blueprint, render_template

import src.controllers.alumnos.MateriasController


# Crear un blueprint
alumnos_bp = Blueprint("alumnos", __name__, template_folder="../views/alumnos")


# Definir rutas dentro del blueprint

@alumnos_bp.route("/alumnos")
def alumnos():
    return render_template("alumnos/inicio.html")
    