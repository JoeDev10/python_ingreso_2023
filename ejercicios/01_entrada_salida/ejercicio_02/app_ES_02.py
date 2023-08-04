import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Joel
apellido: Rodriguez
---
Ejercicio: entrada_salida_02
---
Enunciado:
Al presionar el botón  'Mostrar', se deberá obtener un dato utilizando el Dialog Prompt
y luego mostrarlo utilizando el Dialog Alert
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        nombre_alumno = prompt("ingreso", "ingrese nombre del alumno")
        alert("titulo",f"el nombre del alumno es: {nombre_alumno}" )
        
        
        # nombre = "joel"
        # apellido = "rodriguez"
        # edad = "27"
        # mensaje = f"el nombre del alumno es: {nombre}\n el apellido es: {apellido}\n y la edad es: {edad} años"
        # alert("titulo", mensaje)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

    
    def btn_mostrar_todos_on_click(self):
        pass
    
    
    def btn_mostrar_informe_1(self):
        if len(self.lista_nombre_pokemones) > 0:
            poder_mas_bajo = 0
            bandera_primer_ingreso = False
            
            for i in range(len(self.lista_nombre_pokemones)):
                tipo = self.lista_tipo_pokemones[i]
                poder = self.lista_poder_pokemones[i]
                nombre = self.lista_nombre_pokemones[i]

                if tipo == "psíquico":
                    if bandera_primer_ingreso == False or poder < poder_mas_bajo:
                        poder_mas_bajo = poder
                        nombre_mas_debil = nombre
                        bandera_primer_ingreso = True
            
            print(f'''
                el nombre del pokemon psiquico mas debil es: {nombre_mas_debil}
                y su poder es: {poder_mas_bajo}
                ''')
        else:
            print("no se ingresaron datos")
    def btn_mostrar_informe_2(self):
    #? 4) - Porcentaje de pokemones de tipo agua con mas de 100 puntos de poder (Sobre el total de pokemones ingresados).
        
        contador_tipo_agua = 0
        
        for i in range(len(self.lista_nombre_pokemones)):
            tipo = self.lista_tipo_pokemones[i]
            poder = self.lista_poder_pokemones[i]
            
            if tipo == "agua" and poder > 100:
                contador_tipo_agua += 1
                
        porcentaje = (contador_tipo_agua * 100) / len(self.lista_poder_pokemones)
        
        print(porcentaje)
                

    #? 5) - Porcentaje de pokemones de tipo psiquico con poder de pelea inferior o igual a 150 (sobre el total de pokemones ingresados).

        contador_tipo_psiquico = 0
            
        for i in range(len(self.lista_nombre_pokemones)):
            tipo = self.lista_tipo_pokemones[i]
            poder = self.lista_poder_pokemones[i]
            
            if tipo == "psíquico":
                if poder <= 150:
                    contador_tipo_psiquico += 1
                    
        porcentaje = (contador_tipo_psiquico * 100) / len(self.lista_poder_pokemones)
        
        print(f"{porcentaje}%")
        
    #? 6) - tipo de los pokemones del tipo que mas pokemones posea. 

        contador_tipo_psiquico = 0
        contador_tipo_agua = 0
        contador_tipo_fuego = 0
        
        for i in range(len(self.lista_poder_pokemones)):
            tipo = self.lista_tipo_pokemones[i]
            
            if tipo == "psíquico":
                contador_tipo_psiquico += 1
            else:
                if tipo == "agua":
                    contador_tipo_agua += 1
                else:
                    contador_tipo_fuego += 1
                    
        if contador_tipo_psiquico > contador_tipo_agua and contador_tipo_psiquico > contador_tipo_fuego:
            mayor_tipo = "psíquico"
        else:
            if contador_tipo_agua > contador_tipo_fuego and contador_tipo_agua > contador_tipo_fuego:
                mayor_tipo = "agua"
            else:
                mayor_tipo = "fuego"
                
        print(f'''
            el tipo con mayor tipos es: {mayor_tipo}
            ''')
                    
        
    #? 7) - tipo de los pokemones del tipo que menos pokemones posea. 

        contador_tipo_psiquico = 0
        contador_tipo_agua = 0
        contador_tipo_fuego = 0
        
        for i in range(len(self.lista_poder_pokemones)):
            tipo = self.lista_tipo_pokemones[i]
            
            if tipo == "psíquico":
                contador_tipo_psiquico += 1
            else:
                if tipo == "agua":
                    contador_tipo_agua += 1
                else:
                    contador_tipo_fuego += 1
                    
        if contador_tipo_psiquico < contador_tipo_agua and contador_tipo_psiquico < contador_tipo_fuego:
            menor_tipo = "psíquico"
        else:
            if contador_tipo_agua < contador_tipo_fuego and contador_tipo_agua < contador_tipo_fuego:
                menor_tipo = "agua"
            else:
                menor_tipo = "fuego"
                
        print(f'''
            el tipo con menor tipos es: {menor_tipo}
            ''')
        
    #? 8) - Listado de todos los pokemones cuyo poder de pelea supere el valor promedio.

        acumulador_poderes = 0
        contador_poderes = 0
        
        for i in range(len(self.lista_nombre_pokemones)):
            poder = self.lista_poder_pokemones[i]
            acumulador_poderes += poder
            contador_poderes += 1
            
        promedio = acumulador_poderes / contador_poderes
        
        print("promedio", promedio)
        

        for i in range(len(self.lista_nombre_pokemones)):
            poder = self.lista_poder_pokemones[i]
            nombre = self.lista_nombre_pokemones[i]

            if poder > promedio: 
                poder_superior_promedio = poder
                nombre_superior_promedio = nombre
            
                print(f'''
                    el nombre del pokemon mas fuerte que el promedio es: {nombre_superior_promedio}
                    y su poder es: {poder_superior_promedio}
                    ''')
                
    #? 9) - el promedio de poder de todos los pokemones de tipo Psiquico.

            acumulador_poderes_psiquico = 0
            contador_poderes_psiquico = 0
            
        for i in range(len(self.lista_nombre_pokemones)):
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            
            if tipo == "psíquico":
                acumulador_poderes_psiquico += poder
                contador_poderes_psiquico += 1
                
        promedio_psiquico = acumulador_poderes_psiquico / contador_poderes_psiquico
        
        print(f'''
            el promedio de poderes de tipo psiquico es: {promedio_psiquico:.0f}
            ''')

    #? 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.

        bandera_primer_ingreso = False
        poder_mas_bajo = 0
        
        for i in range(len(self.lista_nombre_pokemones)):
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            
            if tipo == "psíquico":
                if poder < poder_mas_bajo or bandera_primer_ingreso == False:
                    poder_mas_bajo = poder
                    bandera_primer_ingreso = True
                    
        
        for i in range(len(self.lista_nombre_pokemones)):
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            nombre = self.lista_nombre_pokemones[i]
            
            if tipo == "psíquico" and poder == poder_mas_bajo:
                print(nombre, poder_mas_bajo)
            
        
        
    #? 1) - Cantidad de pokemones de tipo Psiquico cuyo poder de pelea con un 15% menos este entre los 100 y los 150 puntos.

        contador_tipo_psiquico = 0
        
        for i in range(len(self.lista_nombre_pokemones)):
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            poder_con_descuento = poder * 0.85
            
            if tipo == "psíquico":
                if poder_con_descuento > 100 and poder_con_descuento < 150:
                    contador_tipo_psiquico += 1
                    
        print(f"la cantidad de psiquicos con poder de pelea entre 100 y 150 es: {contador_tipo_psiquico}")
                    
        
        
    #? 0) - Cantidad de pokemones de tipo Fuego cuyo poder de pelea con un 10% extra supere los 100 puntos.

        contador_tipo_fuego = 0
        
        for i in range(len(self.lista_nombre_pokemones)):
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            poder_con_aumento = poder * 1.1
            
            if tipo == "fuego" and poder_con_aumento > 100:
                contador_tipo_fuego += 1
                
        print(f"la cantidad de tipo fuego con poder mayor a 100 es: {contador_tipo_fuego}")
        
    def btn_mostrar_informe_3(self):
        #? 2) - Nombre y Poder del pokemon de tipo Agua con el poder mas alto.

        bandera_primer_ingreso = False
        poder_mas_alto = 0
        
        for i in range(len(self.lista_tipo_pokemones)):
            # Obtenemos el poder y el tipo del Pokémon actual en la iteración.
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            
            # Si el tipo del Pokémon es "agua".
            if tipo == "agua":
            # Comprobamos si el poder es mayor al poder más alto encontrado hasta el momento
            # o si es el primer ingreso al bucle, en ese caso actualizamos el poder más alto.
                if poder > poder_mas_alto or bandera_primer_ingreso == False:
                    poder_mas_alto = poder
                    bandera_primer_ingreso = True
                    
        # Ahora que hemos encontrado el poder más alto para el tipo "agua",
        # recorremos nuevamente la lista para encontrar los Pokémon con ese poder y tipo.
        for i in range(len(self.lista_tipo_pokemones)):
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            nombre = self.lista_nombre_pokemones[i]
            
            # Si el tipo es "agua" y el poder es igual al poder más alto encontrado,
            # imprimimos el nombre del Pokémon y el poder más alto.
            if tipo == "agua" and poder == poder_mas_alto:
                print(nombre, poder_mas_alto)
                
                
        #? 3) - Nombre y Poder del pokemon de tipo Psiquico con el poder mas bajo.

        bandera_primer_ingreso = False
        poder_mas_bajo = 0
        
        for i in range(len(self.lista_nombre_pokemones)):
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            
            if tipo == "psíquico":
                if poder < poder_mas_bajo or bandera_primer_ingreso == False:
                    poder_mas_bajo = poder
                    bandera_primer_ingreso = True
                    
        
        for i in range(len(self.lista_nombre_pokemones)):
            poder = self.lista_poder_pokemones[i]
            tipo = self.lista_tipo_pokemones[i]
            nombre = self.lista_nombre_pokemones[i]
            
            if tipo == "psíquico" and poder == poder_mas_bajo:
                print(nombre, poder_mas_bajo)
        
        
                
    def btn_cargar_pokedex_on_click(self):
        pass