from flask import Blueprint, render_template

# Crear un blueprint
main_bp = Blueprint("main", __name__, template_folder="../templates")


# Definir rutas dentro del blueprint
@main_bp.route('/')
def login():
    return render_template('Login.html')

@main_bp.route("/index")
def index():
    return render_template("index.html")

@main_bp.route('/home', methods=['POST'])
def header():
    return render_template('header.html')



