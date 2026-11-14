# 使用OpenCV显示图像
import cv2

# 读取图像
img = cv2.imread('cat.png', 1)

# # 显示图像
# cv2.imshow("window1", img)

# # 生成显示窗口
# cv2.namedWindow("window1")

cv2.namedWindow("window1", cv2.WINDOW_NORMAL)  # 先建窗，且允许拖拽缩放
cv2.imshow("window1", img)

# 暂停等待  每次运行保留一行有效代码
# 无限期等待，直到键盘输入，运行后续程序
cv2.waitKey(0)
# 等待3000毫秒或者键盘输入，运行后续程序
# cv2.waitKey(3000)

# 销毁所有窗口
cv2.destroyAllWindows()
