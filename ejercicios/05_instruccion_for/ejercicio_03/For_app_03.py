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
Enunciado:
Al presionar el botón Mostrar tomar del campo de texto cantidad de veces que se desea
repetir el mensaje "Hola UTN FRA" (utilizando el Dialog Alert)
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="saludo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)

        self.txt_repetir = customtkinter.CTkEntry(master=self)
        self.txt_repetir.grid(row=0, column=1)

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        # Obtener el contenido del campo de texto "txt_repetir"
        cantidad = self.txt_repetir.get()
        # parseamos a entero la variable cantidad
        cantidad = int(cantidad)
        
        # Bucle for que se repetirá 'cantidad' veces
        for i in range(0, cantidad):
            alert("mensaje", "hola UTN FRA")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
