import cv2
import numpy as np

img = cv2.imread('test1.jpg')

# 中值滤波，核大小5，使图像更加平滑，从而减少边界检测中的误差。
img = cv2.medianBlur(img, 5)

# 转换为HSV颜色空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 设置临界值，取粉色区间
lower_pink = np.array([100, 30, 30])
upper_pink = np.array([200, 255, 255])

# 根据临界值创建掩膜，掩膜中符合粉色范围的像素为白色（255），其余为黑色（0）
mask = cv2.inRange(hsv, lower_pink, upper_pink)

# 显示掩膜
mask1 = cv2.resize(mask, (600, 600))
cv2.imshow("Mask", mask1)
cv2.waitKey(0)

# 查找轮廓
# cv2.RETR_TREE 表示提取完整的轮廓层级结构。
# cv2.CHAIN_APPROX_SIMPLE 压缩轮廓点以减少冗余。
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print("Number of contours in image:", len(contours))

#  创建原始图像的副本，在上面绘制轮廓线
img_contours = img.copy()
 
# 根据面积从大到小对等值线进行排序
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

# 检查两条轮廓线是否重叠

def contours_overlap(cnt1, cnt2):
    """
    cnt1 和 cnt2 是两个轮廓线
    cv2.boundingRect 函数计算每个轮廓的边界矩形。
    边界矩形是包含该轮廓的最小矩形，返回值为 (x, y, width, height)。
    x 和 y 是矩形左上角的坐标，width 和 height 是矩形的宽度和高度。"""
    rect1 = cv2.boundingRect(cnt1)
    rect2 = cv2.boundingRect(cnt2)
    x_overlap = rect1[0] < rect2[0] + rect2[2] and rect1[0] + rect1[2] > rect2[0]
    y_overlap = rect1[1] < rect2[1] + rect2[3] and rect1[1] + rect1[3] > rect2[1]
    return x_overlap and y_overlap

# 选择最大的 27 个不重叠轮廓线
selected_contours = []
for cnt in sorted_contours:
    if len(selected_contours) == 27:
        break
    overlap = False
    for selected in selected_contours:
        if contours_overlap(cnt, selected):
            overlap = True
            break
    if not overlap:
        selected_contours.append(cnt)

# 循环遍历在之前调出的27个轮廓线并计算面积并绘制图像
contour_areas = []
for cnt in selected_contours:
    # 使用 cv2.convexHull 计算凸包（凸包是包裹轮廓的最小凸多边形）
    hull = cv2.convexHull(cnt)
    
    """
    使用 cv2.approxPolyDP 对凸包进行多边形逼近
    epsilon 是逼近精度参数，表示允许的最大偏差，值越小多边形越接近实际轮廓。
    cv2.arcLength(hull, True) 返回凸包的周长，用于计算 epsilon。"""
    epsilon = 0.00000001 * cv2.arcLength(hull, True) 
    approx = cv2.approxPolyDP(hull, epsilon, True)
    
    # 绘制逼近后的多边形轮廓
    cv2.drawContours(img_contours, [approx], -1, (0, 255, 0), 3)
    
    #  计算近似多边形的面积
    area = cv2.contourArea(approx)
    contour_areas.append(area)
    # 计算近似多边形的周长但文中并没有使用
    perimeter = cv2.arcLength(approx, True)
    perimeter = round(perimeter, 4)

    x1, y1 = approx[0][0]
    cv2.putText(img_contours, f'{area:.0f}', (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 0, 0), 10)

img_resized = cv2.resize(img_contours, (400, 400))
cv2.imshow("Contours", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('processed_image.png', img_contours)

print("Areas of selected contours:", contour_areas)
