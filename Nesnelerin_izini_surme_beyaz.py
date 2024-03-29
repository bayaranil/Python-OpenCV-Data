import cv2
import numpy as np

cap = cv2.VideoCapture("Elsa.mp4")

while True:
    ret,frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    sensitivity = 15
    lower_white = np.array([0,0,255-sensitivity]) #kırmızı için hsv code for red şeklinde google da aratabiliriz.
    upper_white = np.array([255, sensitivity, 255])


    mask = cv2.inRange(hsv, lower_white, upper_white)
    #hsv içinde lower white ve upper white arasında kalan bölgeye mask uygula kalan bölgeyi kazı sil diyoruz.
    res = cv2.bitwise_and(frame,frame,mask=mask)
    #maskın doğru uygulanabilmesi için bitwise yaptık.
    #çift frame yazdık çünkü özel bir kullanımdır. her mask yazmamız gereken yerde çift frame yazmalıyız -bknz. cv2.bitwise_and()


    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

