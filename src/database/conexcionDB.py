# Importando Libreria mysql.connector para conectar Python con MySQL
# pip install mysql-connector-python

import mysql.connector


def connectionBD():
    mydb = mysql.connector.connect(
        host="localhost", port=3306, user="root", passwd="", database="universidad" 
    )

    return mydb
