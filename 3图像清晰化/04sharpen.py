# 锐化
# 导入模块
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 设置正常显示中文和负号
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei', 'PingFang SC', 'Heiti TC', 'Microsoft YaHei']  # 正常显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 读取灰度图
moon = cv2.imread("picture/moon.jpg", 0)
print(moon.dtype)
moon_copy = np.copy(moon)
moon_float = moon_copy.astype("float")  # 修改图像类型
print(moon_float.dtype)

# 计算梯度图
row, column = moon.shape
gradient = np.zeros((row, column))
for x in range(row - 1):
    for y in range(column - 1):
        gx = abs(moon_float[x + 1, y] - moon_float[x, y])  # 通过相邻像素相减计算图像梯度
        gy = abs(moon_float[x, y + 1] - moon_float[x, y])  # 通过相邻像素相减计算图像梯度
        gradient[x, y] = gx + gy

# 叠加灰度图与梯度图得到锐化图
sharp = moon_float + gradient
sharp = np.where(sharp < 0, 0, np.where(sharp > 255, 255, sharp))  # 将小于0的像素设置为0，大于255的像素设置为255

# 修改图像类型
gradient = gradient.astype("uint8")
sharp = sharp.astype("uint8")

# 显示图像
plt.subplot(1, 3, 1)
plt.imshow(moon, "gray")
plt.title("灰度图")

plt.subplot(1, 3, 2)
plt.imshow(gradient, "gray")
plt.title("梯度图")

plt.subplot(1, 3, 3)
plt.imshow(sharp, "gray")
plt.title("锐化图")

# 保存结果（方便无图形界面时查看）
os.makedirs("save", exist_ok=True)
plt.savefig("save/04sharpen_result.png", dpi=150, bbox_inches="tight")

plt.show()
