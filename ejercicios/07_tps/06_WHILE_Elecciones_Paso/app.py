'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        votos_mas_altos = 0
        votos_mas_bajos = 0
        acumulador_total_votos = 0
        bandera_votos_primer_ingreso = False
        acumulador_edades = 0
        contador_edades = 0
        respuesta = True
        
        
        while respuesta == True:
            nombre = prompt("utn", "ingrese nombre")
            edad = prompt("utn", "ingrese edad")
            edad = int(edad)
            votos_ingresados = prompt("utn", "ingrese votos")
            votos_ingresados = int(votos_ingresados)
            
            while len(nombre) < 3:
                nombre = prompt("error", "reingrese nombre")
                
            while edad < 25:
                edad = prompt("error", "reingrese edad")
                
            while votos_ingresados < 0:
                votos_ingresados = prompt("error", "reingrese votos")
                
            # a. nombre del candidato con más votos
            if votos_ingresados > votos_mas_altos or bandera_votos_primer_ingreso == False:
                votos_mas_altos = votos_ingresados
                nombre_candidato_mas_votado = nombre
                
            # nombre y edad del candidato con menos votos    
            if votos_ingresados < votos_mas_bajos or bandera_votos_primer_ingreso == False:
                votos_mas_bajos = votos_ingresados
                nombre_candidato_menos_votado = nombre
                edad_candidato_menos_votado = edad
                bandera_votos_primer_ingreso = True
                
            # c. el promedio de edades de los candidatos
            acumulador_edades += edad
            contador_edades += 1
            
            # d. total de votos emitidos.
            acumulador_total_votos += votos_ingresados
        
            respuesta = question("utn", "desea continuar")
            
        promedio = acumulador_edades / contador_edades
        print("utn", f'''
            el nombre del candidato mas votado es: {nombre_candidato_mas_votado}
            el nombre del candidato menos votado es: {nombre_candidato_menos_votado}
            y su edad es: {edad_candidato_menos_votado}
            el promedio de edades es: {promedio:.0f}
            y el total de votos emitidos es: {acumulador_total_votos}
            ''')
            

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
    
    '''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar:
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
    

        # ASI NO!!!
        
        # respuesta = True
        # votos_mas_altos = None
        # votos_mas_bajos = None
        # acumulador_votos_totales = 0
        # acumulador_edad = 0
        # contador_edad = 0

        # while respuesta == True:
        #     nombre = prompt("utn", "ingrese nombre")
        #     while nombre == "":
        #         nombre = prompt("utn", "ingrese nombre")

        #     edad = prompt("utn", "ingrese edad")
        #     edad = int(edad)
        #     while edad == "" and edad < 25:
        #         edad = prompt("utn", "ingrese edad")
        #         edad = int(edad)

        #     votos_ingresados = prompt("utn", "ingrese votos_ingresados")
        #     votos_ingresados = int(votos_ingresados)
        #     while votos_ingresados == "" and votos_ingresados < 0:
        #         votos_ingresados = prompt("utn", "ingrese votos_ingresados")
        #         votos_ingresados = int(votos_ingresados)

        #     if votos_mas_altos == None or votos_ingresados > votos_mas_altos:
        #         votos_mas_altos = votos_ingresados
        #         nombre_candidato_mas_votado = nombre
        #     else:
        #         if votos_mas_bajos == None or votos_ingresados < votos_mas_bajos:
        #             votos_mas_bajos = votos_ingresados
        #             nombre_candidato_menos_votado = nombre
        #             edad_candidato_menos_votado = edad

        #     contador_edad += 1
        #     acumulador_edad += edad
        #     acumulador_votos_totales += votos_ingresados

        #     respuesta = question("utn", "¿Desea ingresar otro candidato?")

        # promedio = acumulador_edad / contador_edad
        # print(f'''
        #     el candidato con mas votos es: {nombre_candidato_mas_votado}
        #     el candidato menos votado es: {nombre_candidato_menos_votado}
        #     su edad es: {edad_candidato_menos_votado}
        #     el promedio de edad es: {promedio}
        #     su total de votos es: {acumulador_votos_totales}
        #     ''')