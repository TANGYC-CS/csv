# 画圆圈
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((512, 512, 3), np.uint8)

cv2.circle(img,  # 目标图像
           (256, 256),  # 圆心
           256,  # 半径
           (0, 0, 255),  # 颜色
           -1)  # 线宽，-1为填充

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.show()
