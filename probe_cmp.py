#!/usr/bin/python3
import os
import sys
from ffprobe import FFProbe

rootdir = os.getcwd()
rootfiles = os.listdir(rootdir)

#print(rootfiles)
#print("Files count: ", len(rootfiles))

for file_index in range(len(rootfiles)):
    file_len = len(rootfiles[file_index])
    if (rootfiles[file_index][file_len-4:file_len] == ".mp4") or (rootfiles[file_index][file_len-4:file_len] == ".mkv"):
        #print("mp4 : yes")
        metadata = FFProbe(rootfiles[file_index])
        #print(metadata.streams[0].duration)
        time = int(float(metadata.streams[0].duration))
        time_s = time % 60
        time = time - time_s
        time_m = int(time / 60)
        time_h = int((time_m - (time_m % 60))/60)
        time_m = time_m % 60

        if time_m <10:
            time_m = "0"+str(time_m)
        if time_s <10:
            time_s = "0"+str(time_s)
        time_hms = "["+str(time_h)+"-"+str(time_m)+"-"+str(time_s)+"]"
        print(time_hms, rootfiles[file_index])

    file_index = file_index+1
