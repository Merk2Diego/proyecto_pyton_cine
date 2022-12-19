import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def borrar_pelicula(conn, id):
   
    sql = 'DELETE FROM pelicula WHERE id_pelicula=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()



def main():
    database = r"cinemark.db"

    conn = create_connection(database)
    with conn:
        borrar_pelicula(conn, 2);
       
#probado y funciona
if __name__ == '__main__':
    main()