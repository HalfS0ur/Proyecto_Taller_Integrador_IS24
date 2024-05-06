import easyocr

reader = easyocr.Reader(['es'], gpu=True) #Configura el lector de imagenes (configurar gpu de acuerdo al caso)

def deteccion_de_texto(imagen_placa):
    texto = reader.readtext(imagen_placa)
    print(texto)