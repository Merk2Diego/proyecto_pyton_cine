import sqlite3
from sqlite3 import Error

from cineAdm import *
from cinecliente import *
def create_connection(db_file):
    """creando la conexion a Cinemark.db"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)

    return conn


def create_usuario(conn, usuario):
    
    sql = ''' INSERT INTO usuario(dni,apellidos,nombres,tipo_usuario,email,contrasenia)
              VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, usuario)
    conn.commit()
    return cur.lastrowid



def create_butaca(conn, butaca):
    
    sql = ''' INSERT INTO butaca(fila, numero, reserva, id_sala)
              VALUES(?,?,?,?) '''
              
    cur = conn.cursor()
    cur.execute(sql, butaca)
    conn.commit()
    return cur.lastrowid

def create_tarjeta(conn, tarjeta):
   

    sql = ''' INSERT INTO tarjeta(numero,banco,titular,fecha_cad,id_usuario)
              VALUES(?,?,?,?,?)'''
                    
    cur = conn.cursor()
    cur.execute(sql, tarjeta)
    conn.commit()
    return cur.lastrowid

def create_descuento(conn, descuento):
   

    sql = ''' INSERT INTO descuento(dia,porcentaje)
              VALUES(?,?)'''
                    
    cur = conn.cursor()
    cur.execute(sql, descuento)
    conn.commit()
    return cur.lastrowid

def create_pelicula(conn, pelicula):
   
    sql = ''' INSERT INTO pelicula(nombre, director,reparto,pais,sinopsis,duracion,genero,clasificacion,formato, idioma, subtitulada)
            VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, pelicula)
    conn.commit()
    return cur.lastrowid

def create_sesion(conn, sesion):
   
    sql = ''' INSERT INTO sesion(fecha, hora, id_sala, id_pelicula)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, sesion)
    conn.commit()
    return cur.lastrowid