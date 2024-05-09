from flask import Blueprint, render_template

import src.controllers.Profesor
import src.controllers.Profesor.DatosProfesorController


# Crear un blueprint
profesor_bp = Blueprint("profesor", __name__, template_folder="../views")


# Definir rutas dentro del blueprint

@profesor_bp.route("/profesores")
def index():
    return render_template("layouts/dashboard_profesor.html")
    



