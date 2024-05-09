from flask import Blueprint, redirect, render_template, session, flash, url_for
from functools import wraps

import src.controllers.alumnos.MateriasController


# Crear un blueprint
admin_bp = Blueprint("admin", __name__, template_folder="../views/admin")


def require_admin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "User_id" not in session or session.get("role") != 1:
            flash(
                "Acceso denegado: Solo administradores pueden acceder a esta sección."
            )
            return redirect(url_for("auth.register"))
        return f(*args, **kwargs)

    return decorated_function


# Definir rutas dentro del blueprint


@admin_bp.route("/admin")
@require_admin
def admin_inicio():
    return render_template("/admin/inicio.html")


@admin_bp.route("/admin/carreras")
@require_admin
def carreras():
    return render_template("admin/Carreras.html")


@admin_bp.route("/admin/carga-academica")
@require_admin
def carga_academica():
    return render_template("admin/CargasAcademicas.html")


@admin_bp.route("/admin/usuarios")
@require_admin
def usuarios():
    return render_template("admin/Usuarios.html")


# //


@admin_bp.route("/admin/profesores")
@require_admin
def profesores():
    return render_template("admin/Profesores.html")


@admin_bp.route("/admin/plazas")
@require_admin
def plazas():
    return render_template("admin/Plazas.html")


# //


@admin_bp.route("/admin/alumnos-en-curso")
@require_admin
def alumnos_en_curso():
    return render_template("admin/EnCurso.html")


@admin_bp.route("/admin/alumnos-agresados")
@require_admin
def alumnos_egresados():
    return render_template("admin/Egresados.html")


# //


@admin_bp.route("/admin/setting")
@require_admin
def setting():
    return render_template("admin/Setting.html")
