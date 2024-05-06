import easyocr

reader = easyocr.Reader(['es'], gpu=True) #Configura el lector de imagenes (configurar gpu de acuerdo al caso)

def deteccion_de_texto(imagen_placa):
    info_deteccion = reader.readtext(imagen_placa)
    print(info_deteccion)