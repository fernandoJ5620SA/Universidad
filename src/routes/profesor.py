from flask import Blueprint, render_template

import src.controllers.Profesor
import src.controllers.Profesor.DatosProfesorController


# Crear un blueprint
profesor_bp = Blueprint("profesor", __name__, template_folder="../views")


# Definir rutas dentro del blueprint

@profesor_bp.route("/")
def index():
    return render_template("layouts/dashboard_profesor.html")
    
@profesor_bp.route("/index")
def Datos_Profesor():
    Datos_Profesor = src.controllers.Profesor.DatosProfesorController.obtener_datosprofesor()
    return render_template("Profesor/profesor.html", Datos_Profesor=Datos_Profesor)


@profesor_bp.route('/home', methods=['POST'])
def header():
    return render_template('header.html')



