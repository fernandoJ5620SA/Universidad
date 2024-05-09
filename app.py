# Este archivo será el punto de entrada de nuestra aplicación. Contendrá el código para ejecutar la aplicación Flask.
from flask import Flask

from src.routes.main import main_bp
from src.routes.admin import admin_bp
from src.routes.profesor import profesor_bp
from src.routes.auth import auth_bp

# Crear una instancia de la aplicación Flask
app = Flask(__name__, static_folder="src/static")
app.secret_key = 'gil_se_la_come'

# Registrar el blueprint en la aplicación
app.register_blueprint(main_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(profesor_bp)


if __name__ == "__main__":
    app.run(debug=True, port=8081, host="0.0.0.0")
