from src.database.conexcionDB import *

def Bitacora_Ad():
    conexion_MySQLdb = connectionBD()  # Hago instancia a mi conexion desde la funcion
    mycursor = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = "SELECT * FROM universidad.bitacora;"

    mycursor.execute(querySQL)
    Bitacora_Ad = mycursor.fetchall()  # fetchall () Obtener todos los registros

    mycursor.close()  # cerrrando conexion SQL
    conexion_MySQLdb.close()  # cerrando conexion de la BD

    return Bitacora_Ad