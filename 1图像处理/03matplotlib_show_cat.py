# 使用matplotlib显示图像
import cv2 as cv
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread('cat.png', 1)

# 在matplotlib中展示图像
# 默认展示方式
plt.imshow(img)
plt.title('show img1'), plt.xticks([]), plt.yticks([])
plt.show()

# 将opencvBGR图像展示方式转化为RGB

# 使用切片处理通道维度
plt.imshow(img[:, :, ::-1])  # 通道进行逆序排序 BGR-->RGB
plt.title('show img2'), plt.xticks([]), plt.yticks([])
plt.show()

# 使用OpenCV处理通道维度
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('show img3'), plt.xticks([]), plt.yticks([])
plt.show()
