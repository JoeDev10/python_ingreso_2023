'''
#!BANDERAS!!!

bandera_votos_primer_ingreso = False           <- (#!INICIALIZAMOS BANDERA)
votos_mas_altos_max = 0                 <- (#!INICIALIZAMOS MAXIMOS Y MINIMOS EN 0)
votos_mas_bajos_min = 0

if votos_ingresados > votos_mas_altos or bandera_votos_primer_ingreso == False:
    votos_mas_altos = votos_ingresados
    nombre_candidato_mas_votado = nombre
                
            
if votos_ingresados < votos_mas_bajos or bandera_votos_primer_ingreso == False:
    votos_mas_bajos = votos_ingresados
    nombre_candidato_menos_votado = nombre
    edad_candidato_menos_votado = edad
    bandera_votos_primer_ingreso = True           <-  #!(CAMBIAMOS EL VALOR DE LA BANDERA A TRUE)
'''

# !PROMEDIOS!!!
'''
promedio = acumulador_edades / contador_edades

promedio = (producto1 + producto2 + producto3) / 3
'''

#!PORCENTAJES!!!
'''
porcentaje_tragamonedas = (contador_tragamonedas * 100) / contador_general     <- #?(codigo)
porcentaje =                      (parte *100)       /         total         <- #?(explicacion)
'''

# ! CALCULAR PRECIO TOTAL MAS EL IVA INCLUIDO
'''
suma_total_con_iva = suma_total * 1.21
'''

# ! CALCULA EL PRECIO DEL IVA SIN INCLUIR EL MONTO TOTAL
'''
precio_con_iva = precio_sin_iva + precio_sin_iva * 0.21


precio_sin_iva = 1000  # Monto de la compra sin incluir el IVA
tasa_iva = 0.21       # Tasa de IVA (21%)
precio_con_iva = precio_sin_iva + precio_sin_iva * tasa_iva
print("El precio total con IVA incluido es:", precio_con_iva)

'''

#! APLICAR DESCUENTOS
'''
poder_con_descuento = poder * 0.85
poder_con_aumento = poder * 1.1
'''

#! CARGAR UNA LISTA

'''
self.lista_nombres.append(estadisticas)     <- #?(codigo)  

(nombre de lista)          (variable)       <- #?(explicacion)
'''


#!MOSTRAR LA LISTA
'''
for i in range(len(self.lista_nombre_pokemones)):
    nombre = self.lista_nombre_pokemones[i]
    poder = self.lista_poder_pokemones[i]
    tipo = self.lista_tipo_pokemones[i]
    print(f"{i:10}-{nombre:15}{tipo:10}{poder:10}")
'''
