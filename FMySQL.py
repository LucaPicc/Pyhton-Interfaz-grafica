def creadorSQL(cursor,nomT):

    sql = ("CREATE TABLE IF NOT EXISTS %s (Name VARCHAR(50),Mail VARCHAR(50),Direccion VARCHAR(50))" % nomT)
    cursor.execute(sql)
    print("Tabla creada")


def insertSQL(cursor,nameT,name,mail,dir):

    sql=("INSERT INTO %s VALUES ('%s','%s','%s')" % (nameT, name, mail, dir ))
    cursor.execute(sql)
    print(sql)