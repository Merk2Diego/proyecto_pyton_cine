import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def selecion_peliculas(conn):
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM pelicula")

    rows = cur.fetchall()

    return rows

def selecion_peli(conn, id):
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM pelicula WHERE id_pelicula=?", (id,))

    rows = cur.fetchall()#metodo de cursor para obtener datos

    return(rows)
    
def selecion_usuario(conn, id):
    
        cur = conn.cursor()
        cur.execute("SELECT contrasenia FROM usuario WHERE email=?", (id,))

        rows = cur.fetchall()#metodo de cursor para obtener datos
        if rows :
            return(rows[0])
        else:
            return("Usuario no encontrado")

