import cv2

harcascade = "model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) # height

min_area = 500
max_area = 0
max_plate_coords = None

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    max_area = 0  # Reset max area for each frame
    max_plate_coords = None

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area and area > max_area:
            max_area = area
            max_plate_coords = (x, y, w, h)

    if max_plate_coords is not None:
        x, y, w, h = max_plate_coords
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, "Placa", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

        img_roi = img[y: y+h, x:x+w]
        cv2.imshow("Resultado", img_roi)
    else:
        print("no hay detecciones")#cv2.destroyWindow("ROI")  # Destroy window if no plate detected

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s') and max_plate_coords is not None:
        cv2.imwrite("plates/scaned_img.jpg", img_roi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results", img)
        cv2.waitKey(500)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

