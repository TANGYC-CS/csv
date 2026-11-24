# 膨胀腐蚀操作
import numpy as np
import cv2
import matplotlib.pyplot as plt

# 设置正常显示中文和负号（必须写在 set_title 之前才生效）
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei', 'PingFang SC', 'Heiti TC', 'Microsoft YaHei']  # 正常显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 1 读取图像
img = cv2.imread("picture/2.png")
print("图像尺寸:", img.shape)

# 2 创建核结构
kernel = np.ones((5, 5), np.uint8)   # 5×5 全 1 的方阵，腐蚀/膨胀的作用半径就由它决定

# 3 图像腐蚀和膨胀
erosion = cv2.erode(img, kernel)     # 腐蚀：任何一个 5×5 邻域内出现黑色，中心点就变黑 → 白色笔画变细
dilate = cv2.dilate(img, kernel)     # 膨胀：任何一个 5×5 邻域内出现白色，中心点就变白 → 白色笔画变粗

print("原图白色像素: %.1f%%" % (100 * (img.mean(axis=2) > 128).mean()))
print("腐蚀后白色像素: %.1f%%" % (100 * (erosion.mean(axis=2) > 128).mean()))
print("膨胀后白色像素: %.1f%%" % (100 * (dilate.mean(axis=2) > 128).mean()))

# 4 图像展示
# matplotlib 期望 RGB，OpenCV 读进来是 BGR，直接 imshow 颜色会颠倒
def to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB) if image.ndim == 3 else image

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(10, 8), dpi=100)

axes[0].imshow(to_rgb(img))
axes[0].set_title("原图")

axes[1].imshow(to_rgb(erosion))
axes[1].set_title("腐蚀后结果")

axes[2].imshow(to_rgb(dilate))
axes[2].set_title("膨胀后结果")

for ax in axes:
    ax.axis("off")

# 保存结果（方便无图形界面时查看）
import os

os.makedirs("save", exist_ok=True)
plt.savefig("save/05erode_dilate_result.png", dpi=150, bbox_inches="tight")

plt.show()
