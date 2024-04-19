from flask import Blueprint, render_template

# Crear un blueprint
main_bp = Blueprint('main', __name__)

# Definir rutas dentro del blueprint
@main_bp.route("/")
def home():
    return render_template("/src/template/base.html")
