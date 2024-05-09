from flask import Blueprint, render_template

import src.controllers.alumnos.MateriasController


# Crear un blueprint
main_bp = Blueprint("main", __name__, template_folder="../views")

# Definir rutas dentro del blueprint

@main_bp.route("/")
def index():
    return render_template("Login/Login.html")
#layouts/dashboard_alumnos.html




