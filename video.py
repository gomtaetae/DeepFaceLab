import os
import cv2

# 동영상 폴더 경로
video_dir = "C:/Users/직원/Downloads/UCF-101"
output_dir = "C:/Users/직원/Downloads/UCF-101/avi_files"

# 출력 폴더 생성
os.makedirs(output_dir, exist_ok=True)

# 모든 동영상 파일 처리
for video_file in os.listdir(video_dir):
    if video_file.endswith(".avi"):
        video_path = os.path.join(video_dir, video_file)
        cap = cv2.VideoCapture(video_path)

        frame_count = 0
        success, frame = cap.read()
        while success:
            frame_count += 1
            frame_filename = os.path.join(output_dir, f"{os.path.splitext(video_file)[0]}_frame_{frame_count:04d}.png")
            cv2.imwrite(frame_filename, frame)
            success, frame = cap.read()

        cap.release()

        print(f"Processed: {video_file} ({frame_count} frames)")
