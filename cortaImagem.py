import cv2
import numpy as np

imagemCarregada = cv2.imread("img/teste.png")

print imagemCarregada.shape # quais os canais de cor
print imagemCarregada.item(0,0,2),imagemCarregada.item(0,0,1),imagemCarregada.item(0,0,0)

imagemCarregada.itemset((0, 0, 2),255)
imagemCarregada.itemset((0, 0, 1), 0)
imagemCarregada.itemset((0, 0, 0), 0)
corte = imagemCarregada[180:250, 250:315] # cortando uma parte da imagem
cv2.imwrite("img/corte.png", corte)


imagemCarregada[130:200, 200:265] = corte # cortando uma parte da imagem
cv2.imwrite("img/imgAlterada.png", imagemCarregada)
