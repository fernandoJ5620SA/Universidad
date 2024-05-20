from src.database.conexcionDB import *

def obtener_usuario_por_id(User_id):
    conexion_MySQLdb = connectionBD()
    mycursor = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = "SELECT * FROM universidad.useruni WHERE User_id = %s"
    valores = (User_id)

    mycursor.execute(querySQL, valores)
    usuario = mycursor.fetchone()

    mycursor.close()
    conexion_MySQLdb.close()

    return usuario