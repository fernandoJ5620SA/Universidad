from src.database.conexcionDB import *


def usuarios():
    conexion_MySQLdb = connectionBD()  # Hago instancia a mi conexion desde la funcion
    mycursor = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = (
        "select * from UserUni;")

    mycursor.execute(querySQL)
    usuarios = mycursor.fetchall()  # fetchall () Obtener todos los registros

    mycursor.close()  # cerrrando conexion SQL
    conexion_MySQLdb.close()  # cerrando conexion de la BD

    return usuarios
