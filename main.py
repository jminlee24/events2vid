import video

def get_events(path:str)->dict:
    """ Opens events file and returns array containing the events """
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

if __name__ == "__main__":
    event_data = get_events('normal.txt')
    video.create_video(event_data, "output.mp4")
    event_data = get_events('warped.txt')
    video.create_video(event_data, "wtf.mp4")
