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
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_cargar.grid(row=2, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar Estadísticas", command=self.btn_mostrar_estadisticas_on_click)
        self.btn_mostrar.grid(row=3, padx=20, pady=20,
                            columnspan=2, sticky="nsew")

        self.lista = []
        

    def btn_comenzar_ingreso_on_click(self):
        contador_de_ceros = 0
        negativo_mas_bajo = 0
        positivo_mas_alto = 0
        bandera_primer_ingreso = False
        acumulador_negativos = 0
        contador_negativos = 0
        acumulador_positivos = 0
        contador_positivos = 0
        
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
            
            if numero_ingresado < negativo_mas_bajo or bandera_primer_ingreso == False:
                negativo_mas_bajo = numero_ingresado
                
            if numero_ingresado > positivo_mas_alto or bandera_primer_ingreso == False:
                positivo_mas_alto = numero_ingresado
                bandera_primer_ingreso = True
    
        
        if contador_negativos != 0:
            promedio_negativos = acumulador_negativos / contador_negativos
        else:
            promedio_negativos = "no hubo\n\
            numeros negativos"
        
        
        estadisticas = f'''
        la suma acumulada de negativos: {acumulador_negativos}
        la suma acumulada de los positivos: {acumulador_positivos}
        la cantidad de numeros positivos ingresados: {contador_positivos}
        la cantidad de numeros negativos ingresados: {contador_negativos}
        la cantidad de ceros ingresados: {contador_de_ceros}
        el minimo de los negativos: {negativo_mas_bajo}
        el maximo de los positivos: {positivo_mas_alto}
        el promedio de los negativos: {promedio_negativos}
        '''
        self.lista.append(estadisticas)
        
    def btn_mostrar_estadisticas_on_click(self):
        alert("utn", self.lista)
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el
usuario quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    a. La suma acumulada de los negativos
    b. La suma acumulada de los positivos
    c. Cantidad de números positivos ingresados
    d. Cantidad de números negativos ingresados
    e. Cantidad de ceros
    f. El minimo de los negativos
    g. El maximo de los positivos
    h. El promedio de los negativos

Informar los resultados mediante alert()

'''