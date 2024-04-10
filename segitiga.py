import numpy as np
import cv2 

jendela = np.zeros((500,500, 3), dtype='uint8')
jendela [ : ] = (255, 0, 100)

merah = 0,0,255
kuning = 255, 100, 0
hijau = 0, 255, 0
biru = 255, 0, 0

# segitiga
kordinat1 = (250, 125)
kordinat2 = (125, 375)
kordinat3 = (375, 375)

cv2.circle(jendela, (kordinat1), 20, (merah), -10)
cv2.circle(jendela, (kordinat1), 20, (kuning), -1)
cv2.circle(jendela, (kordinat1), 20, (hijau), -1)

titik_segitiga = np.arrray ([kordinat1, kordinat2, kordinat3])

cv2.drawContours(jendela, [titik_segitiga], 0, biru, -1)

cv2.imshow("kertas", jendela)
cv2.waitKey(0)