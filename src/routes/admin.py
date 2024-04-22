from flask import Blueprint, render_template

import src.controllers.alumnos.MateriasController


# Crear un blueprint
admin_bp = Blueprint("admin", __name__, template_folder="../views/admin")


# Definir rutas dentro del blueprint

@admin_bp.route("/admin")
def index():
    return render_template("admin/inicio.html")
    