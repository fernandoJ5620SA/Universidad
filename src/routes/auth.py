from flask import Blueprint, render_template,request, redirect, url_for, session, flash
from src.database.conexcionDB import connectionBD
from werkzeug.security import generate_password_hash
from src.controllers.AuthController import auth_user, salir , register_user

# Crear un blueprint
auth_bp = Blueprint("auth", __name__, template_folder="../views")



# Definir rutas dentro del blueprint
@auth_bp.route("/login", methods=['GET',"POST"])
def login():
    if request.method == 'POST':
         return auth_user()
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    return salir()



@auth_bp.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST':
            return register_user()
    return render_template("register.html")
