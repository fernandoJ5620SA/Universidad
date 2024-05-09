from flask import Blueprint, render_template

import src.controllers.alumnos.MateriasController


# Crear un blueprint
admin_bp = Blueprint("admin", __name__, template_folder="../views/admin")


# Definir rutas dentro del blueprint

@admin_bp.route('/admin')
def admin_inicio():
    return render_template("/admin/inicio.html")

@admin_bp.route("/admin/carreras")
def carreras():
    return render_template("admin/Carreras.html")
    
@admin_bp.route("/admin/carga-academica")
def carga_academica():
    return render_template("admin/CargasAcademicas.html")

@admin_bp.route("/admin/usuarios")
def usuarios():
    return render_template("admin/Usuarios.html")
    
# //

@admin_bp.route("/admin/profesores")
def profesores():
    return render_template("admin/Profesores.html")

@admin_bp.route("/admin/plazas")
def plazas():
    return render_template("admin/Plazas.html")
    

# //

@admin_bp.route("/admin/alumnos-en-curso")
def alumnos_en_curso():
    return render_template("admin/EnCurso.html")
    

@admin_bp.route("/admin/alumnos-agresados")
def alumnos_egresados():
    return render_template("admin/Egresados.html")
    
# //

@admin_bp.route("/admin/setting")
def setting():
    return render_template("admin/Setting.html")
    