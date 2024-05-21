import csv
import os
from datetime import datetime

def placa_registrada(numero_placa):
    with open('datos/registro_interno/datos_internos.csv', 'r') as base_datos_internos:
        reader = csv.DictReader(base_datos_internos)
        for columna in reader:
            if columna ["PLACA"] == numero_placa:
                dato1 = columna['DATO1']
                dato2 = columna['DATO2']
                dato3 = columna['DATO3']
                color = columna['COLOR']
                extra = columna['EXTRA']
                return(dato1, dato2, dato3, color, extra)
            
    return None

def registro_existe():
    fecha = datetime.today().strftime('%Y-%m-%d')
    archivos = os.listdir('datos/registro_acceso/')
    nombre_archivo = f"{fecha}.csv"
    ruta = os.path.join('datos/registro_acceso/',f"{fecha}.csv")

    if not os.path.exists(ruta):
        with open(ruta, 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['Hora', 'Número de placa', 'Confianza'])
            pass
        return True
    else:
        return False