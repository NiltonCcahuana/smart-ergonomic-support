class Estudiante:
    def __init__(self, estatura_m, horas_uso, dolor_cervical):
        self.estatura_m = estatura_m
        self.horas_uso = horas_uso
        self.dolor_cervical = dolor_cervical


class AnalizadorErgonomico:
    def __init__(self, estudiante):
        self.estudiante = estudiante

    def calcular_riesgo(self):
        riesgo = 0

        if self.estudiante.horas_uso >= 6:
            riesgo += 2
        elif self.estudiante.horas_uso >= 3:
            riesgo += 1

        if self.estudiante.dolor_cervical:
            riesgo += 2

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
    def generar(self, estudiante, riesgo, elevacion, inclinacion):
        print("=== REPORTE ERGONÓMICO ===")
        print("Estatura:", estudiante.estatura_m)
        print("Horas de uso:", estudiante.horas_uso)
        print("Riesgo:", riesgo)
        print("Elevación recomendada:", elevacion)
        print("Inclinación recomendada:", inclinacion)


estudiante = Estudiante(1.72, 6, True)

analizador = AnalizadorErgonomico(estudiante)
riesgo = analizador.clasificar_riesgo()

soporte = SoporteErgonomico()
elevacion, inclinacion = soporte.recomendar_ajuste(estudiante)

reporte = Reporte()
reporte.generar(estudiante, riesgo, elevacion, inclinacion)