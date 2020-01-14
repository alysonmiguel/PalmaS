import cv2

imagemCarregada = cv2.imread("img/exemplo.png", 0)
cv2.imshow("Imagem", imagemCarregada)
cv2.waitKey(0)
cv2.destroyAllWindows()