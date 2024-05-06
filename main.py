import sys
import cv2
import ultralytics

#obtener video
ruta_video = sys.argv[0]
video = cv2.VideoCapture(ruta_video)