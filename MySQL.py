import mysql.connector
import FMySQL

#Creo un diccionario para que se conecte

dbConnector = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'usuarios'
}
nomT = 'User'
#creo la conección y el cursor
conexion = mysql.connector.connect(**dbConnector)
cursor = conexion.cursor()

FMySQL.creadorSQL(cursor,nomT)

FMySQL.insertSQL(cursor,nomT,"Luca","luca.piccinini","Av. Mitre")

conexion.commit()

