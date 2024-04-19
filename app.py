# Este archivo será el punto de entrada de nuestra aplicación. Contendrá el código para ejecutar la aplicación Flask.
from flask import Flask

from src.routes.main import main_bp

# Crear una instancia de la aplicación Flask
app = Flask(__name__)


# Registrar el blueprint en la aplicación
app.register_blueprint(main_bp)


if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")

