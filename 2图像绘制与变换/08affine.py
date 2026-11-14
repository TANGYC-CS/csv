# 仿射变换
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

# 显示仿射前的图像
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()

# 2x3变换矩阵
pst1 = np.float32([[10, 10], [20, 20], [50, 30]])
pst2 = np.float32([[190, 10], [180, 20], [150, 30]])  # x=100对称
M = cv2.getAffineTransform(pst1, pst2)
print(M)

# 仿射变换
img_radiate = cv2.warpAffine(img,  # 输入图像
                             M,  # 变换矩阵
                             (width, height))  # 变换后的大小

img_radiate = cv2.cvtColor(img_radiate, cv2.COLOR_BGR2RGB)
plt.imshow(img_radiate)
plt.show()
