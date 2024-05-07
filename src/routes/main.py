from flask import Blueprint, render_template

import src.controllers.alumnos.MateriasController


# Crear un blueprint
main_bp = Blueprint("main", __name__, template_folder="../views")


# Definir rutas dentro del blueprint

@main_bp.route("/")
def index():
    return render_template("login.html")
#layouts/dashboard_alumnos.html
    
@main_bp.route("/index")
def alumnos_materias():
    materias_alumn = src.controllers.alumnos.MateriasController.obtener_materias()
    return render_template("alumnos/materias_test.html", materias=materias_alumn)


@main_bp.route('/home', methods=['POST'])
def header():
    return render_template('header.html')



