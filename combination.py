import cv2
import os


def video_combina():
    fps = 30.0  # 帧率
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 视频编码器
    size = (426, 240)  # 视频分辨率,与原始图片保持一致
    out = cv2.VideoWriter('dehaze_done/dehaze_video_1.avi', fourcc, fps, size)  # 定义输出文件及其它参数
    path = 'dehaze_done/dehaze_video_img'
    filenum = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
    print(filenum)
    for i in range(1, filenum):
        image_file = 'dehaze_done/dehaze_video_img/dehaze_img_'+str(i)+'.jpg'
        frame = cv2.imread(image_file)
        out.write(frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    out.release()
    cv2.destroyAllWindows()
    return out


'''import cv2
import os


fps = 15.0  # 帧率
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 视频编码器
size = (426, 240)  # 视频分辨率,与原始图片保持一致
out = cv2.VideoWriter('track_data/airplane.avi', fourcc, fps, size)  # 定义输出文件及其它参数
path = 'track_data/airplane1/img'
filenum = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
print(filenum)
for i in range(1, filenum):
    image_file = 'track_data/airplane1/img/img_'+str(i)+'.jpg'
    frame = cv2.imread(image_file)
    out.write(frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
out.release()
cv2.destroyAllWindows()'''

