
'''
nombre: Joel
apellido: Rodriguez
'''
'''
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

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
        contador = 0 # Contador general de postulantes
        contador_genero_NB = 0  # Contador de postulantes no binarios con ciertas condiciones
        bandera = False # Bandera para identificar si se encontró un postulante "Jr" con la edad más baja
        edad_postulante_mas_chico = 0 # Edad del postulante "Jr" más joven
        nombre_postulante_mas_chico = None # Nombre del postulante "Jr" más joven

        acumulador_edades_NB = 0 # Acumulador de edades de postulantes no binarios
        acumulador_edades_M = 0 # Acumulador de edades de postulantes masculinos
        acumulador_edades_F = 0  # Acumulador de edades de postulantes femeninas
        contador_edades_NB = 0  # Contador de postulantes no binarios
        contador_edades_M = 0  # Contador de postulantes masculinos
        contador_edades_F = 0 # Contador de postulantes femeninas

        contador_Python = 0 # Contador de postulantes con experiencia en Python
        contador_JS = 0 # Contador de postulantes con experiencia en JavaScript
        contador_asp_net = 0 # Contador de postulantes con experiencia en ASP.NET

        tecnologia_postulantes_max = None # Tecnología con más postulantes

        contador_genero_M = 0 # Contador de postulantes masculinos
        contador_genero_F = 0 # Contador de postulantes femeninas

        # Ciclo para ingresar datos de 10 postulantes
        for i in range(10):

            nombre = prompt("utn", "ingrese nombre")
            while len(nombre) < 3:
                nombre = prompt("utn", "reingrese nombre")

            edad = prompt("utn", "ingrese edad")
            edad = int(edad)
            while edad < 18:
                edad = prompt("utn", "reingrese edad")
                edad = int(edad)

            genero = prompt("utn", "ingrese genero las opciones son: F, M, NB")
            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt("utn", "reingrese genero")

            tecnologia = prompt(
                "utn", "ingrese tecnologia, las opciones son: PYTHON, JS, ASP.NET")
            while tecnologia != "PYTHON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("utn", "reingrese tecnologia")

            puesto = prompt("utn", "ingrese puesto, las opciones: Jr, Ssr, Sr")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("utn", "reingrese puesto")

            contador += 1 # Aumentar el contador de postulantes

            # Verificar si el postulante es "NB" y cumple con ciertas condiciones para incrementar el contador correspondiente
            if genero == "NB" and ((tecnologia == "ASP.NET" or tecnologia == "JS") and (edad >= 25 or edad <= 40) and puesto == "Ssr"):
                contador_genero_NB += 1

            else:
                # Si el puesto es "Jr" y es el primer "Jr" encontrado o tiene la edad más baja hasta el momento,
                # actualizar los datos del postulante más joven
                if puesto == "Jr" and (edad < edad_postulante_mas_chico or bandera == False):
                    edad_postulante_mas_chico = edad
                    nombre_postulante_mas_chico = nombre
                    bandera = True

            # Acumular edades y contar postulantes según su género
            if genero == "NB":
                acumulador_edades_NB += edad
                contador_edades_NB += 1
            else:
                if genero == "M":
                    acumulador_edades_M += edad
                    contador_edades_M += 1
                    contador_genero_M += 1

                else:
                    if genero == "F":
                        acumulador_edades_F += edad
                        contador_edades_F += 1
                        contador_genero_F += 1
                        
        # Calcular promedios de edades para ciertos grupos
        if contador_edades_NB == 0:
            promedio_NB = 0
        else:
            promedio_NB = acumulador_edades_NB / contador_edades_NB
            if contador_edades_M == 0:
                promedio_masculino = 0
            else:
                promedio_masculino = acumulador_edades_M / contador_edades_M
                if contador_edades_F == 0:
                    promedio_femenino = 0
                else:
                    promedio_femenino = acumulador_edades_F / contador_edades_F

            # Contar la cantidad de postulantes con cada tecnología
            if tecnologia == "PYTHON":
                contador_Python += 1
            else:
                if tecnologia == "JS":
                    contador_JS += 1
                else:
                    contador_asp_net += 1

            # Determinar la tecnología con más postulantes
            if contador_Python > contador_JS and contador_Python > contador_asp_net:
                tecnologia_postulantes_max = "PYTHON"
            else:
                if contador_JS > contador_asp_net:
                    tecnologia_postulantes_max = "JS"
                else:
                    tecnologia_postulantes_max = "ASP.NET"

        # Calcular porcentajes de postulantes por género
        porcentaje_NB = (contador_genero_NB * 100) / contador
        porcentaje_M = (contador_genero_M * 100) / contador
        porcentaje_F = (contador_genero_F * 100) / contador

        print(f'''
            la cantidad de postulantes NB son: {contador_genero_NB:.0f}
            nombre del postulante con menor edad: {nombre_postulante_mas_chico}
            el promedio de edad de genero NB: {promedio_NB:.0f}
            el pormedio de edad de genero masculino: {promedio_masculino:.0f}
            el promedio de edad de genero femenino: {promedio_femenino:.0f}
            la tecnologia con mas postulantes es: {tecnologia_postulantes_max}
            el porcentaje de postulantes de genero NB: {porcentaje_NB:.0f}%
            el porcentaje de postulantes de genero masculino: {porcentaje_M:.0f}%
            el porcentaje de postulantes de genero femenino: {porcentaje_F:.0f}%
            ''')


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
