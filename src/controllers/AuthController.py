from flask import render_template, request, redirect, url_for, flash, session
from src.database.conexcionDB import connectionBD
from werkzeug.security import generate_password_hash, check_password_hash
import requests

SITE_KEY = "6LclYtYpAAAAAIYCif1X8SHFqFkWpcVcp1uvf8Ud"
SECRET_KEY = "6LclYtYpAAAAAPDlmQ_LKs19Nax1z7YRpwkEj0rT"
VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"


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

            # print(request.form)

            secret_response = request.form["g-recaptcha-response"]
            verify_response = requests.post(
                url=f"{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}"
            ).json()

            print(verify_response)

            if (
                account
                and check_password_hash(account["password"], password)
                and verify_response["success"]
                and verify_response["score"] > 0.5
            ):

                session["loggedin"] = True
                session["User_id"] = True
                session["email"] = account["email"]
                session["role"] = account["fk_User_Role"]
                session["name"] = account["name"]

                def switch_case(role):
                    match role:
                        case 1:
                            return redirect(url_for("admin.admin_inicio"))
                        case 2:
                            return redirect(url_for("alumnos.alumnos"))
                        case 3:
                            return redirect(url_for("profesor.Inicio"))
                        case _:
                            return "A ocurrido un error:"

                return switch_case(
                    session["role"]
                )  # Retorna el resultado del switch_case
                # msg = "Logged in successfully !"

                # return redirect(url_for("auth.login"))
            else:
                return render_template(
                    "Auth/login.html",
                    msg="Correo y contraseña incorrectos",
                    site_key=SITE_KEY,
                )
        except Exception as e:
            #  print("A ocurrido el error desdepues antes de ingresar", e)
            msg = "A ocurrido un error: {}"  # .format(e)
        finally:
            cursor.close()
            conn.close()
    return render_template("Auth/Login.html", msg=msg, site_key=SITE_KEY)


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
            msg = "Ingrese correctamente la contraseña"
            return render_template("Auth/Register.html", msg=msg)

        # Verificar que los correos sean únicos
        conn = connectionBD()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM useruni WHERE email = %s", (email,))
        result = cursor.fetchone()

        if result:
            msg = "El correo electrónico ya está en uso"
            return render_template("Auth/Register.html", msg=msg)

        password_hash = generate_password_hash(password)

        try:
            cursor = conn.cursor()

            cursor.execute("SELECT MAX(user_id) FROM useruni")
            last_user_id = cursor.fetchone()[0]

            if last_user_id is None:
                new_user_id = 1
            else:
                new_user_id = last_user_id + 1

            sql = "INSERT INTO useruni(User_id, name, email, password, fk_User_Role) VALUES (%s, %s, %s, %s, 0)"
            cursor.execute(sql, (new_user_id, name, email, password_hash))

            conn.commit()

            cursor.close()
            conn.close()
            return redirect(
                url_for("auth.login")
            )  # Redirige al login después de un registro exitoso
        except Exception as e:
            print("Error", e)
            conn.rollback()
            msg = "Error en el registro, por favor intenta de nuevo."
            return render_template("Auth/Register.html", msg=msg)
    else:
        msg = "Por favor, completa el formulario."
        return render_template("Auth/Register.html", msg=msg)
