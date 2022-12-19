import tkinter as tk
from tkinter import messagebox
from cineconsulta2 import *

class uspeli(tk.Toplevel):
    def __init__(self, parent,  *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        database = r"Cinemark.db"
        conn = create_connection(database)
        rows=selecion_peliculas(conn)
        i=0
        for row in rows:
            i+=1
            row1=row[0:4]
            self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text=row1, highlightbackground='black')
            self.Label.grid(row=i,sticky="nw")
            i+=1
            row2=row[5]
            self.Label= tk.Label(self, font=("Arial", 12), fg='black', text=row2, highlightbackground='black')
            self.Label.grid(row=i,sticky="nw")
            i+=1
            row3=row[6:]
            self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text=row3, highlightbackground='black')
            self.Label.grid(row=i,sticky="nw")
        

        self.ceButton= tk.Button(self, text="Volver", command=self.volver)
        self.ceButton.grid(row=0, sticky="nw")
        self.parent.withdraw()


    def volver(self):
        self.parent.deiconify()
        self.destroy()