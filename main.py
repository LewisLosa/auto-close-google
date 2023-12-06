# https://github.com/LewisLosa/auto-close-google
# Lütfen yorum satırlarını silmeyin :/ ❤️
import cv2
import numpy as np
import os
def renk_algila(frame, renk_siniri):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, renk_siniri[0], renk_siniri[1])
    return mask
def ana():
    kamera = cv2.VideoCapture(0)
    renk_siniri = (np.array([0, 0, 200]), np.array([100, 100, 255]))
    while True:
        ret, frame = kamera.read()
        if not ret:
            print("Kamera bağlantı hatası.")
            break
        maske = renk_algila(frame, renk_siniri)
        if cv2.countNonZero(maske) > 0:
            print("Renk Algılandı")
            os.system("taskkill /im chrome.exe /f")
        cv2.imshow("Kamera Goruntusu", maske)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            kamera.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    ana()
# losa.dev tarafından yazılmıştır.
