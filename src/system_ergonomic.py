import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


class Estudiante:
    def __init__(self, nombre, estatura_m, horas_uso, dolor_cervical):
        self.nombre = nombre
        self.estatura_m = estatura_m
        self.horas_uso = horas_uso
        self.dolor_cervical = dolor_cervical


class AnalizadorErgonomico:
    def __init__(self, estudiante):
        self.estudiante = estudiante

    def calcular_riesgo(self):
        riesgo = 0

        # Horas de uso
        if self.estudiante.horas_uso >= 6:
            riesgo += 2
        elif self.estudiante.horas_uso >= 3:
            riesgo += 1

        # Dolor cervical
        if self.estudiante.dolor_cervical:
            riesgo += 2

        # Estatura
        if self.estudiante.estatura_m < 1.60 or self.estudiante.estatura_m > 1.85:
            riesgo += 1

        return riesgo

    def clasificar_riesgo(self):
        riesgo = self.calcular_riesgo()

        if riesgo <= 1:
            return "BAJO"
        elif riesgo <= 3:
            return "MEDIO"
        else:
            return "ALTO"


class SoporteErgonomico:
    def recomendar_ajuste(self, estudiante):

        if estudiante.estatura_m >= 1.80:
            elevacion = 10
        elif estudiante.estatura_m >= 1.65:
            elevacion = 6
        else:
            elevacion = 3

        inclinacion = 20 if estudiante.horas_uso >= 5 else 15

        return elevacion, inclinacion


class Reporte:

    @staticmethod
    def mostrar(estudiante, riesgo, elevacion, inclinacion):

        print("\n")
        print("=" * 45)
        print("      REPORTE ERGONÓMICO")
        print("=" * 45)
        print(f"Nombre                 : {estudiante.nombre}")
        print(f"Estatura               : {estudiante.estatura_m:.2f} m")
        print(f"Horas de uso           : {estudiante.horas_uso}")
        print(f"Dolor cervical         : {estudiante.dolor_cervical}")
        print(f"Nivel de riesgo        : {riesgo}")
        print(f"Elevación recomendada  : {elevacion} cm")
        print(f"Inclinación recomendada: {inclinacion}°")
        print("=" * 45)

    @staticmethod
    def guardar_csv(estudiante, riesgo, elevacion, inclinacion):

        datos = {
            "Fecha": [datetime.now()],
            "Nombre": [estudiante.nombre],
            "Estatura_m": [estudiante.estatura_m],
            "Horas_uso": [estudiante.horas_uso],
            "Dolor_cervical": [estudiante.dolor_cervical],
            "Riesgo": [riesgo],
            "Elevacion_cm": [elevacion],
            "Inclinacion_grados": [inclinacion],
        }

        df = pd.DataFrame(datos)

        try:
            historial = pd.read_csv("reporte_ergonomico.csv")
            historial = pd.concat([historial, df], ignore_index=True)
            historial.to_csv("reporte_ergonomico.csv", index=False)
        except FileNotFoundError:
            df.to_csv("reporte_ergonomico.csv", index=False)

        print("\nReporte guardado en reporte_ergonomico.csv")

    @staticmethod
    def graficar(estudiante, elevacion, inclinacion):

        variables = [
            "Estatura\n(cm)",
            "Horas\nuso",
            "Elevación\n(cm)",
            "Inclinación\n(°)"
        ]

        valores = [
            estudiante.estatura_m * 100,
            estudiante.horas_uso,
            elevacion,
            inclinacion
        ]

        fig, ax = plt.subplots(figsize=(8, 5))

        barras = ax.bar(variables, valores)

        ax.set_title("Parámetros Ergonómicos")
        ax.set_ylabel("Valor")

        for barra in barras:
            altura = barra.get_height()
            ax.text(
                barra.get_x() + barra.get_width()/2,
                altura,
                f'{altura:.1f}',
                ha='center',
                va='bottom'
            )

        plt.tight_layout()
        plt.show()


# ==========================
# PROGRAMA PRINCIPAL
# ==========================

print("=" * 50)
print(" SISTEMA DE SOPORTE ERGONÓMICO INTELIGENTE")
print("=" * 50)

nombre = input("Ingrese nombre del usuario: ")
estatura = float(input("Ingrese estatura (m): "))
horas = int(input("Ingrese horas de uso diario: "))

dolor = input(
    "¿Presenta dolor cervical? (s/n): "
).strip().lower()

dolor = dolor == "s"

# Objeto usuario
estudiante = Estudiante(
    nombre,
    estatura,
    horas,
    dolor
)

# Análisis
analizador = AnalizadorErgonomico(estudiante)
riesgo = analizador.clasificar_riesgo()

# Recomendación
soporte = SoporteErgonomico()
elevacion, inclinacion = soporte.recomendar_ajuste(estudiante)

# Reporte
Reporte.mostrar(
    estudiante,
    riesgo,
    elevacion,
    inclinacion
)

# Exportación
Reporte.guardar_csv(
    estudiante,
    riesgo,
    elevacion,
    inclinacion
)

# Dashboard
Reporte.graficar(
    estudiante,
    elevacion,
    inclinacion
)