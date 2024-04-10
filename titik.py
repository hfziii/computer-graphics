import numpy as np
import cv2 

jendela = np.zeros((500,500, 3), dtype='uint8')
jendela [ : ] = (255, 0, 100)

merah = 0,0,255

cv2.line(jendela, (250,250), (250,250), (merah), 10)

cv2.imshow("kertas", jendela)
cv2.waitKey(0)