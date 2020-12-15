import cv2

img = cv2.imread("contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

M = cv2.moments(thresh)
print(M) #--> tuttuğu keyword ve değerler sözlük

x = int(M["m10"] / M["m00"])
y = int(M["m01"] / M["m00"])
#Ağırlık merkezi koordinatları...

cv2.circle(img, (x,y), 5, (0,0,255), -1)


cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()