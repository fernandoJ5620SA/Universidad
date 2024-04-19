# Importando Libreria mysql.connector para conectar Python con MySQL
# pip install mysql-connector-python

import mysql.connector

def connectionBD():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="1423#Ghz1233",
        database="Universidad"
    )