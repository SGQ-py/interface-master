
import cv2
import os

fps = 16.0  # 帧率
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 视频编码器
# size = (1280, 720)  # 视频分辨率,与原始图片保持一致
size = (426, 240)
out = cv2.VideoWriter('track_done/track_2.avi', fourcc, fps, size)  # 定义输出文件及其它参数
path = 'track_data/b'
filenum = len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))])
print(filenum)
for i in range(1, filenum):
    image_file = 'track_data/b/img_'+str(i)+'.jpg'
    frame = cv2.imread(image_file)
    out.write(frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
out.release()
cv2.destroyAllWindows()
