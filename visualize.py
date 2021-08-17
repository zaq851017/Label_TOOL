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
    parser.add_argument("--input_path")
    args = parser.parse_args()
    for num_files in LISTDIR(args.input_path):
        full_path = os.path.join(args.input_path,num_files)
        for dir_files in LISTDIR(full_path):
            full_path_2 = os.path.join(full_path,dir_files)
            mask_path = os.path.join(full_path_2, "mask")
            origin_path = os.path.join(full_path_2, "original")
            heat_path = os.path.join(full_path_2, "heat")
            merge_path = os.path.join(full_path_2, "merge")
            if not os.path.isdir(heat_path):
                os.makedirs(heat_path)
            for files in LISTDIR(origin_path):
                origin_files = os.path.join(origin_path, files)
                mask_files = os.path.join(mask_path, files.split(".")[0]+"_out.jpg")
                origin_img = cv2.imread(origin_files)
                mask_img = cv2.imread(mask_files) / 255
                heatmap = np.uint8(110 * mask_img)
                heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_HOT)
                heat_img = heatmap*0.6+origin_img
                merge_img = np.hstack([origin_img, heat_img])
                cv2.imwrite(os.path.join(merge_path, files), merge_img)
                cv2.imwrite(os.path.join(heat_path, files), heat_img)