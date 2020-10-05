import cv2
import numpy as np


def zmMinFilterGray(src, rz):
    return cv2.erode(src, np.ones((2 * rz + 1, 2 * rz + 1)))


def guidedfilter(I, p, rd, eps):
    height, width = I.shape
    m_I = cv2.boxFilter(I, -1, (rd, rd))  # I的均值平滑
    m_p = cv2.boxFilter(p, -1, (rd, rd))  # p的均值平滑
    m_Ip = cv2.boxFilter(I * p, -1, (rd, rd))  # I*p的均值平滑
    cov_Ip = m_Ip - m_I * m_p  # 输出协方差

    m_II = cv2.boxFilter(I * I, -1, (rd, rd))  # I*I的均值平滑
    var_I = m_II - m_I * m_I  # 输出方差

    a = cov_Ip / (var_I + eps)  # 相关因子a
    b = m_p - a * m_I  # 相关因子b

    m_a = cv2.boxFilter(a, -1, (rd, rd))  # 对a进行均值平滑
    m_b = cv2.boxFilter(b, -1, (rd, rd))  # 对b进行均值平滑
    return m_a * I + m_b  # 返回导向滤波结果


def getV1(m, rs, rz, eps, w, maxV1):  # 输入rgb图像，值范围[0,1]
    '''计算大气遮罩图像V1和光照值A, V1 = 1-t/A'''
    V1 = np.min(m, 2)  # 得到暗通道图像
    V1 = guidedfilter(V1, zmMinFilterGray(V1, rz), rs, eps)  # 使用引导滤波优化
    bins = 2000
    ht = np.histogram(V1, bins)  # 计算大气光照A
    d = np.cumsum(ht[0]) / float(V1.size)
    for lmax in range(bins - 1, 0, -1):
        if d[lmax] <= 0.999:
            break
    A = np.mean(m, 2)[V1 >= ht[1][lmax]].max()

    V1 = np.minimum(V1 * w, maxV1)  # 对值范围进行限制

    return V1, A


def dehaze(m, rd, rz, w, bGamma=False):
    eps = 0.001
    maxV1 = 0.80
    Y = np.zeros(m.shape)
    Mask_img, A = getV1(m, rd, rz, eps, w, maxV1)             # 得到遮罩图像和大气光照

    for k in range(3):
        Y[:, :, k] = (m[:, :, k] - Mask_img)/(1-Mask_img/A)  # 颜色校正
    Y = np.clip(Y, 0, 1)
    if bGamma:
        Y = Y ** (np.log(0.5) / np.log(Y.mean()))       # gamma校正,默认不进行该操作
    return Y


'''if __name__ == '__main__':
    imgname = 'im_1.jpg'
    m = dehaze(cv2.imread(imgname)/255.0,rd=100,rz=7,w=0.95)*255
    print(m)
    cv2.imwrite('out1.jpg', m)'''
