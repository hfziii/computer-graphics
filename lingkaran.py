import numpy as np
import cv2 

jendela = np.zeros((500,500, 3), dtype='uint8')
jendela [ : ] = (255, 0, 100)

# merah = 0,0,255
putih = 255,255,255

# lingkaran
cv2.circle(jendela, (125,125), 100, (putih), 20) 

cv2.imshow("kertas", jendela)
cv2.waitKey(0)