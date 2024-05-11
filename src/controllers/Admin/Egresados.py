from src.database.conexcionDB import *


def egresados():
    conexion_MySQLdb = connectionBD()  # Hago instancia a mi conexion desde la funcion
    mycursor = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = (
        "SELECT * FROM uni_egresados;")

    mycursor.execute(querySQL)
    egresado = mycursor.fetchall()  # fetchall () Obtener todos los registros

    mycursor.close()  # cerrrando conexion SQL
    conexion_MySQLdb.close()  # cerrando conexion de la BD

    return egresado
