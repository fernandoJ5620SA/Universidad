from flask import render_template, request, redirect, url_for, flash, session
from src.database.conexcionDB import connectionBD
from werkzeug.security import generate_password_hash, check_password_hash


def auth_user():
    msg = ""
    if (
        request.method == "POST"
        and "email" in request.form
        and "password" in request.form
    ):
        email = request.form["email"]
        password = request.form["password"]

        conn = connectionBD()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM useruni WHERE email = %s ", (email,))
            account = cursor.fetchone()

            if account and check_password_hash(account["password"], password):
                session["loggedin"] = True
                session["User_id"] = True
                session["email"] = account["email"]
                session["role"] = account["fk_User_Role"]

                msg = "Logged in successfully !"
                return redirect(url_for("auth.login"))
            else:
                print("Correo y contraseña incorrectos")
                return render_template(
                    "Auth/login.html", msg="Correo y contraseña incorrectos"
                )
        except Exception as e:
            #  print("A ocurrido el error desdepues antes de ingresar", e)
            msg = "A ocurrido un error: {}".format(e)
        finally:
            cursor.close()
            conn.close()
    return render_template("Auth/Login.html", msg=msg)


def salir():
    session.pop("loggedin", None)
    session.pop("User_id", None)
    session.pop("email", None)
    return redirect(url_for("Auth/login.html"))


def register_user():
    if (
        request.method == "POST"
        and "name" in request.form
        and "email" in request.form
        and "password" in request.form
        and "passwordconfirm" in request.form
    ):
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        password_confirm = request.form["passwordconfirm"]

        if password != password_confirm:
            msg = "ingrese correctamente la contraseña"
            return render_template("Auth/Register.html", msg=msg)
        # Verificar que los correos sean unicos
        conn = connectionBD()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM useruni WHERE email = %s", (email,))
        result = cursor.fetchone()

        if result:
            msg = "El correo electronico ya está en uso"
            return render_template("Auth/Register.html", msg=msg)

        password_hash = generate_password_hash(password)

        try:
            cursor = conn.cursor()

            cursor.execute("SELECT MAX(user_id) FROM useruni")
            last_user_id = cursor.fetchone()[0]

            if last_user_id is None:
                new_user_ud = 1
            else:
                new_user_ud = last_user_id + 1

            sql = "INSERT INTO useruni(User_id, name, email, password) VALUES (%s,%s, %s, %s)"
            cursor.execute(sql, (new_user_ud, name, email, password_hash))

            conn.commit()

            cursor.close()
            conn.close()
            return render_template("Auth/Login.html")
        except Exception as e:
            print("Error", e)
            conn.rollback()
