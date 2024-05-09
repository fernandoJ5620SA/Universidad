from flask import Blueprint, redirect, render_template, session, flash, url_for
from functools import wraps

# Crear un blueprint
alumnos_bp = Blueprint("alumnos", __name__, template_folder="../views")


def require_alumnos(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "User_id" not in session or session.get("role") != 3:
            flash(
                "Acceso denegado: Solo administradores pueden acceder a esta sección."
            )
            return redirect(url_for("auth.register"))
        return f(*args, **kwargs)

    return decorated_function


# Definir rutas dentro del blueprint


@alumnos_bp.route("/alumnos")
@require_alumnos
def index():
    return render_template("alumnos/inicio.html")


@alumnos_bp.route("/alumnos/materias")
@require_alumnos
def index():
    return render_template("alumnos/materias.html")


@alumnos_bp.route("/alumnos/Kardex")
@require_alumnos
def index():
    return render_template("alumnos/Kardex.html")


@alumnos_bp.route("/alumnos/Horarios")
@require_alumnos
def index():
    return render_template("alumnos/Horarios.html")


@alumnos_bp.route("/alumnos/Historial")
@require_alumnos
def index():
    return render_template("alumnos/Historial.html")
