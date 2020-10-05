import cv2
from quwu import dehaze


def video_frame(filename, rd, rz, w):
    # filename = 'dehaze_data/haze_1.mp4'
    vc = cv2.VideoCapture(filename)  # 读取视频文件
    c = 1
    if vc.isOpened():  # 判断是否正常打开
        right, frame = vc.read()
    else:
        right = False
    f = 1  # 视频帧计数间隔频率
    while right:  # 循环读取视频帧
        right, frame = vc.read()
        if c % f == 0:  # 每隔f帧进行存储操作
            frame1 = dehaze(frame / 255.0, rd, rz, w)*255
            # print(frame1)
            cv2.imwrite('D:/interface/dehaze_done/dehaze_video_img/' + 'dehaze_video_' + str(c) + '.jpg', frame1)
        c = c + 1
        cv2.waitKey(1)
    vc.release()
