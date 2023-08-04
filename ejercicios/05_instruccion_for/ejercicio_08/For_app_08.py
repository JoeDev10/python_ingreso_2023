import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Joel
apellido: Rodriguez
'''

'''
Al presionar el botón Mostrar pedir un número. Informar si el número es PRIMO o no.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero_ingresado = prompt("utn", "ingrese numero")
        numero_ingresado = int(numero_ingresado)
        contador_divisores = 0
        
        for i in range(1, numero_ingresado + 1):
            if numero_ingresado % i == 0:
                contador_divisores += 1
        if contador_divisores == 2:
            alert("utn", "el numero es primo")
        else:
            alert("utn", "el numero no es primo")
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()