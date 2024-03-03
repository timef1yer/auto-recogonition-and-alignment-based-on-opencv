import cv2
import numpy as np

'''
加载图像：
使用 OpenCV 的 cv2.imread() 函数加载包含对准标记的图像。
python
Copy code
'''
image = cv2.imread('Z:\\Microscope\\aviad frydman\\shaw\\exfoliated graphene\\DEV116\\10x\\2.jpg')

'''
图像处理：
为了更好地检测对准标记，您可以进行一些图像处理操作，例如灰度化、二值化、边缘检测等。
python
Copy code
'''
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)[1]
edges = cv2.Canny(thresh, 50, 150)

'''
检测轮廓：
使用 OpenCV 的 cv2.findContours() 函数检测图像中的轮廓。
python
Copy code
'''

contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

'''
筛选对准标记：
根据对准标记的特征，您可以根据一些条件筛选出符合要求的轮廓。
python
Copy code
'''

alignment_marks = []
for contour in contours:
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    if area > 100 and perimeter > 100:
        alignment_marks.append(contour)

'''
绘制标记：
最后，您可以使用 OpenCV 的绘图函数，在原始图像上绘制检测到的对准标记。
python
Copy code
'''

cv2.drawContours(image, alignment_marks, -1, (0, 255, 0), 2)
cv2.imshow('Alignment Marks', image)
cv2.waitKey(0)
cv2.destroyAllWindows()