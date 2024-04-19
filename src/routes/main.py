from flask import Blueprint, render_template

# Crear un blueprint
main_bp = Blueprint("main", __name__, template_folder="../templates")


# Definir rutas dentro del blueprint
@main_bp.route("/")
def index():
    return render_template("index.html")
