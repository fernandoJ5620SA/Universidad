from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
    session,
    request,
    jsonify,
)
from functools import wraps

import src.controllers.admin
import src.controllers.admin.Carrera
import src.controllers.admin.Egresados
import src.controllers.admin.Users
import src.controllers.admin.kardex
import src.controllers.Profesor
import src.controllers.Profesor.DatosProfesorController
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


# Leer carrera
@admin_bp.route("/admin/carreras")
@require_admin
def carreras():
    carreras = src.controllers.admin.Carrera.usuarios()
    return render_template("admin/Carreras.html", carrera=carreras)


# Crear carrera
@admin_bp.route("/admin/carreras", methods=["POST"])
@require_admin
def crear_carrera():
    id_carrera = request.form.get("id_carrrera")
    cve_carrera = request.form.get("cve_carrera")
    nombre_carrera = request.form.get("nombre_carrera")
    duracion = request.form.get("duracion")
    requisitos_ad = request.form.get("requisitos_ad")
    creditos_gradu = request.form.get("creditos_gradu")

    src.controllers.admin.Carrera.insertar_carrera(
        id_carrera, cve_carrera, nombre_carrera, duracion, requisitos_ad, creditos_gradu
    )
    return redirect(url_for("admin.carreras"))


# Actualizar carrera
@admin_bp.route("/admin/carreras/<int:id>", methods=["GET", "POST"])
@require_admin
def editar_carrera(id):
    if request.method == "POST":
        # Obtener datos del formulario
        cve_carrera = request.form.get("cve_carrera")
        nombre_carrera = request.form.get("nombre_carrera")
        duracion = request.form.get("duracion")
        requisitos_ad = request.form.get("requisitos_ad")
        creditos_gradu = request.form.get("creditos_gradu")

        # Actualizar carrera en la base de datos
        src.controllers.admin.Carrera.actualizar_carrera(
            id, cve_carrera, nombre_carrera, duracion, requisitos_ad, creditos_gradu
        )

        return redirect(url_for("admin.carreras"))

    # Obtener datos actuales de la carrera para mostrar en el formulario
    carrera = src.controllers.admin.Carrera.obtener_carrera_por_id(id)

    if not carrera:
        return jsonify({"error": "Carrera no encontrada"}), 404

    return render_template("admin/Carreras.html", carrera=carrera)


# Eliminar carrera
@admin_bp.route("/admin/eliminar_carrera/<int:id>")
@require_admin
def eliminar_carrera(id):
    eliminar_carrera(id)
    return redirect(url_for("admin.carreras"))


@admin_bp.route("/admin/carga-academica")
@require_admin
def carga_academica():
    kardex = src.controllers.admin.kardex.kardex()
    return render_template("admin/CargasAcademicas.html", kardex=kardex)


@admin_bp.route("/admin/usuarios")
@require_admin
def usuarios():
    usuarios = src.controllers.admin.Users.usuarios()
    return render_template("admin/Usuarios.html", usuario=usuarios)


# //


@admin_bp.route("/admin/profesores")
@require_admin
def profesores():
    profesores = src.controllers.Profesor.DatosProfesorController.obtener_profesor()
    return render_template("admin/Profesores.html", profesor=profesores)


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
    egresados = src.controllers.admin.Egresados.egresados()
    return render_template("admin/Egresados.html", egresado=egresados)


# //


@admin_bp.route("/admin/setting")
@require_admin
def setting():
    return render_template("admin/Setting.html")
