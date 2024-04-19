from flask import Blueprint, render_template

# Crear un blueprint
account_bp = Blueprint("account", __name__, template_folder="../templates/account")


# Definir rutas dentro del blueprint
@account_bp.route("/login")
def login():
    return render_template("login.html")

@account_bp.route('/register')
def register():
<<<<<<< HEAD
    return render_template("Register.html")
=======
    return render_template('register.html')

#que haces cedrick
# @account_bp.route("/register")
# def register():
#     return render_template("login.html")
>>>>>>> e866cb49916f90a110585ac154f0d8047c90c9e9
