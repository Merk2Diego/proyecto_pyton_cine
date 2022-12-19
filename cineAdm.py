import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
# operaciones sobre sala    
def crear_Sala(conn, especificaciones):

    sql = ''' INSERT INTO sala(nombre,formato,capacidad)
              VALUES(?,?,?) '''# inseta datos en la base
    cur = conn.cursor()
    cur.execute(sql, especificaciones)
    conn.commit()
    return cur.lastrowid

def actualizar_Sala(conn, tarea):
    
    sql = ''' UPDATE sala
              SET formato = ?
              WHERE id_sala = ?'''
    cur = conn.cursor()
    cur.execute(sql, tarea)
    conn.commit()

def eliminar_Sala(conn, id):
    
    sql = 'DELETE FROM sala WHERE id_sala=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
#operaciones sobre descuentos
def descuentos(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM descuento")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def actualizar_descuentos(conn, tarea):
    
    sql = ''' UPDATE descuento
              SET porcentaje = ?
              WHERE id_descuento = ?'''
    cur = conn.cursor()
    cur.execute(sql, tarea)
    conn.commit()

# Operaciones de Reservas
def todas_reservas(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM reserva")

    rows = cur.fetchall()

    for row in rows:
        print(row)    

def reservas_cliente(conn, id):

    cur = conn.cursor()
    cur.execute("SELECT * FROM reserva WHERE id_usuario=?", (id,))

    rows = cur.fetchall()#metodo de cursor para obtener datos

    for row in rows:
        print(row)
# menu de opciones
def main():

    database=r"Cinemark.db"
    conn = create_connection(database)

    with conn:
        print("Opciones")
        print("1 - Crear Sala")
        print("2 - Modificar Sala")
        print("3 - Eliminar Sala")
        print("4 - Modificar Descuentos")
        print("5 - Ver Reserva todos clientes")
        print("6 - Ver Historial Reserva")
        print("7 - Para Salir")
        
        opcion=int(input("Seleccione opcion: "))

        if opcion == 1:
            nombre=input("Ingrese nombre de la Sala: ")
            capacidad=int(input("Ingrese Capacidad: "))
            formato=input("Ingrese Formato de la Pelicula: ")
            crear_Sala(conn, (nombre,formato,capacidad))
        elif opcion == 2:
            numero=int(input("Ingrese Numero de la Sala: "))
            formato=input("Ingrese Formato de la Pelicula: ")
            actualizar_Sala(conn, (formato,numero))
        elif opcion == 3:
            numero=int(input("Ingrese Numero de sala a eliminar: "))
            eliminar_Sala(conn, numero)
        elif opcion == 4:
            descuentos(conn)
            numero=int(input("Ingrese el numero del dia desea modificar: "))
            desc=float(input("ingrese el descuento: "))
            actualizar_descuentos(conn, (desc,numero))
        elif opcion == 5:
            print("Todas las Reservas son: ")
            todas_reservas(conn)
        elif opcion == 6:
            numero=int(input("Ingrese Numero de Cliente: "))
            reservas_cliente(conn, numero)
        else:
            print("Gracias por utilizar")
        


if __name__ == '__main__':
    main()