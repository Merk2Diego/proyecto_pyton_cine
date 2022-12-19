import tkinter as tk
import ventusuario
import ventpeliculas
import ventLogin
#funciona falta pulir 
class menu(tk.Frame):
    def __init__(self, parent, *args,**kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Configuración")
        #self.configure(background='light grey') # Color de Fondo
        self.crearWidgets()
    
    def crearWidgets(self):
        self.Label= tk.Label(self)
        self.Label.grid(row=1)
        self.ceButton = tk.Button(self, font=("Arial", 12), fg='red', text="Peliculas", highlightbackground='yellow',command=self.funcionPeli)
        self.ceButton.grid(row=2)
        self.Label= tk.Label(self)
        self.Label.grid(row=3)
        self.ceButton = tk.Button(self, font=("Arial", 12), fg='black', text="LOGIN", highlightbackground='yellow',command=self.funcionLogin)
        self.ceButton.grid(row=4)
        self.Label= tk.Label(self)
        self.Label.grid(row=5)
        self.ceButton = tk.Button(self, font=("Arial", 12), fg='blue', text="CREA", highlightbackground='yellow',command=self.funcion1)
        self.ceButton.grid(row=6)
        self.Label= tk.Label(self)
        self.Label.grid(row=7)

    def funcion1(self):
        ventusuario.usuario(self.parent)
    def funcionPeli(self):
        ventpeliculas.uspeli(self.parent)
    def funcionLogin(self):
        ventLogin.usuario(self.parent)

if __name__ == "__main__":
    root = tk.Tk()
    menu(root).pack(side="top", fill="both", expand=True)
    #menu(root)
    root.mainloop()