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
<<<<<<< HEAD
@require_alumnos
def index():
=======
def alumnos():
>>>>>>> e7979d716bd78b700149e55738a75399f37fe10f
    return render_template("alumnos/inicio.html")


@alumnos_bp.route("/alumnos/materias")
<<<<<<< HEAD
@require_alumnos
def index():
=======
def alumnos_materias():
>>>>>>> e7979d716bd78b700149e55738a75399f37fe10f
    return render_template("alumnos/materias.html")


@alumnos_bp.route("/alumnos/Kardex")
<<<<<<< HEAD
@require_alumnos
def index():
=======
def alumnos_kardex():
>>>>>>> e7979d716bd78b700149e55738a75399f37fe10f
    return render_template("alumnos/Kardex.html")


@alumnos_bp.route("/alumnos/Horarios")
<<<<<<< HEAD
@require_alumnos
def index():
=======
def alumnos_horarios():
>>>>>>> e7979d716bd78b700149e55738a75399f37fe10f
    return render_template("alumnos/Horarios.html")


@alumnos_bp.route("/alumnos/Historial")
<<<<<<< HEAD
@require_alumnos
def index():
    return render_template("alumnos/Historial.html")
=======
def alumnos_historial():
    return render_template("alumnos/Historial.html")    
>>>>>>> e7979d716bd78b700149e55738a75399f37fe10f
