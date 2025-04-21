import cv2
import numpy as np



def create_video(event_data, filename):
    events = event_data["events"]
    frame_width = event_data["dim"][1]
    frame_height = event_data["dim"][0]
    max_time = event_data["max"]
    fps = 30

    total_frames = max_time // (100 * fps)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))

    k = 0

    for i in range(total_frames):
        frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)
        while k < len(events) and events[k]["t"] < i * (100 * fps):
            y = events[k]["y"]
            x = events[k]["x"]
            k += 1
            if y >= frame_height or x >= frame_width:
                continue
            frame[y][x] = 255

        # Generate random pixel data for each frame
        video_writer.write(frame)
    print(total_frames)
    video_writer.release()
    


