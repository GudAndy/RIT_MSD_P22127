import ydlidar

class Lidar:
    name: str
    lidar_id: int

    def __init__(self):
        self.name = "YDLiDAR X4"
        self.lidar_id = 1
        ydlidar.os_init()
        ports = ydlidar.lidarPortList()
        port = "/dev/ydlidar"

        # Configure laser settings
        self.laser = ydlidar.CYdLidar()
        self.laser.setlidaropt(ydlidar.LidarPropSerialPort, port)
        self.laser.setlidaropt(ydlidar.LidarPropSerialBaudrate, 128000)
        self.laser.setlidaropt(ydlidar.LidarPropLidarType, ydlidar.TYPE_TRIANGLE)
        self.laser.setlidaropt(ydlidar.LidarPropDeviceType, ydlidar.YDLIDAR_TYPE_SERIAL)



def main():
    lidar = Lidar()
    print(lidar.name)

if __name__ == "__main__":
    main()