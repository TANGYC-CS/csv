# 图像的读取操作
# 导入OpenCV库
import cv2

# 读取图像操作
# 读取彩色图片，两种操作生成效果相同
img1 = cv2.imread("cat.png", 1)
img2 = cv2.imread("cat.png", cv2.IMREAD_COLOR)

# 输出图片参数
print("img1对象的形状：\n", img1.shape)
print("img1对象的大小：\n", img1.size)
print("img2对象的形状：\n", img2.shape)
print("img2对象的大小：\n", img2.size)
print("*" * 100)

# 读取灰度图片
img3 = cv2.imread("cat.png", 0)  # cv2.IMREAD_GRAYSCALE
# 输出图片参数
print("img3对象的形状：\n", img3.shape)
print("img3对象的大小：\n", img3.size)
print("*" * 100)


# 如果读取图片不存在此路径，输出结果为None
img4 = cv2.imread("cat.jpg", 0)  # cv2.IMREAD_GRAYSCALE
# 输出图片参数
# print("img3对象的形状：\n", img3.shape)
# print("img3对象的大小：\n", img3.size)
print(img4)
print("*" * 100)
