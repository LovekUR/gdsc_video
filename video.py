
import os
import cv2
from moviepy.editor import VideoFileClip

# Directories
VIDEO_DIR = "videos"  # Folder where all your videos are stored
FRAME_DIR = "frames"  # Folder to save extracted frames
os.makedirs(FRAME_DIR, exist_ok=True)

def extract_frames(video_path, save_folder, frame_rate=1):
    """
    Extract frames from a video at the specified frame rate.
    """
    clip = VideoFileClip(video_path)
    fps = clip.fps
    frame_interval = int(fps / frame_rate)

    cap = cv2.VideoCapture(video_path)
    count = 0
    frame_count = 0

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    video_folder = os.path.join(save_folder, video_name)
    os.makedirs(video_folder, exist_ok=True)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        if count % frame_interval == 0:
            frame_path = os.path.join(video_folder, f"frame_{frame_count}.jpg")
            cv2.imwrite(frame_path, frame)
            frame_count += 1
        count += 1

    cap.release()
    print(f"Frames extracted for {video_path}")

# Process all videos in the directory
for video_file in os.listdir(VIDEO_DIR):
    if video_file.endswith(('.mp4', '.avi', '.mov')):
        extract_frames(os.path.join(VIDEO_DIR, video_file), FRAME_DIR, frame_rate=1)
