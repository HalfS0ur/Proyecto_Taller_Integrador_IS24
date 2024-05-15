import easyocr
import string

reader = easyocr.Reader(['es'], gpu=True) #Configura el lector de imagenes (configurar gpu de acuerdo al caso)

lista_numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

diccionario_num_car = {
    '2' : 'Z',
    '3' : 'J',
    '5' : 'S',
    '6' : 'G',
    '8' : 'B',
}

diccionario_car_num = {
    'O' : '0',
    'I' : '1',
    'Z' : '2',
    'J' : '3',
    'A' : '4',
    'S' : '5',
    'G' : '6',
    'B' : '8',
}

diccionario_simbolos = {
    '-' : '-'
}

def verificar_formato_placa_alfanumerica(numero_placa):
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
    
def verificar_formato_placas_especiales(numero_placa):
    #TODO
    return 0

def verificar_formato_placas_numericas(numero_placa):
    if len(numero_placa) > 6:
        return False
    
    for caracter in numero_placa:
        if (caracter in lista_numeros or caracter in diccionario_num_car.keys()):
            return True
        else:
            return False
        
def dar_formato_alfanumerico(numero_placa):
    placa_ = ''
    mapeo = {0:diccionario_num_car, 1:diccionario_num_car, 2:diccionario_num_car, 3:diccionario_simbolos, 4:diccionario_car_num, 5:diccionario_car_num, 6:diccionario_car_num}
    for t in [0, 1, 2, 3, 4, 5, 6]:
        if numero_placa[t] in mapeo[t].keys():
            placa_ += mapeo[t][numero_placa[t]]
        else:
            placa_ += numero_placa[t]

    return placa_



def deteccion_de_texto(imagen_placa):
    numero_placa = None
    info_deteccion = reader.readtext(imagen_placa)

    if info_deteccion:
        if info_deteccion[0][2] >= 0.9: #Bejó de 0.9
            numero_placa = info_deteccion[0][1]
            print(numero_placa)

            if ('-') in numero_placa and (len(numero_placa)) == 7 and verificar_formato_placa_alfanumerica(numero_placa):
                return dar_formato_alfanumerico(numero_placa)

            elif ('-') in numero_placa and (len(numero_placa)) != 7:
                verificar_formato_placas_especiales(numero_placa)

            elif verificar_formato_placas_numericas(numero_placa):
                return numero_placa
    else:
        return None