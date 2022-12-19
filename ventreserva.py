
import tkinter as tk
from tkinter import messagebox

class usuariov(tk.Toplevel):
    def __init__(self, parent,  *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="Opciones:", highlightbackground='black')
        self.Label.grid(row=0, column=0, sticky="nsew")  
        
        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="1 - Crear Reserva", highlightbackground='black')
        self.Label.grid(row=2, column=0, sticky="nsew") 

        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="2 - Consultas Reservas", highlightbackground='black')
        self.Label.grid(row=3, column=0, sticky="nsew")

        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="3 - Actualizar Reservas", highlightbackground='black')
        self.Label.grid(row=4, column=0, sticky="nsew")

        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="4 - Ver Historial", highlightbackground='black')
        self.Label.grid(row=5, column=0, sticky="nsew")


        self.Label = tk.Label(self, font=("Arial", 12), fg='red', text="5 - Para Salir", highlightbackground='yellow')
        self.Label.grid(row=6, column=0, sticky="nsew")

        self.opcion=tk.StringVar()#opcion
        self.display=tk.Entry(self, bd=5,textvariable=self.opcion)
        self.display.grid(row=8, column=1, sticky="nsew")
   
        self.ceButton= tk.Button(self, text="volver", command=self.volver)
        self.ceButton.grid(row=11, column=0, sticky="nsew")
        self.ceButton= tk.Button(self, text="acede", command=self.volver)
        self.ceButton.grid(row=11, column=1, sticky="nsew")
        self.parent.withdraw()

    def volver(self):
            self.parent.deiconify()
            self.destroy()
        