import easyocr
import string

reader = easyocr.Reader(['es'], gpu=True) #Configura el lector de imagenes (configurar gpu de acuerdo al caso)

lista_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

diccionario_num_car = {
    '0' : 'O',
    '1' : 'I',
    '2' : 'Z',
    '3' : 'J',
    '4' : 'A',
    '5' : 'S',
    '6' : 'G',
    '7' : '',
    '8' : 'B',
    '9' : ''
}

diccionario_car_num = {
    'O' : '0',
    'I' : '1',
    'Z' : '2',
    'J' : '3',
    'A' : '4',
    'S' : '5',
    'G' : '6',
    '' : '7',
    'B' : '8',
    '' : '9'
}

def formato_placa_alfanumerica(numero_placa):
    if (len(numero_placa) != 7):
        return False
    
    if (numero_placa[0] in string.ascii_uppercase or numero_placa[0] in diccionario_car_num.keys() and \
        numero_placa[1] in string.ascii_uppercase or numero_placa[1] in diccionario_car_num.keys() and \
        numero_placa[2] in string.ascii_uppercase or numero_placa[2] in diccionario_car_num.keys() and \
        numero_placa[3] == '-'                                                                     and \
        numero_placa[4] in lista_numeros or numero_placa[4] in diccionario_num_car.keys()          and \
        numero_placa[5] in lista_numeros or numero_placa[5] in diccionario_num_car.keys()          and \
        numero_placa[6] in lista_numeros or numero_placa[6] in diccionario_num_car.keys()):
        return True

    else:
        return False 
    
def formato_placas_especiales(numero_placa):
    #TODO
    return 0

def formato_placas_numericas(numero_placa):
    return 0

def deteccion_de_texto(imagen_placa):
    numero_placa = None
    info_deteccion = reader.readtext(imagen_placa)

    if info_deteccion:
        if info_deteccion[0][2] >= 0.9:
            numero_placa = info_deteccion[0][1]

            if ('-') in numero_placa and (len(numero_placa)) == 7:
                formato_placa_alfanumerica(numero_placa)

            elif ('-') in numero_placa and (len(numero_placa)) != 7:
                formato_placas_especiales(numero_placa)

            return numero_placa

    else:
        return numero_placa