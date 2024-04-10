import cv2
import numpy as np

jendela = np.zeros((500, 500, 3), dtype="uint8")

persegi = cv2.rectangle(jendela, (125, 125), (375,375), (255,255,255), 5)

cv2.imshow("Canvas", jendela)
cv2.waitKey(0)