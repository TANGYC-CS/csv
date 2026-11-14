# 绘制直线
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 画线
img = np.zeros((512, 512, 3), np.uint8)
print(img.dtype)

cv2.line(img,  # 目标图像
         (0, 0),  # 起点
         (256, 256),  # 终点
         (0, 255, 0),  # 颜色 BGR
         5)  # 粗细

img_line = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_line)
plt.show()
