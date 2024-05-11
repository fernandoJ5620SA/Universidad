from flask import Blueprint, render_template

import src.controllers.Admin
import src.controllers.Admin.Carrera
import src.controllers.Admin.Egresados
import src.controllers.Admin.Users
import src.controllers.Admin.kardex
import src.controllers.Profesor
import src.controllers.Profesor.DatosProfesorController
import src.controllers.alumnos.MateriasController


# Crear un blueprint
admin_bp = Blueprint("admin", __name__, template_folder="../views/admin")


# Definir rutas dentro del blueprint

@admin_bp.route('/admin')
def admin_inicio():
    return render_template("/admin/inicio.html")

@admin_bp.route("/admin/carreras")
def carreras():
    carreras = src.controllers.Admin.Carrera.usuarios()
    return render_template("admin/Carreras.html", carrera = carreras)
    
@admin_bp.route("/admin/carga-academica")
def carga_academica():
    kardex = src.controllers.Admin.kardex.kardex()
    return render_template("admin/CargasAcademicas.html", kardex = kardex)

@admin_bp.route("/admin/usuarios")
def usuarios():
    usuarios = src.controllers.Admin.Users.usuarios()
    return render_template("admin/Usuarios.html", usuario = usuarios)
    
# //

@admin_bp.route("/admin/profesores")
def profesores():
    profesores = src.controllers.Profesor.DatosProfesorController.obtener_profesor()
    return render_template("admin/Profesores.html", profesor = profesores )

@admin_bp.route("/admin/plazas")
def plazas():
    return render_template("admin/Plazas.html")
    

# //

@admin_bp.route("/admin/alumnos-en-curso")
def alumnos_en_curso():
    return render_template("admin/EnCurso.html")
    

@admin_bp.route("/admin/alumnos-agresados")
def alumnos_egresados():
    egresados = src.controllers.Admin.Egresados.egresados()
    return render_template("admin/Egresados.html", egresado = egresados)
    
# //

@admin_bp.route("/admin/setting")
def setting():
    return render_template("admin/Setting.html")
    