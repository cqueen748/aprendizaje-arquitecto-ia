paginas_totales = 150
paginas_procesadas = 75

if paginas_totales > 0:
    porcentaje_avance = paginas_procesadas / paginas_totales * 100
    print("Porcentaje de avance:", porcentaje_avance, "%")
else:
    print("El total de paginas debe ser mayor que cero.")