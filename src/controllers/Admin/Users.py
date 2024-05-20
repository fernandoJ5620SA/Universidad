from src.database.conexcionDB import *


#R
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

#Obtener usuario por ID  (para usar en la actualización)
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

#U
def actualizar_usuario(
          User_id, name, email, password, fk_User_Role
):
    conexion_MySQL = connectionBD()
    mycursor = conexion_MySQL.cursor()
    querySQL = """
        UPDATE universidad.useruni
        SET name = %s, email = %s, password = %s, fk_User_Role= %s    
        WHERE User_id = %s
        """
    valores = ( name, email, password, fk_User_Role, User_id)
    mycursor.execute(querySQL, valores)
    conexion_MySQL.commit()

    return "Usuario actualizado exitosamente"

#D
def eliminar_usuario(User_id):
    conexion_MySQLdb = connectionBD()
    mycursor = conexion_MySQLdb.cursor() 
    querySQL = "DELETE FROM universidad.useruni WHERE User_id = %s"
    valores = (User_id,) 

    mycursor.execute(querySQL, valores)  
    conexion_MySQLdb.commit()  

    mycursor.close()  
    conexion_MySQLdb.close()

    return "Usuario eliminado exitosamente"