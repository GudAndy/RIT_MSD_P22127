from freenect import sync_get_depth as scan, sync_get_video as get_vid
import cv2
import frame_convert2

def main():
    print("Kinect Test Code")

    data = scan()
    print("{0} x {1}".format(len(data[0]), len(data[0][0])))
    print(data[0])
    print(data[0][-1])


if __name__ == "__main__":
    main()