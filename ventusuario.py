import tkinter as tk
from tkinter import messagebox
from ventregistro import *

class usuario(tk.Toplevel):
    def __init__(self, parent,  *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="Nombres", highlightbackground='black')
        self.Label.grid(row=0, column=0, sticky="nsew")  

        self.nombre=tk.StringVar()
        self.display=tk.Entry(self, bd=1,textvariable=self.nombre)  
        self.display.grid(row=0, column=1, sticky="nsew") 

        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="Apellidos", highlightbackground='black')
        self.Label.grid(row=2, column=0, sticky="nsew") 

        self.apellido=tk.StringVar() 
        self.display=tk.Entry(self, bd=3,textvariable=self.apellido)  
        self.display.grid(row=2, column=1, sticky="nsew") 

        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="DNI", highlightbackground='black')
        self.Label.grid(row=4, column=0, sticky="nsew")

        self.DNI=tk.StringVar()
        self.display=tk.Entry(self, bd=5,textvariable=self.DNI)
        self.display.grid(row=4, column=1, sticky="nsew")

        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="email", highlightbackground='black')
        self.Label.grid(row=6, column=0, sticky="nsew")

        self.email=tk.StringVar()
        self.display=tk.Entry(self, bd=5,textvariable=self.email)
        self.display.grid(row=6, column=1, sticky="nsew")

        self.Label= tk.Label(self, font=("Arial", 12), fg='blue', text="contraseña", highlightbackground='black')
        self.Label.grid(row=8, column=0, sticky="nsew")

        self.contra=tk.StringVar()#contraseña
        self.display=tk.Entry(self, bd=5,textvariable=self.contra)
        self.display.grid(row=8, column=1, sticky="nsew")

        self.ceButton = tk.Button(self, font=("Arial", 12), fg='red', text="CREAR", highlightbackground='yellow',command=self.mostrar)
        self.ceButton.grid(row=10, column=1, sticky="nsew")
   
        self.ceButton= tk.Button(self, text="Volver", command=self.volver)
        self.ceButton.grid(row=11, column=1, sticky="nsew")
        self.parent.withdraw()

    def mostrar(self):
        
        usuario=(int(self.DNI.get()),self.nombre.get(),self.apellido.get(),"cliente",self.email.get(),self.contra.get())
        database=r"Cinemark.db"
        conn = create_connection(database)
        create_usuario(conn, usuario)
    
    def volver(self):
        self.parent.deiconify()
        self.destroy()