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
Al presionar el botón 'CARGAR' se le solicitarán tres números al usuario mediante el Dialog Prompt, los mismos deberán ser almacenados en un vector lista_datos. 
Al presionar el botón 'MOSTRAR', se deberán mostrar los números almacenados en el vector utilizando Dialog Alert para informar cada elemento.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

        self.btn_cargar = customtkinter.CTkButton(
            master=self, text="Cargar", command=self.btn_cargar_on_click)
        self.btn_cargar.grid(row=3, pady=10, columnspan=2, sticky="nsew")

        self.nombres = [
            "Juan", "María", "Luis", "Ana", "Carlos", "Jose", "Pedro", "Sofía", "Miguel", "Valentina",
            "Andrés", "Lucía", "Fernando", "Gabriela", "Diego", "Martina", "Jorge", "Camila", "Ricardo", "Isabella",
            "José", "Paula", "Manuel", "Alejandra", "Santiago", "Daniela", "Gustavo", "Carolina", "Emilio", "Antonella",
            "Pablo", "Valeria", "Eduardo", "Florencia", "Alberto", "Agustina", "Raul", "Rocio", "Javier", "Marina",
            "Sebastian", "Catalina", "Rafael", "Carmen", "Rodrigo", "Elena", "Oscar", "Pilar", "Hugo", "Juana",   "Guillermo", "Natalia", "Francisco", "Constanza", "Hector", "Adriana", "Victor", "Anita", "Lorenzo", "Estela",
            "Enrique", "Diana", "Fabian", "Patricia", "Felipe", "Claudia", "Camilo", "Teresa", "Samuel", "Rosa",
            "Joaquin", "Monica", "Lucas", "Ines", "Omar", "Gloria", "Mariano", "Silvia", "Nicolas", "Alicia",
            "Federico", "Olga", "Arturo", "Amparo", "Julio", "Elsa", "Alfredo", "Beatriz", "Elias", "Rita",
            "Benjamin", "Margarita", "Agustin", "Dolores", "Dario", "Lourdes", "Gerardo", "Manuela", "Feliciano", "Marta"
        ]

        self.edades = [
            25, 33, 20, 29, 50, 40, 22, 28, 35, 18,
            26, 21, 30, 32, 19, 27, 24, 38, 31, 23,
            29, 17, 28, 34, 20, 25, 22, 33, 40, 16,
            19, 37, 24, 28, 31, 21, 33, 18, 29, 26,
            35, 20, 23, 39, 30, 27, 22, 36, 28, 32,
            31, 19, 24, 20, 25, 33, 40, 27, 21, 39,
            29, 22, 36, 30, 19, 25, 21, 38, 34, 17,
            32, 18, 23, 27, 22, 40, 36, 29, 20, 33,
            31, 35, 24, 19, 28, 30, 26, 37, 33, 21,
            25, 29, 16, 38, 40, 50, 27, 30, 32, 24
        ]

        self.generos = [
            "Masculino", "Femenino", "Masculino", "Femenino", "Otro", "Masculino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
            "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino"
        ]

        self.tipo_entrada = [
            "General", "Campo delantero", "Platea", "General", "Platea", "General", "General", "Platea", "Campo delantero", "General",
            "Campo delantero", "Platea", "General", "General", "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea",
            "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
            "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "General", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
            "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea",
            "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero", "General", "Platea", "Campo delantero",
            "Campo delantero", "Platea", "Platea", "Campo delantero", "General", "Platea", "Campo delantero"
        ]

        self.medio_pago = [
            "Credito", "Debito", "Efectivo", "Credito", "Efectivo", "Debito", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito",
            "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito",
            "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo",
            "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito", "Debito", "Efectivo", "Credito"
        ]

        self.lista_precios = [16000, 30000, 25000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
                            25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
                            30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
                            16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
                            25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
                            30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
                            16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000,
                            25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000,
                            30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000,
                            16000, 25000, 30000, 16000, 25000, 30000, 16000, 25000, 30000, 16000
                            ]

    def btn_mostrar_on_click(self):
    #* Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo delantero".
        contador_masculino = 0
        contador_femenino = 0
        
        for i in range(len(self.tipo_entrada)):
            tipo_entrada = self.tipo_entrada[i]
            genero = self.generos[i]
            if tipo_entrada == "Campo delantero" and genero == "Masculino":
                contador_masculino += 1
            else:
                if tipo_entrada == "Campo delantero" and genero == "Femenino":
                    contador_femenino += 1
                    
        if contador_masculino > contador_femenino:
            genero_mas_frecuente_campo = "Masculino"
        else:
            genero_mas_frecuente_campo = "Femenino"
        
        print(genero_mas_frecuente_campo)

    #* Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
        contador_personas_credito = 0
        acumulador_edad = 0
        
        for i in range(len(self.tipo_entrada)):
            tipo_entrada = self.tipo_entrada[i]
            medio_pago = self.medio_pago[i]
            edad = self.edades[i]
            
            if tipo_entrada == "General" and medio_pago == "Credito":
                contador_personas_credito += 1
                acumulador_edad += edad
                
        promedio_edad = acumulador_edad / contador_personas_credito
        print(f'''
            la cantidad de personas que pagaron con credito son: {contador_personas_credito}
            y el promedio de edades es: {promedio_edad:.0f}
            ''')

        #* Calcula el número total de entradas compradas por personas mayores de 30 años y su precio promedio.
        contador_entradas_mayores_treinta = 0
        acumulador_precios = 0

        for i in range(len(self.lista_precios)):
            tipo_entrada = self.tipo_entrada[i]
            edad = self.edades[i]
            precios = self.lista_precios[i]
            
            if edad > 30:
                contador_entradas_mayores_treinta += 1
                acumulador_precios += precios
                
            
        promedio_precios = acumulador_precios / contador_entradas_mayores_treinta
        
        print(f'''
            el total de entradas compradas por personas mayores de 30 años es: {contador_entradas_mayores_treinta}
            y su precio promedio: {promedio_precios:.0f}
            ''')
            
        #*Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito respecto al total de personas en la lista.

        contador_platea_debito = 0
        
        for i in range(len(self.tipo_entrada)):
            tipo_entrada = self.tipo_entrada[i]
            medio_pago = self.medio_pago[i]
            
            if tipo_entrada == "Platea" and medio_pago == "Debito":
                contador_platea_debito += 1
                
        porcentaje = (contador_platea_debito * 100) / len(self.nombres)
        
        print(f'''
            el porcentaje de personas en platea que pagaron con debito es: {porcentaje:.0f}%
            ''')
        
        
        # !Cantidad total de dinero recaudado por las ventas de entradas.

        
        
    def btn_cargar_on_click(self):
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

    # una sola lista: for medio in self.medio_pago
    # dos o mas listas: for i in range(self.medio_pago)

    '''
    Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo delantero".
    Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
    Calcula el número total de entradas compradas por personas mayores de 30 años y su precio promedio.
    Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito respecto al total de personas en la lista.
    Cuál es el total de descuentos en pesos que aplicó la empresa.
    Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito.
    Encuentra los nombres y las edades de la personas que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito.
    Encuentra la cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
    Calcula el monto total recaudado por la venta de entradas de tipo "General" y pagadas con tarjeta de crédito por personas cuyas edades son múltiplos de 5.

    '''

    '''
    Al finalizar la venta de entradas, los organizadores quieren obtener la siguiente información:
Cantidad total de dinero recaudado por las ventas de entradas.
Cantidad de entradas vendidas para cada tipo.
Promedio de edad de las personas que compraron ubicación en Platea.
Nombre de la persona de mayor edad que compró una entrada de platea.
Porcentaje de entradas vendidas de tipo "general"
Nombre de la/s persona/s de mayor edad, de género Masculino que compro una entrada general.
Tipo de entradas más vendidas
    '''


        # # !Cantidad total de dinero recaudado por las ventas de entradas.
        # # punto A

        # acumulador_dinero_recaudado = 0

        # for i in range(len(self.lista_precios)):
        #     acumulador_dinero_recaudado += self.lista_precios[i]

        # print(acumulador_dinero_recaudado)

        # # *Cantidad de entradas vendidas para cada tipo.
        # # punto B

        # contador_entradas_tipo_general = 0
        # contador_entradas_campo = 0
        # contador_entradas_platea = 0

        # for i in range(len(self.tipo_entrada)):
        #     if self.tipo_entrada[i] == "General":
        #         contador_entradas_tipo_general += 1
        #     else:
        #         if self.tipo_entrada[i] == "Campo delantero":
        #             contador_entradas_campo += 1
        #         else:
        #             contador_entradas_platea += 1
        # print(f'''
        #     la cantidad de entradas vendidas para cada tipo son:
        #     general: {contador_entradas_tipo_general}
        #     campo delantero: {contador_entradas_campo}
        #     platea: {contador_entradas_platea}
        #     ''')

        # # !Promedio de edad de las personas que compraron ubicación en Platea.
        # # punto C

        # acumulador_edades_platea = 0
        # contador_edades_platea = 0

        # for i in range(len(self.edades)):
        #     if self.tipo_entrada[i] == "Platea":
        #         acumulador_edades_platea += self.edades[i]
        #         contador_edades_platea += 1

        # if contador_edades_platea != 0:
        #     promedio = acumulador_edades_platea / contador_edades_platea
        # else:
        #     print("no hubo entradas vendidas en platea")

        # print(
        #     f"el promedio de edades de las personas que compraron ubicacion platea es: {promedio:.0f}")

        # # !Nombre de la persona de mayor edad que compró una entrada de platea.
        # # punto D

        # persona_mayor_en_platea = 0
        # bandera = False

        # for i in range(len(self.edades)):
        #     if ((self.edades[i] > persona_mayor_en_platea or bandera == False) and self.tipo_entrada[i] == "Platea"):
        #         nombre_mayor_en_platea = self.nombres[i]
        #         entrada_mayor_platea = self.tipo_entrada[i]
        #         bandera = True
        # print(f"la persona mayor en platea: {nombre_mayor_en_platea}")

        # # !Porcentaje de entradas vendidas de tipo "general"
        # # punto E

        # acumulador_entradas_tipo_general = 0

        # for i in range(len(self.tipo_entrada)):
        #     if self.tipo_entrada[i] == "General":
        #         acumulador_entradas_tipo_general += 1

        # porcentaje_tipo_general = ( acumulador_entradas_tipo_general * 100) / 100

        # print(
        #     f"el porcentaje de entradas vendidas de tipo general es: {porcentaje_tipo_general:.2f}%")

        # # !Nombre de la/s persona/s de mayor edad, de género Masculino que compro una entrada general.
        # # punto F

        # nombre_mayor_edad = None
        # edad_mayor = 0

        # for i in range(len(self.nombres)):
        #     if self.generos[i] == "Masculino" and self.tipo_entrada[i] == "General":
        #         if self.edades[i] > edad_mayor:
        #             nombre_mayor_edad = self.nombres[i]
        #             edad_mayor = self.edades[i]

        # if nombre_mayor_edad:
        #     print(
        #         f"la persona de mayor edad, de genero masculino que compro entrada general es: {nombre_mayor_edad}")
        # else:
        #     print(
        #         "No se encontró ninguna persona de género masculino que haya comprado una entrada general.")

        # # !Tipo de entradas más vendidas
        # # punto G

        # for i in range(len(self.tipo_entrada)):
        #     if self.tipo_entrada[i] == "General":
        #         contador_entradas_tipo_general += 1
        #     else:
        #         if self.tipo_entrada[i] == "Campo delantero":
        #             contador_entradas_campo += 1
        #         else:
        #             contador_entradas_platea += 1

        #     if contador_entradas_tipo_general > contador_entradas_campo and contador_entradas_tipo_general > contador_entradas_platea:
        #         entrada_mas_vendida = "General"
        #     else:
        #         if contador_entradas_campo > contador_entradas_platea:
        #             entrada_mas_vendida = "Campo delantero"
        #         else:
        #             entrada_mas_vendida = "Platea"

        # print(f"la entrada mas vendida es: {entrada_mas_vendida}")

        # ############################################################# primera_parte! ################################

        # # * Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo delantero".
        # # punto 1
        # contador_masculinos = 0
        # contador_femeninos = 0
        # genero_mas_frecuente_campo = 0

        # for i in range(len(self.generos)):
        #     if self.generos[i] == "Masculino" and self.tipo_entrada == "Campo delantero":
        #         contador_masculinos += 1
        #     else:
        #         if self.generos[i] == "Femenino" and self.tipo_entrada[i] == "Campo delantero":
        #             contador_femeninos += 1

        # if contador_masculinos > contador_femeninos:
        #     genero_mas_frecuente_campo = "Masculino"
        # else:
        #     genero_mas_frecuente_campo = "Femenino"

        # print(f"el genero  mas frecuente es: {genero_mas_frecuente_campo}")

        # # * Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.

        # acumulador_edades_credito = 0
        # contador_edades_credito = 0
        # contador_personas_credito = 0

        # for i in range(len(self.tipo_entrada)):
        #     if self.tipo_entrada[i] == "General" and self.medio_pago[i] == "Credito":
        #         acumulador_edades_credito += self.edades[i]
        #         contador_edades_credito += 1
        #         contador_personas_credito += 1

        # if contador_edades_credito != 0:
        #     promedio_edades_credito = acumulador_edades_credito / contador_edades_credito
        # else:
        #     promedio_edades_credito = "no hubo personas que pagaron con tarjeta"

        # print("utn"f'''
        #     la cantidad de personas que compraron entradas de tipo general y pagaron con credito son: {contador_personas_credito}
        #     y su edad promedio es {promedio_edades_credito:.0f}
        #     ''')

        # # * Calcula el número total de entradas compradas por personas mayores de 30 años y su precio promedio.

        # contador_entradas_totales = 0
        # acumulador_precios_totales = 0

        # for i in range(len(self.tipo_entrada)):
        #     if self.edades[i] > 30:
        #         acumulador_precios_totales += self.lista_precios[i]
        #         contador_entradas_totales += 1

        # if acumulador_precios_totales != 0:
        #     promedio_entradas_totales = acumulador_precios_totales / contador_entradas_totales
        # else:
        #     promedio_entradas_totales = "no hubo entradas para mayores de 30 años"

        # print(f'''
        #     el numero total de entradas compradas por personas mayores a 30 años es: {contador_entradas_totales}
        #     y el promedio de precios es: {promedio_entradas_totales:.0f}
        #     ''')
        
        # #* Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito respecto al total de personas en la lista.

        # contador_personas_debito = 0
        
        # for i in range(len(self.tipo_entrada)):
        #     if self.tipo_entrada[i] == "Platea" and self.medio_pago[i] == "Debito":
        #         contador_personas_debito += 1
                
        # porcentaje_personas_debito = (contador_personas_credito * 100) / 100
        # print(f"el porcentaje de personas que compraron en platea y pagaron con debito es: {porcentaje_personas_debito:.0f}%")
        
        # # *Encuentra la cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
        
        # #a resolver...
        
        
        # #* Calcula el monto total recaudado por la venta de entradas de tipo "General" y pagadas con tarjeta de crédito por personas cuyas edades son múltiplos de 5.

        # acumulador_dinero_tipo_general = 0
        
        # for i in range(len(self.tipo_entrada)):
        #     if self.tipo_entrada[i] == "General" and self.medio_pago[i] == "Credito":
        #         if self.edades[i] % 5 == 0:
        #             acumulador_dinero_tipo_general += self.lista_precios[i]
                    
        # print(f"el dinero recaudado en tipo general es: {acumulador_dinero_tipo_general}")
                    
                