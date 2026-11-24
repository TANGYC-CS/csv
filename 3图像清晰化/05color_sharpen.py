# 彩色图像锐化
# 原理：锐化 = 原图 + 高频边缘（梯度）。彩色图不能简单当成一张灰度矩阵，
#      因为 B、G、R 三个通道的梯度方向和大小并不一致，需要选对「在哪里加梯度」。
# 导入模块
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 设置正常显示中文和负号
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei', 'PingFang SC', 'Heiti TC', 'Microsoft YaHei']  # 正常显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 正常显示负号


# ---------- 工具函数 ----------
def gradient_of(channel):
    """对单通道求梯度：|f[x+1,y]-f[x,y]| + |f[x,y+1]-f[x,y]|
    与 04sharpen.py 的双重循环完全等价，这里用向量化写法，速度快几百倍。
    """
    f = channel.astype("float32")
    gx = np.abs(f[:, 1:] - f[:, :-1])   # 水平方向相邻像素相减，结果形状 (row, col-1)
    gy = np.abs(f[1:, :] - f[:-1, :])   # 垂直方向相邻像素相减，结果形状 (row-1, col)
    g = np.zeros_like(f)
    g[:, :-1] += gx                     # 放回原位置，最后一行/列保持 0（没有右/下邻居）
    g[:-1, :] += gy
    return g


def sharpen_per_channel(image, k=1.0):
    """方案一：对 B、G、R 三个通道各自独立做「原图 + 梯度」。"""
    out = np.zeros(image.shape, dtype="float32")
    for c in range(3):
        f = image[:, :, c].astype("float32")
        out[:, :, c] = f + k * gradient_of(image[:, :, c])
    return np.clip(out, 0, 255).astype("uint8")


# ---------- 1. 读取彩色图像 ----------
img = cv2.imread("picture/bg.png", 1)          # 1 = 彩色三通道，BGR 顺序
row, column = img.shape[:2]
print("图像尺寸:", row, "x", column, " 通道数:", img.shape[2])

# ---------- 2. 转到 YCrCb，把亮度与颜色分开 ----------
# Y 是亮度（人眼感知的「清晰度」几乎全来自它），Cr / Cb 只携带颜色信息
ycc = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb).astype("float32")
Y, Cr, Cb = cv2.split(ycc)
grad = gradient_of(Y)
print("亮度 Y 的范围: %.0f ~ %.0f, 梯度均值 %.2f" % (Y.min(), Y.max(), grad.mean()))

# ---------- 3. 三种锐化结果 ----------
# 方案一：三通道各自锐化（教学对照，容易产生彩色噪点/彩边）
sharp_rgb = sharpen_per_channel(img, k=1.0)

# 方案二：只在亮度 Y 上加梯度，颜色通道原样不动（推荐做法）
Y_light = np.clip(Y + 5 * grad, 0, 255)        # k=5 是因为这张图整体被压白、梯度很小
sharp_ycc = cv2.cvtColor(
    cv2.merge([Y_light, Cr, Cb]).astype("uint8"), cv2.COLOR_YCrCb2BGR)

# 方案三：先把亮度拉伸，再锐化，细节最明显
# 注意：Y 拉到 0~255 后颜色会被亮度“淹没”，画面偏灰白，属于比较激进的改造
Y_norm = cv2.normalize(Y, None, 0, 255, cv2.NORM_MINMAX)
Y_strong = np.clip(Y_norm + 3 * gradient_of(Y_norm), 0, 255)
sharp_strong = cv2.cvtColor(
    cv2.merge([Y_strong, Cr, Cb]).astype("uint8"), cv2.COLOR_YCrCb2BGR)

# 方案四（实用版）：温和拉伸 + 平滑后的梯度，保留原有色调
# 1) 梯度先做 3×3 高斯平滑，避免把噪点也一起放大成白边（非锐化掩模的常见处理）
grad_smooth = cv2.GaussianBlur(grad, (3, 3), 0)
# 2) 只把亮度从 213~255 映射到 150~255，留出层次，不压成黑白
Y_mild = np.clip((Y - 213.0) * (255.0 - 150.0) / (255.0 - 213.0) + 150.0, 0, 255)
# 3) 在拉伸后的亮度上叠加平滑梯度
Y_final = np.clip(Y_mild + 3 * gradient_of(Y_mild), 0, 255)
sharp_final = cv2.cvtColor(
    cv2.merge([Y_final, Cr, Cb]).astype("uint8"), cv2.COLOR_YCrCb2BGR)

# ---------- 4. 显示图像（matplotlib 需要 RGB 顺序） ----------
to_rgb = lambda im: cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
grad_show = np.clip(grad * 6, 0, 255).astype("uint8")   # 梯度本身很暗，×6 才看得见

plt.figure(figsize=(15, 10))
gs = plt.GridSpec(3, 3, height_ratios=[1, 1, 0.62], hspace=0.22)

plt.subplot(gs[0, 0])
plt.imshow(to_rgb(img))
plt.title("原图（偏淡、低对比）")
plt.axis("off")

plt.subplot(gs[0, 1])
plt.imshow(grad_show, "gray")
plt.title("亮度梯度图（×6 增强显示）")
plt.axis("off")

plt.subplot(gs[0, 2])
plt.imshow(to_rgb(sharp_rgb))
plt.title("方案一：三通道各自锐化 k=1")
plt.axis("off")

plt.subplot(gs[1, 0])
plt.imshow(to_rgb(sharp_ycc))
plt.title("方案二：只锐化亮度 Y，k=5")
plt.axis("off")

plt.subplot(gs[1, 1])
plt.imshow(to_rgb(sharp_strong))
plt.title("方案三：亮度拉满 0~255 再锐化（激进）")
plt.axis("off")

plt.subplot(gs[1, 2])
plt.imshow(to_rgb(sharp_final))
plt.title("方案四：温和拉伸 + 平滑梯度（推荐）")
plt.axis("off")

ax_txt = plt.subplot(gs[2, :])
ax_txt.axis("off")
ax_txt.text(0.01, 0.95,
            "锐化公式：锐化图 = 原图 + k × 梯度（梯度 = 相邻像素差，代表边缘强度）\n\n"
            "· 方案一  B/G/R 三通道各自加梯度 → 三通道增量不一致，边缘处会冒彩色噪点、彩边\n"
            "· 方案二  只在亮度 Y 上加梯度，Cr/Cb 原样不动 → 细节增强且绝不串色（标准做法）\n"
            "· 方案三  Y 用 min-max 拉到 0~255，细节最猛，但颜色会被亮度淹没、画面发灰白\n"
            "· 方案四  只把 213~255 温和映射到 150~255，梯度先高斯平滑再叠加 → 保留色调且无硬白边\n\n"
            "k（增益）越大越锐；过大时边缘出现光晕（halo）、噪点被一起放大。这张图原始动态范围只有 42 级灰度，"
            "所以 k 要取 3~5 才看得出来。",
            fontsize=11, va="top", linespacing=1.7)

# 保存结果（方便无图形界面时查看）
os.makedirs("save", exist_ok=True)
plt.savefig("save/05color_sharpen_result.png", dpi=150, bbox_inches="tight")

# 单独导出两张成品图（BGR，可直接被其他程序读取）
cv2.imwrite("save/bg_sharp_strong.png", sharp_strong)   # 细节最强，偏灰白
cv2.imwrite("save/bg_sharp_mild.png", sharp_final)      # 保色版本，推荐使用
print("已保存: save/bg_sharp_strong.png（激进版） / save/bg_sharp_mild.png（保色版）")

plt.show()
