# 导入模块
import os
import cv2
import matplotlib.pyplot as plt

# 切换到脚本所在目录，保证在任意工作目录下运行都能找到同目录的 1.jpeg
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 读取图像
img = cv2.imread('1.jpeg')
print(img.shape)
width, height = img.shape[:2]

# 显示旋转前图像
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)
plt.show()

# 2x3 变换矩阵
M = cv2.getRotationMatrix2D((width/2, height/2),  # 旋转中心
                           45,  # 旋转角度（逆时针）
                           1)  # 缩放比例

print(M)

# 旋转
img_rotate = cv2.warpAffine(img,  # 输入图像
                            M,  # 变换矩阵
                            (width, height))  # 变换后的大小

img_rotate = cv2.cvtColor(img_rotate, cv2.COLOR_BGR2RGB)
plt.imshow(img_rotate)
plt.show()
