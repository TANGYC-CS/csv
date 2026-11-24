# 中值滤波
# 导入模块
import os
import cv2
import matplotlib.pyplot as plt

# 设置正常显示中文和负号
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei', 'PingFang SC', 'Heiti TC', 'Microsoft YaHei']  # 正常显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 中值滤波
img = cv2.imread("picture/1.png", 1)  # 读取彩色图像
dst = cv2.medianBlur(
    img,  # 输入图像
    (5)  # 内核大小（必须为大于 1 的奇数）
)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

# 图像显示
plt.subplot(2, 1, 1)
plt.imshow(img)
plt.title('noise')

plt.subplot(2, 1, 2)
plt.imshow(dst)
plt.title('median blur')

# 保存结果（方便无图形界面时查看）
os.makedirs("save", exist_ok=True)
plt.savefig("save/02median_blur_result.png", dpi=150, bbox_inches="tight")

plt.show()
