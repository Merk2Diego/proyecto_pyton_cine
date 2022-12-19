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
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT id_pelicula,nombre FROM pelicula")

    rows = cur.fetchall()

    for row in rows:
        print(row)
def selecion_peli(conn, id):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM pelicula WHERE id_pelicula=?", (id,))

    rows = cur.fetchall()#metodo de cursor para obtener datos

    print(rows)

def main():
    database = r"Cinemark.db"
    
    # create a database connection
    conn = create_connection(database)
    with conn:

        print("Peliculas en cartelera")
        selecion_peliculas(conn)

        numero = int(input("Selecione numero pelicula: "))
        selecion_peli(conn, numero)

#probado y funciona
if __name__ == '__main__':
    main()