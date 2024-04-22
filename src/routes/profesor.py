from flask import Blueprint, render_template

import src.controllers.Profesor
import src.controllers.Profesor.DatosProfesorController


# Crear un blueprint
main_bp = Blueprint("main", __name__, template_folder="../views")


# Definir rutas dentro del blueprint

@main_bp.route("/")
def index():
    return render_template("layouts/dashboard_profesor.html")
    
@main_bp.route("/index")
def Datos_Profesor():
    Datos_Profesor = src.controllers.Profesor.DatosProfesorController.obtener_datosprofesor()
    return render_template("Profesor/profesor.html", Datos_Profesor=Datos_Profesor)


@main_bp.route('/home', methods=['POST'])
def header():
    return render_template('header.html')



