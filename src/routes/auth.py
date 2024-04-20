from flask import Blueprint, render_template

import src.controllers.AuthController

# Crear un blueprint
auth_bp = Blueprint("auth", __name__, template_folder="../views")


# Definir rutas dentro del blueprint
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    src.controllers.AuthController.auth_user()
    return render_template("login.html")


@auth_bp.route("/register")
def register():
    return render_template("register.html")
