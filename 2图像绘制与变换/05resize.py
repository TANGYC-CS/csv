# 图像缩放
import os
import cv2
import matplotlib.pyplot as plt

# 切换到脚本所在目录，保证从任意工作目录运行都能找到同目录的 1.jpeg
# （VS Code 右键运行时，终端当前目录是 F:\计算机视觉，不是本文件所在目录）
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 读取图像
img = cv2.imread('1.jpeg')
print(img.shape)
width, height = img.shape[:2]

# 显示图像
img_original = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_original)
plt.show()

# 通过 dsize 设置输出图像大小
img_dsize = cv2.resize(img,  # 输入图像
                       (4 * width, 2 * height),  # 输出图像大小
                       )

img_dsize = cv2.cvtColor(img_dsize, cv2.COLOR_BGR2RGB)
plt.imshow(img_dsize)
plt.show()

# 2、通过 fx 和 fy 设置输出图像大小
img_fx_fy = cv2.resize(img,  # 输入图像
                       None,  # 输出图像大小
                       fx=1/2,  # x轴缩放因子
                       fy=1/4,  # y轴缩放因子
                       )

img_fx_fy = cv2.cvtColor(img_fx_fy, cv2.COLOR_BGR2RGB)
plt.imshow(img_fx_fy)
plt.show()
