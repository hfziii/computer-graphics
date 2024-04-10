import numpy as np
import cv2 

jendela = np.zeros((500,500, 3), dtype='uint8')
jendela [ : ] = (255, 0, 100)

# merah = 0,0,255
putih = 255,255,255

# kotak
cv2.rectangle(jendela, (125,125), (250,375), (putih)) 

# garis
# cv2.line(jendela, (0,0), (250,250), (merah), 20)
# cv2.line(jendela, (0,0), (500,500), (merah), 20)
# cv2.line(jendela, (500,0), (0,500), (merah), 20)

cv2.imshow("kertas", jendela)
cv2.waitKey(0)