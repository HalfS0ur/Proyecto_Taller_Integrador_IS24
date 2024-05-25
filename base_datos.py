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
                dato4 = columna['DATO4']
                dato5 = columna['DATO5']
                return(dato1, dato2, dato3, dato4, dato5)
            
    return None


def registro_existe():
    fecha = datetime.today().strftime('%Y-%m-%d')
    ruta = os.path.join('datos/registro_acceso', f"{fecha}.csv")
    
    if not os.path.exists(ruta):
        with open(ruta, 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['Hora', 'Número de placa', 'Ingreso'])
        return False
    else:
        return True
    
def placa_ya_registrada(ruta, numero_placa):
    if registro_existe():
        with open(ruta, 'r', newline='') as registro_acceso:
            reader = csv.reader(registro_acceso)
            ultimo_registro = None
            for row in reader:
                if row[1] == numero_placa:
                    registro_time = datetime.strptime(row[0], '%H:%M:%S')
                    if ultimo_registro is None or registro_time > ultimo_registro:
                        ultimo_registro = registro_time

            if ultimo_registro:
                tiempo_actual = datetime.strptime(datetime.now().strftime('%H:%M:%S'), '%H:%M:%S')
                print(tiempo_actual - ultimo_registro)
                if tiempo_actual - ultimo_registro < timedelta(minutes=1):
                    return True
    return False

def registrar_placas(numero_placa, ingreso):
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
                writer.writerow([datetime.now().strftime('%H:%M:%S'), numero_placa, ingreso])
            print('Datos registrados con éxito.')
    else:
        print('El número de placa es inválido.')
