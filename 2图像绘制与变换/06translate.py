# 图像平移
# 导入模块
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 切换到脚本所在目录，保证在任意工作目录下运行都能找到同目录的 1.jpeg
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 读取图像
img = cv2.imread('1.jpeg')
print(img.shape)
width, height = img.shape[:2]

# 显示平移前图像
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()

# 2x3 变换矩阵：100 表示水平方向上的平移距离，50 表示垂直方向上的平移距离
M = np.float64([[1, 0, 100], [0, 1, 50]])

# 平移
img2 = cv2.warpAffine(img,  # 转换前的图像
                      M,  # 变换矩阵
                      (width, height))  # 变换后的大小

img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
plt.imshow(img2_rgb)
plt.show()
