from src.database.conexcionDB import *


# C
def insertar_carrera(
    id_carrera, cve_carrera, nombre_carrera, duracion, requisitos_ad, creditos_gradu
):
    conexion_MySQLdb = connectionBD()
    mycursor = conexion_MySQLdb.cursor()
    querySQL = "INSERT INTO universidad.uni_carreras (id_carrrera, Cve_Carrera,Nombre_Carrera,Duracion,Requisitos_ad,Creditos_gradu) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (
        id_carrera,
        cve_carrera,
        nombre_carrera,
        duracion,
        requisitos_ad,
        creditos_gradu,
    )

    mycursor.execute(querySQL, valores)
    conexion_MySQLdb.commit()  # Guardar los cambios

    mycursor.close()
    conexion_MySQLdb.close()

    return "Carrera insertada exitosamente"


# R
def usuarios():
    conexion_MySQLdb = connectionBD()  # Hago instancia a mi conexion desde la funcion
    mycursor = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = "SELECT * FROM universidad.uni_carreras;"

    mycursor.execute(querySQL)
    carrera = mycursor.fetchall()  # fetchall () Obtener todos los registros

    mycursor.close()  # cerrrando conexion SQL
    conexion_MySQLdb.close()  # cerrando conexion de la BD

    return carrera


# Obtener carrera por ID (para usar en la actualización)
def obtener_carrera_por_id(id_carrrera):
    conexion_MySQLdb = connectionBD()
    mycursor = conexion_MySQLdb.cursor(dictionary=True)
    querySQL = "SELECT * FROM universidad.uni_carreras WHERE id_carrrera = %s"
    valores = (id_carrrera,)

    mycursor.execute(querySQL, valores)
    carrera = mycursor.fetchone()

    mycursor.close()
    conexion_MySQLdb.close()

    return carrera


# U
def actualizar_carrera(
    id_carrrera, cve_carrera, nombre_carrera, duracion, requisitos_ad, creditos_gradu
):
    conexion_MySQLdb = connectionBD()
    mycursor = conexion_MySQLdb.cursor()
    querySQL = """
        UPDATE universidad.uni_carreras
        SET Cve_Carrera = %s, Nombre_Carrera = %s, Duracion = %s, Requisitos_ad = %s, Creditos_gradu = %s
        WHERE id_carrrera = %s
    """
    valores = (
        cve_carrera,
        nombre_carrera,
        duracion,
        requisitos_ad,
        creditos_gradu,
        id_carrrera,
    )

    mycursor.execute(querySQL, valores)
    conexion_MySQLdb.commit()

    mycursor.close()
    conexion_MySQLdb.close()

    return "Carrera actualizada exitosamente"


# D
def eliminar_carrera(id_carrera):
    conexion_MySQLdb = connectionBD()
    mycursor = conexion_MySQLdb.cursor()
    querySQL = "DELETE FROM universidad.uni_carreras WHERE id_carrrera = %s"
    valores = (id_carrera,)

    mycursor.execute(querySQL, valores)
    conexion_MySQLdb.commit()

    mycursor.close()
    conexion_MySQLdb.close()

    return "Carrera eliminada exitosamente"
