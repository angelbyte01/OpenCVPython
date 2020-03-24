import numpy as np
import cv2

#mostramos la imagen

def dibujar(event, x,y, etiquetas, parametros):
    if event== cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen,(x,y), 50,(255,0,0),-1)
        
cv2.namedWindow(winname='mi_imagen')
cv2.setMouseCallback('mi_imagen',dibujar)

imagen = np.zeros((500,500,3), np.int8)

#imagen donde vamos a dibujar
while True:
    cv2.imshow('mi_imagen', imagen)
    if cv2.waitKey(10) & 0xFF==27:
        break
cv2.destroyAllWindows()