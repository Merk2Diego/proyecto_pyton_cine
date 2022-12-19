import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def actualizar_pelicula(conn, titulo):
  
    sql = ''' UPDATE pelicula
              SET nombre = ? 
              WHERE id_pelicula = ?'''
    cur = conn.cursor()
    cur.execute(sql, titulo)#cur.execute funciona con tuplas
    conn.commit()


def main():
    database = r"Cinemark.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        nombre = input("Ingrese nombre: ")
        numero = int(input("Ingrese numero: "))
        actualizar_pelicula(conn, (nombre,numero))

#probado y funciona

if __name__ == '__main__':
    main()