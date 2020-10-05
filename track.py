import cv2
import sys

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
print(major_ver, minor_ver, subminor_ver)

if __name__ == '__main__':
    # 创建跟踪器
    tracker_type = 'MIL'
    tracker = cv2.TrackerMIL_create()
    # 读入视频
    video = cv2.VideoCapture("track_data/airplane.avi")
    # 读入第一帧
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    # 定义一个bounding box
    bbox = (287, 23, 86, 320)
    bbox = cv2.selectROI(frame, False)
    # 用第一帧初始化
    ok = tracker.init(frame, bbox)
    c = 1
    while True:
        ok, frame = video.read()
        if not ok:
            break
        # Start timer
        timer = cv2.getTickCount()
        # Update tracker
        ok, bbox = tracker.update(frame)
        # Cakculate FPS
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        # Draw bonding box

        if ok:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
            cv2.imwrite('track_done/track_img/track_img_' + str(c) + '.jpg', frame)
            c = c + 1
        # else:
        # cv2.putText(frame, "Tracking failed detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        # 展示tracker类型
        # cv2.putText(frame, tracker_type + "Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
        # 展示FPS
        # cv2.putText(frame, "FPS:" + str(fps), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
        # Result
        cv2.imshow("Tracking", frame)
        '''fps = video.get(cv2.CAP_PROP_FPS)
        frameCount = video.get(cv2.CAP_PROP_FRAME_COUNT)
        size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        videoWriter = cv2.VideoWriter('track_done/track_airplane.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, size)'''

        # Exit
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
