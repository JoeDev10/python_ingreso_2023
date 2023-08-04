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
Al presionar el botón Mostrar pedir valores por prompt hasta que el usuario ingrese el valor 9 (se deberá utilizar 'BREAK').
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        for i in range(100000000):
            numero_ingresado = prompt("utn", "ingrese el numero 9 si desea salir")
            numero_ingresado = int(numero_ingresado)
            
            # Comprobar si el número ingresado es igual a 9.
            if numero_ingresado == 9:
            # Si el usuario ingresa el número 9, se sale del bucle.
                break
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()