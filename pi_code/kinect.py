#!/usr/bin/env python

from freenect import sync_get_depth as scan, sync_get_video as get_vid
import cv2
import frame_convert2
import warnings
import timeit
# PID Tuning variables
kp = .5
kd = .5
ki = .5

p, i, d = 0, 0, 0

def control():
    left, right = kinect_scan()
    print("\n\n\n\n\n\n")
    print("sum_left: {}\nsum_right: {}".format(left, right))
    if right > left: 
        print("Rover should turn left")
    elif left > right:
        print("Rover should turn right")
    elif right == 0 and left == 0:
        print("Rover should continue forward")

    print("\n\n\n\n\n\n")


def kinect_scan():
    print("Kinect Test Code")

    sum_right = 0
    sum_left = 0
    thresh = 500

    data = scan()
    start = timeit.default_timer()
    pc_data = data[0][len(data[0]) // 2::]
    for i in range(len(pc_data) - 1):
        for j in range(len(pc_data[0]) - 1):
            if pc_data[i][j] < thresh:
                if j < (len(pc_data[0]) - 1) // 2:
                    sum_left += 1
                else:
                    sum_right += 1 

    end = timeit.default_timer()
    print("Total time: {}".format(end-start))
    return sum_left, sum_right


def main():
    control()

if __name__ == "__main__":
    warnings.filterwarnings('ignore', '.*invalid magic.*', )
    main()