# matplotlib保存图片
import cv2 as cv
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread('cat.png', 1)

plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title('show img'), plt.xticks([]), plt.yticks([])
plt.show()

# 保存路径判断，如果没有对应的文件夹，系统会报错
import os
# 如果当前路径下不存在save文件夹，系统会进行创建
if not os.path.exists("save"):
    os.makedirs("save")

# 保存图片
# 注意：img 是 BGR 顺序，而 plt.imsave 按 RGB 顺序写盘，直接存会导致红蓝互换
plt.imsave('save/cat.png', img)  # 课件原样写法：颜色会偏（红蓝互换）
plt.imsave('save/cat_rgb.png', cv.cvtColor(img, cv.COLOR_BGR2RGB))  # 正确颜色

print("保存完成，请查看 save 文件夹")
