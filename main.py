import sys
import cv2
from ultralytics import YOLO
from deteccion_texto import deteccion_de_texto
from base_datos import placa_registrada, registrar_placas

# Cargar modelo
modelo_deteccion_placas = YOLO('modelo/modelo_placas_no_final.pt')

# Cargar video
ruta_video = ('videos/' + sys.argv[1] + '.mp4')
video = cv2.VideoCapture(ruta_video)

# Inicializar variables
numero_placa_anterior = None
info_anterior = None
posiciones_info = [100, 160, 220, 280, 340]

# Procesar video
while True:
    _, cuadro = video.read()  # Leer cuadro del video
    detecciones = modelo_deteccion_placas(cuadro, conf=0.61)  # Detectar placas con una confianza mayor a 0.61%

    for deteccion in detecciones[0].boxes:
        x1, y1, x2, y2 = deteccion.xyxy.squeeze().tolist()  # Coordenadas del cuadro detectado
        confianza = float(deteccion.conf)  # Valor de confianza de la placa detectada

        if confianza != -1:
            imagen_placa = cuadro[int(y1):int(y2), int(x1):int(x2), :]  # Recortar la placa del cuadro
            imagen_gris = cv2.cvtColor(imagen_placa, cv2.COLOR_BGR2GRAY)  # Convertir imagen de la placa a escala de grises
            imagen_umbral = cv2.threshold(imagen_gris, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]  # Aplicar filtros para eliminar el ruido

            numero_placa = deteccion_de_texto(imagen_umbral)
            registrar_placas(numero_placa, 0)

            if numero_placa is not None:
                cuadro = cv2.putText(cuadro, numero_placa, (int(x1), int(y1)), cv2.FONT_HERSHEY_DUPLEX, 6, (128, 17, 0), 7, cv2.LINE_AA)
                info = placa_registrada(numero_placa)
                numero_placa_anterior = numero_placa
                info_anterior = info

                if info_anterior is not None:
                    for i, valor in enumerate(info):
                        posicion = posiciones_info[i]
                        cuadro = cv2.putText(cuadro, valor, (0, posicion), cv2.FONT_HERSHEY_DUPLEX, 2, (128, 17, 0), 5, cv2.LINE_AA)

            else:
                if numero_placa_anterior is not None:
                    cuadro = cv2.putText(cuadro, numero_placa_anterior, (int(x1), int(y1)), cv2.FONT_HERSHEY_DUPLEX, 6, (128, 17, 0), 7, cv2.LINE_AA)

                    if info_anterior is not None:
                        for i, valor in enumerate(info_anterior):
                            posicion = posiciones_info[i]
                            cuadro = cv2.putText(cuadro, valor, (0, posicion), cv2.FONT_HERSHEY_DUPLEX, 2, (128, 17, 0), 5, cv2.LINE_AA)

    cv2.imshow('Video', cv2.resize(cuadro, (1080, 720)))
    if cv2.waitKey(20) == ord('q'):
        break

cv2.destroyAllWindows()