import csv
import os
from datetime import datetime, timedelta

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
    ruta = os.path.join('datos/registro_acceso', f"{fecha}.csv")
    
    if not os.path.exists(ruta):
        with open(ruta, 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['Hora', 'Número de placa', 'Confianza'])
        return False
    else:
        return True
    
def placa_ya_registrada(ruta, numero_placa):
    if registro_existe():
        with open(ruta, 'r', newline='') as registro_acceso:
            reader = csv.reader(registro_acceso)
            for row in reader:
                if row[1] == numero_placa:
                    registro_time = datetime.strptime(row[0], '%H:%M:%S')
                    if datetime.now() - registro_time > timedelta(minutes=1):
                        return True
                    else:
                        return False
    return False

def registrar_placas(numero_placa, confianza):
    fecha = datetime.today().strftime('%Y-%m-%d')
    ruta = os.path.join('datos/registro_acceso', f"{fecha}.csv")

    if numero_placa is not None:
        if placa_ya_registrada(ruta, numero_placa):
            print('La placa ya ha sido registrada anteriormente.')
        else:
            if registro_existe():
                mode = 'a'
            else:
                mode = 'w'
                print('Archivo creado.')

            with open(ruta, mode, newline='') as registro_acceso:
                writer = csv.writer(registro_acceso)
                writer.writerow([datetime.now().strftime('%H:%M:%S'), numero_placa, confianza])
            print('Datos registrados con éxito.')
    else:
        print('El número de placa es inválido.')
