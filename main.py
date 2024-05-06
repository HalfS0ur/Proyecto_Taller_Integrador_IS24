import sys
import cv2
from ultralytics import YOLO

from deteccion_texto import deteccion_de_texto

#Cargar modelo
modelo_deteccion_placas = YOLO('modelo_placas_no_final.pt')

#Obtener video
ruta_video = str(sys.argv[1])
video = cv2.VideoCapture(ruta_video)

#Procesar video
while True: #Ciclo infinito
    _, cuadro = video.read() #Abre el video cuadro por cuadro
    detecciones = modelo_deteccion_placas(cuadro, conf=0.61) #Detecta placas con un intervalo de confianza mayor a 0.61%

    cajas = detecciones[0].boxes #Cajas que encierran las placas en el video
    for caja in cajas:
        x1, y1, x2, y2 = caja.xyxy.squeeze().tolist() #Coordenadas de la caja de detección
        confianza = float(caja.conf) #Valor de confianza de la placa identificada

        if confianza != -1:
            imagen_placa = cuadro[int(y1):int(y2), int(x1):int(x2), :] #Recorta la placa del cuadro completo
            escala_grises = cv2.cvtColor(imagen_placa, cv2.COLOR_BGR2GRAY) #Convierte la imagen de la placa a escala de grises
            threshold_img = cv2.threshold(escala_grises, 64, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] #Aplica filtros para eliminar el ruido

            cv2.imshow('Placa procesada', threshold_img) #Salida de prueba
            deteccion_de_texto(threshold_img)

    #cuadro_ = detecciones[0].plot()

    cv2.imshow('Video', cuadro)
    if (cv2.waitKey(20) == ord('q')):
        break

cv2.destroyAllWindows()
