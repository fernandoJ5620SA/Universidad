from src.database.conexcionDB import *


def obtener_kardex():
    conexion_MySQLdb = connectionBD()  # Hago instancia a mi conexion desde la funcion
    mycursor = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = (
        "select * from uni_kardex;")

    mycursor.execute(querySQL)
    kardex = mycursor.fetchall()  # fetchall () Obtener todos los registros

    mycursor.close()  # cerrrando conexion SQL
    conexion_MySQLdb.close()  # cerrando conexion de la BD

    return kardex