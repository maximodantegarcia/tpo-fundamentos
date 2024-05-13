from typing import Self
import mysql.connector   
 
class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='basededatos', 
                                            user = 'root',
                                            password ='03579')

    def inserta_producto( legajo, Apellido_y_nombre, direccion, localidad, cp, fecha_ingreso, Antigüedad, Fecha_Nacimiento, Edad, DNI, nro, cat, oficina, Nombre_Oficina, Secretaria, sindicato, Sepelio, Mutual, solo_4, Coseguro, Seguro, PUESTO, SEXO, ANTIGÜEDAD, ESTUDIO):
        cur = Self.conexion.cursor()

        sql='''INSERT INTO sindicato ( LEGAJO, APELLIDO_Y_NOMBRE, DIRECCION, LOCALIDAD, CP, FECHA_INGRESO, ANTIGUEDAD, FECHA_DE_NACIMIENTO, EDAD, DNI, NRO, CAT, OFICINA, NOMBRE_OFICINA, SECRETARIA, SINDICATO, SEPELIO, MUTUAL, SOLO_4, COSEGURO, SEGURO, PUESTO, SEXO, ANTIGÜEDAD, ESTUDIO) 
        VALUES('{}', '{}','{}', '{}','{}''{}', '{}','{}', '{}','{}''{}', '{}','{}', '{}','{}''{}', '{}','{}', '{}','{}')'''.format(legajo, Apellido_y_nombre, direccion, localidad, cp, fecha_ingreso, Antigüedad, Fecha_Nacimiento, Edad, DNI, nro, cat, oficina, Nombre_Oficina, Secretaria, sindicato, Sepelio, Mutual, solo_4, Coseguro, Seguro, PUESTO, SEXO, ANTIGÜEDAD, ESTUDIO)
        cur.execute(sql)
        Self.conexion.commit()    
        cur.close()



    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM sindicato    " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM sindicato WHERE APELLIDO_Y_NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 

        

 