"""
Este programa es una calculadora de impuestos sencilla que utiliza una interfaz gráfica creada con CustomTkinter.

Uso:
- Ejecuta el programa.
- Introduce tus ingresos y el porcentaje de impuesto.
- El programa calculará y mostrará el total de impuestos a pagar.

¡Disfruta calculando tus impuestos de manera fácil y rápida!
"""

import customtkinter as ctk

# Definimos la clase CalculadoraImpuestos
class CalculadoraImpuestos:
    def __init__(self):
        # Inicializamos nuestra ventana
        self.ventana = ctk.CTk()
        self.ventana.title('Calculadora de Impuestos')
        self.ventana.geometry('280x200')
        self.ventana.resizable(False, False)

        # Espaciado para los widgets
        self.espaciado: dict = {'padx': 20, 'pady': 10}

        # Etiqueta y entrada para los ingresos
        self.etiqueta_ingresos = ctk.CTkLabel(self.ventana, text='Ingresos:')
        self.etiqueta_ingresos.grid(row=0, column=0, **self.espaciado)
        self.entrada_ingresos = ctk.CTkEntry(self.ventana)
        self.entrada_ingresos.grid(row=0, column=1, **self.espaciado)

        # Etiqueta y entrada para el porcentaje de impuesto
        self.etiqueta_impuesto = ctk.CTkLabel(self.ventana, text='Porcentaje:')
        self.etiqueta_impuesto.grid(row=1, column=0, **self.espaciado)
        self.entrada_impuesto = ctk.CTkEntry(self.ventana)
        self.entrada_impuesto.grid(row=1, column=1, **self.espaciado)

        # Etiqueta y entrada para el resultado
        self.etiqueta_resultado = ctk.CTkLabel(self.ventana, text='Impuesto:')
        self.etiqueta_resultado.grid(row=2, column=0, **self.espaciado)
        self.entrada_resultado = ctk.CTkEntry(self.ventana)
        self.entrada_resultado.insert(0, '0')
        self.entrada_resultado.grid(row=2, column=1, **self.espaciado)

        # Botón para calcular
        self.boton_calcular = ctk.CTkButton(self.ventana, text='Calcular', command=self.calcular_impuesto)
        self.boton_calcular.grid(row=3, column=1, **self.espaciado)

    def actualizar_resultado(self, texto: str):
        """Actualiza el campo del resultado del impuesto."""

        self.entrada_resultado.delete(0, ctk.END)
        self.entrada_resultado.insert(0, texto)

    def calcular_impuesto(self):
        """Calcula el impuesto total basado en el porcentaje ingresado."""

        try:
            ingresos: float = float(self.entrada_ingresos.get())
            porcentaje_impuesto: float = float(self.entrada_impuesto.get())
            # Calculamos el impuesto y actualizamos el resultado
            self.actualizar_resultado(f'₡{ingresos * (porcentaje_impuesto / 100):,.2f}')
        except ValueError:
            # Si la entrada no es válida, mostramos un mensaje de error
            self.actualizar_resultado('Entrada inválida')

    def ejecutar(self):
        """Ejecuta la aplicación tkinter."""

        self.ventana.mainloop()


if __name__ == '__main__':
    calculadora = CalculadoraImpuestos()
    calculadora.ejecutar()
