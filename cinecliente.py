import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
#operaciones reservas cliente

def selecion_sesion(conn, id):

    cur = conn.cursor()
    cur.execute("SELECT * FROM sesion WHERE id_pelicula=?", (id,))

    rows = cur.fetchall()#metodo de cursor para obtener datos
    for row in rows:
        print(row)
    return rows

def selecion_peli(conn, id):

    cur = conn.cursor()
    cur.execute("SELECT * FROM pelicula WHERE id_pelicula=?", (id,))

    rows = cur.fetchall()#metodo de cursor para obtener datos
    return rows

def selecion_peliculas(conn):
   
    cur = conn.cursor()
    cur.execute("SELECT id_pelicula,nombre FROM pelicula")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
def crea_reserva(conn, reserva):
  
    sql = ''' INSERT INTO reserva(precio, fecha, id_usuario, id_sesion, id_butaca, id_descuento,id_tarjeta)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, reserva)
    conn.commit()
    return cur.lastrowid

def actualizar_reserva(conn, tarea):
    
    sql = ''' UPDATE reserva
              SET fecha = ? ,
                  id_sesion = ? ,
                  id_butaca = ?
              WHERE id_reserva = ?'''
    cur = conn.cursor()
    cur.execute(sql, tarea)
    conn.commit()


    
def reserva_cliente(conn, id_usuario,numero):
    cur = conn.cursor()
    cur.execute("SELECT * FROM reserva WHERE id_usuario=?", (id_usuario,))

    rows = cur.fetchall()#metodo de cursor para obtener datos

    for row in rows:
        if numero == row[0]:
            return row

def historial_cliente(conn, id):

    cur = conn.cursor()
    cur.execute("SELECT * FROM reserva WHERE id_usuario=?", (id,))

    rows = cur.fetchall()#metodo de cursor para obtener datos

    for row in rows:
        print(row)

def ver_descuentos(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM descuento")
    rows = cur.fetchall()
    for row in rows:
        print(row)
       
def main():

    database=r"Cinemark.db"
    conn = create_connection(database)

    with conn:
        print("Opciones")
        print("1 - Crear Reserva")
        print("2 - Consultas Reservas")
        print("3 - Actualizar Reservas")
        print("4 - Ver Historial")
        print("5 - Para Salir")

        opcion=int(input("Seleccione opcion: "))

        if opcion == 1:
            print("Peliculas en cartelera")
            selecion_peliculas(conn)
            pelicula = int(input("Selecione numero pelicula: "))
            selecion_sesion(conn, pelicula)
            sesion = int(input("Selecione sesion: "))
            ver_descuentos(conn)
            dia=int(input("Ingrese Numero del dia de la semana: "))
            numbutaca = int(input("Ingrese Numero de butaca:"))
            tarjeta = int(input("Ingrese numero de tarjeta: "))#buscar tarjeta con el dni
            fecha=input("Ingrese Fecha: ")
            reserva=(500,fecha, 2, sesion, numbutaca, dia, tarjeta)
            crea_reserva(conn,reserva)
        elif opcion == 2:
            id_reser=int(input("ingrese el numero de reserva: "))
            print(reserva_cliente(conn, 4,id_reser))

        elif opcion == 3:
            id_reser=int(input("ingrese el numero de reserva: "))
            reserva_cliente(conn, 4,id_reser)
            fecha = input("ingrese nueva fecha: ")
            sesion= input("ingrese nueva sesion: ")
            butaca= input("ingrese nueva butaca: ")
            actualizar_reserva(conn, (fecha,sesion,butaca,id_reser))
    
        elif opcion == 4:
            print("Reservas:")
            historial_cliente(conn, 4)

        else:
            print("Gracias por ocupar nuestro servicio")



if __name__ == '__main__':
    main()