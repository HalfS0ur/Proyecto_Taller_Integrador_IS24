import easyocr

reader = easyocr.Reader(['es'], gpu=True) #Configura el lector de imagenes (configurar gpu de acuerdo al caso)

def deteccion_de_texto(imagen_placa):
    numero_placa = None
    info_deteccion = reader.readtext(imagen_placa)
    
    if info_deteccion[0][2] >= 0.9:
        numero_placa = info_deteccion[0][1]
        return numero_placa

    else:
        return numero_placa