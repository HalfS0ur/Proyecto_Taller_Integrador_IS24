import sys
import cv2
from ultralytics import YOLO

from deteccion_texto import deteccion_de_texto
from base_datos import placa_registrada

#Cargar modelo
modelo_deteccion_placas = YOLO('modelo/modelo_placas_no_final.pt')

#Obtener video
ruta_video = ('videos/'+sys.argv[1]+'.mp4')
video = cv2.VideoCapture(ruta_video)

#Inicializar variables 
numero_placa_prev = None
informacion_prev = None
posiciones_informacion = [100, 160, 220, 280]


#Procesar video
while True: #Ciclo infinito
    _, cuadro = video.read() #Abre el video cuadro por cuadro
    detecciones = modelo_deteccion_placas(cuadro, conf=0.61) #Detecta placas con un intervalo de confianza mayor a 0.61%
    cuadro_numero_placa = cuadro
    hostia = cuadro

    cajas = detecciones[0].boxes #Cajas que encierran las placas en el video
    for caja in cajas:
        x1, y1, x2, y2 = caja.xyxy.squeeze().tolist() #Coordenadas de la caja de detección
        confianza = float(caja.conf) #Valor de confianza de la placa identificada

        if confianza != -1:
            imagen_placa = cuadro[int(y1):int(y2), int(x1):int(x2), :] #Recorta la placa del cuadro completo
            escala_grises = cv2.cvtColor(imagen_placa, cv2.COLOR_BGR2GRAY) #Convierte la imagen de la placa a escala de grises
            threshold_img = cv2.threshold(escala_grises, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1] #Aplica filtros para eliminar el ruido
            
            cv2.imshow('Placa', threshold_img) #Salida de prueba

            numero_placa = deteccion_de_texto(threshold_img)
            print(numero_placa) #Salida de prueba

            if numero_placa is not None:
                cuadro_numero_placa = cv2.putText(cuadro, numero_placa, (int(x1), int(y1)), cv2.FONT_HERSHEY_DUPLEX, 6, (128, 17, 0), 7, cv2.LINE_AA)
                informacion = placa_registrada(numero_placa)
                numero_placa_prev = numero_placa
                informacion_prev = informacion

                for i, valor in enumerate(informacion):
                     posicion = posiciones_informacion[i]
                     cuadro_numero_placa = cv2.putText(cuadro_numero_placa, valor, (0, posicion), cv2.FONT_HERSHEY_DUPLEX, 2, (128, 17, 0), 5, cv2.LINE_AA)

            else:
                if numero_placa_prev is not None:
                    cuadro_numero_placa = cv2.putText(cuadro, numero_placa_prev, (int(x1), int(y1)), cv2.FONT_HERSHEY_DUPLEX, 6, (128, 17, 0), 7, cv2.LINE_AA)

                    for i, valor in enumerate(informacion_prev):
                        posicion = posiciones_informacion[i]
                        cuadro_numero_placa = cv2.putText(cuadro_numero_placa, valor, (0, posicion), cv2.FONT_HERSHEY_DUPLEX, 2, (128, 17, 0), 5, cv2.LINE_AA)

    if numero_placa_prev is not None:
        cuadro_numero_placa = cv2.putText(cuadro, numero_placa_prev, (int(x1), int(y1)), cv2.FONT_HERSHEY_DUPLEX, 6, (128, 17, 0), 7, cv2.LINE_AA)

        for i, valor in enumerate(informacion_prev):
            posicion = posiciones_informacion[i]
            cuadro_numero_placa = cv2.putText(cuadro_numero_placa, valor, (0, posicion), cv2.FONT_HERSHEY_DUPLEX, 2, (128, 17, 0), 5, cv2.LINE_AA)

    if not cajas:
        numero_placa_prev = None
                     
    #cuadro_ = detecciones[0].plot()

    cuadro_ajustado = cv2.resize(cuadro_numero_placa, (1080, 720))
    cv2.imshow('Video', cuadro_ajustado)
    if (cv2.waitKey(20) == ord('q')):
        break

cv2.destroyAllWindows()
