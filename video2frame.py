import cv2
import numpy as np
import colorList
import os
import logging
from tqdm import tqdm
import argparse
import ipdb
def LISTDIR(path):
    out = os.listdir(path)
    out.sort()
    return out
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_path', type=str, default="")
    parser.add_argument('--output_img_path', type=str, default="")
    parser.add_argument('--type', type=str, default="original")
    config = parser.parse_args()
    for num_file in LISTDIR(config.video_path):
        full_path = os.path.join(config.video_path, num_file)
        for video_file in LISTDIR(full_path):
            full_path_2 = os.path.join(full_path, video_file)
            for video_file in LISTDIR(full_path_2):
                video_path = os.path.join(full_path_2, video_file)
                if video_path.split(".")[-1] == 'avi':
                    vidcap = cv2.VideoCapture(video_path)
                    success,image = vidcap.read()
                    count = 0
                    success = True
                    write_path = os.path.join(config.output_img_path,"/".join(video_path.split("/")[1:-1]), config.type)
                    os.makedirs(write_path)
                    while success:
                        #ipdb.set_trace()
                        image = cv2.resize(image, (720, 540), cv2.INTER_CUBIC)
                        #ipdb.set_trace()
                        if count<10:
                            cv2.imwrite(write_path+"/frame00%d.jpg" % count, image) 
                        elif count < 100 and count > 9:
                            cv2.imwrite(write_path+"/frame0%d.jpg" % count, image)
                        elif count > 99: 
                            cv2.imwrite(write_path+"/frame%d.jpg" % count, image)
                        count += 1 
                        success,image = vidcap.read()