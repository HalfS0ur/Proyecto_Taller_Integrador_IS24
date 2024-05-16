import csv

def placa_registrada(numero_placa):
    with open('datos/registro_interno/datos_internos.csv', 'r') as base_datos_internos:
        reader = csv.DictReader(base_datos_internos)
        for columna in reader:
            if columna ["PLACA"] == numero_placa:
                dato1 = columna['DATO1']
                dato2 = columna['DATO2']
                dato3 = columna['DATO3']
                extra = columna['EXTRA']

                return(dato1, dato2, dato3, extra)

    print ("Not bomboclat")