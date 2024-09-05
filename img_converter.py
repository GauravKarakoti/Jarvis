import cv2

img = cv2.imread(r'E:\MIST_AI\tree.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Corrected the color conversion
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
cv2.imwrite("sketch.png", sketch)