import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Enunciado:
Al presionar el botón ‘Mostrar Iteración’, mostrar mediante alert 
10 repeticiones con números ASCENDENTE desde el 1 al 10
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar_iteracion = customtkinter.CTkButton(
            master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(
            row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_iteracion_on_click(self):
        respuesta = True
        mayor_poder_de_pelea = 0
        bandera_primer_ingreso = False
        contador_guerreros_espartanos = 0
        acumulador_vikingos = 0
        contador_saiyayin = 0
        contador_general = 0
        
        while respuesta == True:

            nombre_guerrero = prompt(
                "utn", "ingrese nombre, las opciones son: leonidas, ragnar, geralt, goku")
            while len(nombre_guerrero) < 3:
                nombre_guerrero = prompt("error", "reingrese nombre")

            edad = prompt("edad", "ingrese edad")
            edad = int(edad)
            while edad < 18:
                edad = prompt("error", "reingrese edad")
                edad = int(edad)

            tipo_guerrero = prompt("guerrero", "ingrese tipo guerrero, las opciones son: espartano, vikingo, brujo o saiyayin")
            while tipo_guerrero != "espartano" and tipo_guerrero != "vikingo" and tipo_guerrero != "brujo" and tipo_guerrero != "saiyayin":
                tipo_guerrero = prompt("error", "reingrese nombre")

            poder_de_pelea = prompt("poder", "ingrese poder de pelea")
            poder_de_pelea = int(poder_de_pelea)
            while poder_de_pelea < 5000:
                poder_de_pelea = prompt(
                    "error", "incremente su poder de pelea y regrese, debilucho!")
                poder_de_pelea = int(poder_de_pelea)

            if poder_de_pelea > mayor_poder_de_pelea or bandera_primer_ingreso == False:
                mayor_poder_de_pelea = poder_de_pelea
                nombre_guerrero_mas_poderoso = nombre_guerrero
                bandera_primer_ingreso = True

            if tipo_guerrero == "espartano":
                contador_guerreros_espartanos += 1
            else:
                if tipo_guerrero == "vikingo":
                    acumulador_vikingos += 1
                else:
                    if tipo_guerrero == "saiyayin":
                        contador_saiyayin += 1

            contador_general += 1

            respuesta = question("mensaje", "desea continuar?")
            
        if acumulador_vikingos != 0:
            promedio_vikingos = acumulador_vikingos / contador_general
        else:
            promedio_vikingos = "no hubo guerreros vikingos"
            
        porcentaje_saiyayin = (contador_saiyayin * 100) / contador_general
        
        print(porcentaje_saiyayin)
        print(promedio_vikingos)
            

        alert("estadisticas", f'''
            el guerrero mas poderoso es {nombre_guerrero_mas_poderoso}
            la cantidad de guerreros espartanos es: {contador_guerreros_espartanos}
            el promedio de guerreros vikingos es: {promedio_vikingos:.0f}
            el porcentaje de guerreros saiyayin es: {porcentaje_saiyayin:.0f}
            ''')


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

    # respuesta = True
    # while respuesta == True:
    #     # ENTRADAS
    #     nombre = prompt("utn", "ingrese nombre")
    #     importe_ganado = prompt("utn", "ingrese importe")
    #     importe_ganado = float(importe_ganado)
    #     genero = prompt("utn", "ingrese genero")
    #     juego = prompt("utn", "ingrese juego")

    #     # PROCESOS
    #     while len(nombre) < 3:
    #         nombre = prompt("utn", "reingrese nombre")

    #     while importe_ganado <= 0:
    #         importe_ganado = prompt("utn", "reingrese importe")
    #         importe_ganado = float(importe_ganado)

    #     while genero != "masculino" and genero != "femenino" and genero != "otro":
    #         genero = prompt("utn", "reingrese genero")

    #     while juego != "ruleta" and juego != "poker" and juego != "tragamonedas":
    #         juego = prompt("utn", "reingrese juego")

    #     respuesta = question("utn", "desea continuar?")
    # end while

    # PROCESOS

    # SALIDAS
