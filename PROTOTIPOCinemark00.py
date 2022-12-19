import sqlite3
from sqlite3 import Error

#creacion de la conexion a la base
def create_connection(db_file):
   
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        print(e)

    return conn


def create_tables(conn, create_tables_sql):
    
    try:
        c = conn.cursor()
        c.execute(create_tables_sql)
    except Error as e:
        print(e)

#definicion de tablas
def main():
    database = r"Cinemark.db"
                             
    sql_create_usuario_table = """ CREATE TABLE IF NOT EXISTS usuario (
                                        id_usuario integer PRIMARY KEY AUTOINCREMENT,
                                        dni integer NOT NUll,             
                                        apellidos text NOT NULL,
                                        nombres text NOT NULL,
                                        tipo_usuario text NOT NULL,
                                        email text,
                                        contrasenia text NOT NULL
                                    ); """
                                    
       
   
    sql_create_sala_table = """ CREATE TABLE IF NOT EXISTS sala (
                                        id_sala integer PRIMARY KEY  AUTOINCREMENT,
                                        nombre text NOT NULL,
                                        formato text NOT NULL,
                                        capacidad integer NOT NULL
                                    );  """ 
                                    
    sql_create_butaca_table = """ CREATE TABLE IF NOT EXISTS butaca (
                                        id_butaca integer PRIMARY KEY AUTOINCREMENT,
                                        fila text NOT NULL,
                                        numero integer NOT NULL,
                                        reserva text NOT NULL,
                                        id_sala integer NOT NULL,
                                        FOREIGN KEY (id_sala) REFERENCES sala (id_sala)
                                    );  """ 
                                    
    sql_create_tarjeta_table = """ CREATE TABLE IF NOT EXISTS tarjeta (
                                        id_tarjeta integer PRIMARY KEY AUTOINCREMENT,
                                        numero integer NOT NULL,
                                        banco text NOT NULL,
                                        titular text NOT NULL,
                                        fecha_cad text NOT NULL,   
                                        id_usuario integer NOT NULL,                                
                                        FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario)
                                    ); """
                                    
    sql_create_descuento_table = """ CREATE TABLE IF NOT EXISTS descuento (
                                        id_descuento integer PRIMARY KEY AUTOINCREMENT,
                                        dia text NOT NULL,
                                        porcentaje real NOT NULL                                
                                    ); """
                              
    sql_create_pelicula_table = """ CREATE TABLE IF NOT EXISTS pelicula (
                                        id_pelicula integer PRIMARY KEY AUTOINCREMENT,
                                        nombre text NOT NULL,
                                        director text NOT NULL,    
                                        reparto text NOT NULL,
                                        pais text NOT NULL,
                                        sinopsis text NOT NULL,
                                        duracion integer NOT NULL,
                                        genero text NOT NULL,
                                        clasificacion text NOT NULL,
                                        formato text NOT NULL,
                                        idioma text NOT NULL,
                                        subtitulada text NOT NULL
                                    ); """
                                    
    sql_create_sesion_table = """ CREATE TABLE IF NOT EXISTS sesion (
                                        id_sesion integer PRIMARY KEY AUTOINCREMENT,
                                        fecha text NOT NULL,
                                        hora text NOT NULL,
                                        id_sala integer NOT NULL,
                                        id_pelicula integer NOT NULL,
                                        FOREIGN KEY (id_sala) REFERENCES sala (id_sala),
                                        FOREIGN KEY (id_pelicula) REFERENCES pelicula (id_pelicula)
                                                                    
                                    ); """
                                    
    sql_create_reserva_table = """ CREATE TABLE IF NOT EXISTS reserva (
                                        id_reserva integer PRIMARY KEY AUTOINCREMENT,
                                        precio integer NOT NULL,
                                        fecha text NOT NULL,
                                        id_usuario integer NOT NULL,
                                        id_sesion integer NOT NULL,
                                        id_butaca integer NOT NULL,
                                        id_descuento integer NOT NULL,
                                        id_tarjeta integer NOT NULL,
                                        FOREIGN KEY (id_usuario) REFERENCES usuario (id_usuario),
                                        FOREIGN KEY (id_sesion) REFERENCES sesion (id_sesion),
                                        FOREIGN KEY (id_butaca) REFERENCES butaca (id_butaca),
                                        FOREIGN KEY (id_descuento) REFERENCES descuento (id_descuento),
                                        FOREIGN KEY (id_tarjeta) REFERENCES tarjeta (id_tarjeta)                           
                                    ); """
    
               
    # llamado a creacion de conexion
    conn = create_connection(database)

    # creacion de tablas 
    if conn is not None:
        
        create_tables(conn, sql_create_usuario_table)    
       
        create_tables(conn, sql_create_sala_table)
       
        create_tables(conn, sql_create_butaca_table)
        
        create_tables(conn, sql_create_tarjeta_table)

        create_tables(conn, sql_create_descuento_table)

        create_tables(conn, sql_create_pelicula_table)

        create_tables(conn, sql_create_sesion_table)

        create_tables(conn, sql_create_reserva_table)
    
        print("se termino.")
    else:
        print("Error! .")


if __name__ == '__main__':
    main()