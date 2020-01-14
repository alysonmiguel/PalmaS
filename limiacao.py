import cv2

img = cv2.imread("img/palma.png", 0)

px = 135

limiar, imgLimiar = cv2.threshold(img, px, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("Limiar", imgLimiar)
cv2.imwrite('img/palma_'+str(px)+'_.png', imgLimiar)

cv2.waitKey(0)
cv2.destroyAllWindows()