import tkinter as tk
from tkinter import messagebox
import ventreserva 
from cineconsulta2 import *


class usuario(tk.Toplevel):
    def __init__(self, parent,  *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        
        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="email", highlightbackground='black')
        self.Label.grid(row=2, column=0, sticky="nsew")

        self.email=tk.StringVar()
        self.display=tk.Entry(self, bd=5,textvariable=self.email)
        self.display.grid(row=2, column=1, sticky="nsew")

        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="contraseña", highlightbackground='black')
        self.Label.grid(row=4, column=0, sticky="nsew")

        self.contra=tk.StringVar()
        self.display=tk.Entry(self, bd=5,textvariable=self.contra)
        self.display.grid(row=4, column=1, sticky="nsew")

        self.ceButton = tk.Button(self, font=("Arial", 12), fg='red', text="Aceder", highlightbackground='yellow',command=self.aceder)
        self.ceButton.grid(row=5, column=1, sticky="nsew")
   
        self.ceButton= tk.Button(self, text="Volver", command=self.volver)
        self.ceButton.grid(row=5, column=0, sticky="nsew")
        self.parent.withdraw()
        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="", highlightbackground='black')
        self.Label.grid(row=6, column=0, sticky="nsew")
    
    def aceder(self):
        database=r"Cinemark.db"
        conn = create_connection(database)
        contrase=selecion_usuario(conn, self.email.get())

        textomalo="Usuario no encontrado"
        if contrase == textomalo:
            self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text=textomalo, highlightbackground='black')
            self.Label.grid(row=6, column=0, sticky="nsew")
        elif contrase == (self.contra.get(),):
            print(contrase)
            self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="", highlightbackground='black')
            self.Label.grid(row=6, column=0, sticky="nsew")
            ventreserva.usuariov(self.parent)
            self.destroy()

        else:
            self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="contraseña erronea", highlightbackground='black')
            self.Label.grid(row=6, column=0, sticky="nsew")
    '''def proximavent(self):
        ventreserva.usuariov(self.parent)'''
    

    def volver(self):
        self.parent.deiconify()
        self.destroy()

