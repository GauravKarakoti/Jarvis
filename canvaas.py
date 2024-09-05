import cv2

def sketch_image(image_path, output_path="sketch_with_contours.png"):

    img = cv2.imread(image_path)
    

    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    invert = cv2.bitwise_not(grey_img)
    

    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    

    inverted_blur = cv2.bitwise_not(blur)
    

    sketch = cv2.divide(grey_img, inverted_blur, scale=256.0)


    contours, _ = cv2.findContours(sketch, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    

    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)


    cv2.imwrite(output_path, img)


input_image_path = r'E:\MIST_AI\tree.jpg'
output_sketch_with_contours_path = "sketch_with_contours.png"
sketch_image(input_image_path, output_sketch_with_contours_path)