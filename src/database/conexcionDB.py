# Importando Libreria mysql.connector para conectar Python con MySQL
# pip install mysql-connector-python

import mysql.connector


def connectionBD():
    mydb = mysql.connector.connect(
<<<<<<< HEAD
        host="localhost", port=3306, user="root", passwd="", database="universidad"
=======
        host="localhost", port=3306, user="root", passwd="", database="universidad" 
>>>>>>> 9e13c3931a8befb3987f3b9ef8f9a191e5c240ec
    )

    return mydb
