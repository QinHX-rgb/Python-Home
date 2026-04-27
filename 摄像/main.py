import cv2
import os
import datetime

def main():
    # 1. 加载 OpenCV 自带的预训练人脸检测模型 (Haar Cascade)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 2. 打开电脑的默认摄像头 (数字 0 表示默认摄像头)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("错误：无法打开摄像头。")
        return

    print("摄像头已开启。按 's' 开始录制，按 'p' 停止录制，按 'q' 键退出程序。")

    # 创建保存视频的文件夹
    output_dir = '摄像/videos'
    os.makedirs(output_dir, exist_ok=True)

    is_recording = False
    video_writer = None

    while True:
        # 3. 逐帧读取摄像头的画面
        ret, frame = cap.read()

        if not ret:
            print("无法获取画面帧。")
            break

        # 4. 将彩色图像转换为灰度图像 (人脸检测模型在灰度图上运行更快、更准确)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 5. 进行人脸检测
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # 6. 遍历检测到的所有人脸数据
        for (x, y, w, h) in faces:
            # 在原图(彩色画面)上绘制矩形方框
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 7. 显示带有方框的实时画面
        cv2.imshow('Face Detection', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('s') and not is_recording:
            is_recording = True
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            video_path = os.path.join(output_dir, f"video_{timestamp}.avi")
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            video_writer = cv2.VideoWriter(video_path, fourcc, 20.0, (frame.shape[1], frame.shape[0]))
            print(f"开始录制，视频将保存至 {video_path}")

        elif key == ord('p') and is_recording:
            is_recording = False
            if video_writer:
                video_writer.release()
                video_writer = None
                print("录制结束。")

        elif key == ord('q'):
            if is_recording:
                video_writer.release()
                print("程序退出，录制已保存。")
            break
        
        if is_recording and video_writer:
            video_writer.write(frame)


    # 9. 释放摄像头资源，关闭所有显示窗口
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
