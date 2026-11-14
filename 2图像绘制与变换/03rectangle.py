# 画矩形
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((512, 512, 3), np.uint8)

cv2.rectangle(img,  # 目标图像
              (128, 128),  # 左上角点
              (256, 256),  # 相对的顶点
              (0, 255, 0),  # 颜色
              3)  # 粗细

img_rectangle = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rectangle)
plt.show()
