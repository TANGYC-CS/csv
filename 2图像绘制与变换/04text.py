# 画文字
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((512, 512, 3), np.uint8)

font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(
    img,  # 目标图像
    "OpenCV",  # 文字
    # "你好",  # 文字
    (10, 300),  # 文本框左下角
    font,  # 文字字体
    4,  # 文字大小
    (255, 255, 255),  # 文字颜色
    3,  # 文字粗细
    cv2.LINE_AA  # 文字线型
)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.show()
