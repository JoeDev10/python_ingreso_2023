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
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=[
                                                        "ArgentinaLuz", "FelipeLamparas", "JeLuz", "HazIluminacion", "Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(
            master=self, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)

        self.btn_calcular = customtkinter.CTkButton(
            master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        lamparita_precio_base = 800
        descuento = 0

        marca_lamparita = self.combobox_marca.get()
        cantidad_lamparitas = self.combobox_cantidad.get()
        cantidad_lamparitas = int(cantidad_lamparitas)
        
        if  cantidad_lamparitas >= 6:
            descuento = 0.5
            importe_final = lamparita_precio_base * (1 - descuento)
            importe_total = importe_final * cantidad_lamparitas
            alert("mensaje", f"el precio final es: {importe_total:.0f}")
        elif marca_lamparita == "ArgentinaLuz" and cantidad_lamparitas == 5:
            descuento = 0.4
            importe_final = lamparita_precio_base * (1 - descuento)
            importe_total = importe_final * cantidad_lamparitas
            alert("mensaje", f"el precio final es: {importe_total:.0f}")
        elif marca_lamparita != "ArgentinaLuz" and cantidad_lamparitas == 5:
            descuento = 0.3
            importe_final = lamparita_precio_base * (1 - descuento)
            importe_total = importe_final * cantidad_lamparitas
            alert("mensaje", f"el importe precio final es: {importe_total:.0f}")
        elif cantidad_lamparitas == 4 and marca_lamparita == "ArgentinaLuz" or "FelipeLamparas":
            descuento = 0.25
            importe_final = lamparita_precio_base * (1 - descuento)
            importe_total = importe_final * cantidad_lamparitas
            alert("mensaje", f"el precio final es: {importe_total:.0f}")
        elif cantidad_lamparitas == 3 and marca_lamparita == "ArgentinaLuz":
            descuento = 0.15
            importe_final = lamparita_precio_base * (1 - descuento)
            importe_total = importe_final * cantidad_lamparitas
            alert("mensaje", f"el precio final es: {importe_total:.0f}")
        elif cantidad_lamparitas == 3 and marca_lamparita == "FelipeLamparas":
            descuento = 0.10
            importe_final = lamparita_precio_base * (1 - descuento)
            importe_total = importe_final * cantidad_lamparitas
            alert("mensaje", f"el precio final es: {importe_total:.0f}")
        else:
            descuento = 0.05
            importe_final = lamparita_precio_base * (1 - descuento)
            importe_total = importe_final * cantidad_lamparitas
            alert("mensaje", f"el precio final es: {importe_total:.0f}")
        if importe_total > 4000:
            descuento += 0.05
            importe_final = lamparita_precio_base * (1 - descuento)
            importe_total = importe_final * cantidad_lamparitas
            alert("mensaje", f"el precio final es: {importe_total:.0f}")
        


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
