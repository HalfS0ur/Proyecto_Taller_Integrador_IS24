import cv2

from ultralytics import YOLO

vehiculos = [2, 3, 5, 7]

def main():
    #Obtener video
    video = cv2.VideoCapture(0)

    #Cargar modelo
    modelo_coco = YOLO('license_plate_detector.pt')

    modelo_deteccion_placas = YOLO('license_plate_detector.pt')

    while True:
        ret, cuadro = video.read()

        resultado = modelo_deteccion_placas.track(cuadro, persist=True)  #resultado = modelo_coco.track(cuadro, classes = vehiculos, persist=True) // 

        boxes = resultado[0].boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy.squeeze().tolist()
            confianza = float(box.conf)
            id = box.id
            print('Coordinates:', (x1, y1, x2, y2))
            print('Confianza:', confianza)
            print('id:', id)

            if id != -1:
                crop = cuadro[int(y1):int(y2), int(x1):int(x2), :]
                cv2.imshow('placa', crop)

        frame_ = resultado[0].plot()

        cv2.imshow("video", frame_)

        if (cv2.waitKey(30) == ord('q')):
            break

if __name__ == '__main__':
    main()