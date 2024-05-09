from flask import Blueprint, redirect, render_template, session, flash, url_for
from functools import wraps

import src.controllers.Profesor
import src.controllers.Profesor.DatosProfesorController


# Crear un blueprint
profesor_bp = Blueprint("profesor", __name__, template_folder="../views")


def require_profesor(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "User_id" not in session or session.get("role") != 2:
            flash(
                "Acceso denegado: Solo administradores pueden acceder a esta sección."
            )
            return redirect(url_for("auth.register"))
        return f(*args, **kwargs)

    return decorated_function


# Definir rutas dentro del blueprint


@profesor_bp.route("/profesores")
@require_profesor
def index():
    return render_template("Profesor/profesor.html")
