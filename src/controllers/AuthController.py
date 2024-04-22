from flask import render_template, request, redirect, url_for, flash, session
from src.database.conexcionDB import *
import hashlib


def auth_user():
        msg = ''
        if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
            email = request.form['email']
            password = request.form['password']
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            conn = connectionBD()
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute('SELECT * FROM useruni WHERE email = % s AND password = % s', (email, password_hash ))
                account = cursor.fetchone()
                if account:
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['username']
                    msg = 'Logged in successfully !'
                    return render_template('layouts/dashboard_alumnos.html', msg = msg)
                else:
                    msg = 'Incorrect email / password !'
            except Exception as e:
                 msg = "un error ocurrio: {}".format(e)
            finally:
                 cursor.close()
        return render_template('register.html', msg = msg)
    
    # @auth_bp.route('/logout')
    # def logout():
    #     session.pop('loggedin', None)
    #     session.pop('id', None)
    #     session.pop('username', None)
    #     return redirect(url_for('login'))

