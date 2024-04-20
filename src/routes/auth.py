from flask import Blueprint, render_template,request, redirect, url_for, session
from src.database.conexcionDB import connectionBD
import hashlib


import src.controllers.AuthController

# Crear un blueprint
auth_bp = Blueprint("auth", __name__, template_folder="../views")


def conexionBD():
    mydb = connectionBD()

# Definir rutas dentro del blueprint
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    src.controllers.AuthController.auth_user()
    return render_template("login.html")


@auth_bp.route("/register", methods = ['GET', 'POST'])
def register():
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'password' in request.form and 'passwordconfirm' in request.form:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        password_confirm = request.form['passwordconfirm']

        if password != password_confirm:
            msg = 'ingrese correctamente la contraseña'
            return render_template('login.html', msg=msg)

        conn = connectionBD()

        try:
            cursor = conn.cursor()

            cursor.execute("SELECT MAX(user_id) FROM useruni")
            last_user_id = cursor.fetchone()[0]

            new_user_ud = last_user_id + 1

            sql = 'INSERT INTO useruni(User_id, name, email, password) VALUES (%s,%s, %s, %s)'
            cursor.execute(sql, (new_user_ud,name, email, password_hash))

            conn.commit()

            cursor.close()
            conn.close()
            return render_template('login.html')
        except Exception as e:
                print('Error', e)
                conn.rollback()

        # return f'Usuario registrado: {nombre}, {correo}, {password_hash}'
    return render_template("register.html")
