from flask import Blueprint, render_template

import src.controllers.Profesor
import src.controllers.Profesor.DatosProfesorController


# Crear un blueprint
profesor_bp = Blueprint("profesor", __name__, template_folder="../views")


# Definir rutas dentro del blueprint

@profesor_bp.route("/profesores")
def Inicio():
    return render_template("Profesor/profesor.html")

@profesor_bp.route("/2")
def V2():
    return render_template("Profesor/Vista2.html")
    
@profesor_bp.route("/3")
def V3():
    return render_template("Profesor/Vista3.html")
    
@profesor_bp.route("/4")
def V4():
    return render_template("Profesor/Vista4.html")
    
@profesor_bp.route("/5")
def V5():
    return render_template("Profesor/Vista5.html")
    


