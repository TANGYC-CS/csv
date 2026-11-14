# 使用OpenCV保存图片
import cv2
import os

# 读取图像
img = cv2.imread('cat.png', 1)

# 读取图像后，可以直接保存图片内容，查看图片不是必要过程
# 注意：imwrite 不会自动创建文件夹，目录不存在时只返回 False，不会报错，容易误以为保存成功
if not os.path.exists('save'):
    os.makedirs('save')

# OpenCV 的 imread/imwrite 都是 BGR 顺序，两边一致，所以这里不需要 cvtColor
ok = cv2.imwrite('save/cat_cv2.png', img)   # 课件写的是 save/2.jpg，png 无损更适合存中间结果
# ok = cv2.imwrite('save/cat_cv2.jpg', img)
print("保存是否成功：", ok)
