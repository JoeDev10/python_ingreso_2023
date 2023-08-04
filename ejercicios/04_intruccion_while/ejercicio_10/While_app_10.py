import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        contador_negativos = 0
        contador_de_ceros = 0
        
        while True:
            numero_ingresado = prompt("utn", "ingrese numeros")
            if numero_ingresado == None:
                break
            numero_ingresado = int(numero_ingresado)
        
            if numero_ingresado < 0:
                acumulador_negativos += numero_ingresado
                contador_negativos += 1
            else:
                if numero_ingresado > 0:
                    acumulador_positivos += numero_ingresado
                    contador_positivos += 1
                else:
                    contador_de_ceros += 1
                    
        diferencia = acumulador_positivos - acumulador_negativos
        
        alert("utn", f'''
            la suma acumulada de negativos: {acumulador_negativos}
            la suma acumulada de los positivos: {acumulador_positivos}
            la cantidad de numeros positivos: {contador_positivos}
            la cantidad de numeros negativos: {contador_negativos}
            la cantidad de ceros: {contador_de_ceros}
            la diferencia: {diferencia}
            ''')
        
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''