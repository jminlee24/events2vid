import cv2
import numpy as np

def create_video_from_txt(in_path:str, out_path:str):
    event_data = get_events(in_path)
    create_video(event_data, out_path)

def get_events(path:str)->dict:
    """ Opens events file and returns dict containing events and additional data"""
    ret = {"max": 0, "events":[], "dim": []} 

    with open(path, encoding='utf-8') as f:
        dims = f.readline().replace('\n', '').split(" ")
        ret["dim"].append(int(dims[0]))
        ret["dim"].append(int(dims[1]))
        ret["max"] = int(f.readline().replace("\n", '').split(" ")[0])

        for i, line in enumerate(f):

            estring = line.replace('\n', '').split(' ')
            if len(estring) < 4:
                continue
            ret["events"].append({
                     "x": int(estring[0]),
                     "y": int(estring[1]),
                     "p": int(estring[2]),
                     "t": int(estring[3]),
                     })

    return ret

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
    


