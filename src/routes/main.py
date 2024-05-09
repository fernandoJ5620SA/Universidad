from flask import Blueprint, render_template

import src.controllers.alumnos.MateriasController


# Crear un blueprint
main_bp = Blueprint("main", __name__, template_folder="../views")

# Definir rutas dentro del blueprint

@main_bp.route('/home', methods=['POST'])
def header():
    return render_template('header.html')



