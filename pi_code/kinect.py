from freenect import sync_get_depth as scan, sync_get_video as get_vid
import cv2
import frame_convert2
import warnings


def main():
    print("Kinect Test Code")

    depth_sum = 0
    sum_right = 0
    sum_left = 0
    thresh = 500

    data = scan()
    # print("{0} x {1}".format(len(data[0]), len(data[0][0])))
    # print(data[0])
    # print(data[0][-1])

    pc_data = data[0][len(data[0]) // 2::]
    for i in range(len(pc_data) - 1):
        for j in range(len(pc_data[0]) - 1):
            if pc_data[i][j] < thresh:
                if j < (len(pc_data[0]) - 1) // 2:
                    sum_left += 1
                    # depth_sum -=pc_data[i][j]
                else:
                    sum_right += 1 
                    # depth_sum += pc_data[i][j]

    # print("\n\n\n\n\nDepth Sum: {}".format(depth_sum))
    print("\n\n\n\n\n\n")
    if sum_right > 0: 
    # if depth_sum > thresh:
        print("Rover should turn left")
    elif sum_left > 0:
    # elif depth_sum < (0 - thresh):
        print("Rover should turn right")
    elif sum_right == 0 and sum_left == 0:
    # else:
        print("Rover should continue forward")



if __name__ == "__main__":
    warnings.filterwarnings('ignore', '.*invalid magic.*', )
    main()