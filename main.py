import sys
import cv2
from ultralytics import YOLO

#Cargar modelo
modelo_deteccion_placas = YOLO('modelo_placas_no_final.pt')

#Obtener video
ruta_video = sys.argv[0]
video = cv2.VideoCapture(ruta_video)

