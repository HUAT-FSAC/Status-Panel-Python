import rospy, math

class VehicleData():
    def __init__(self):
        self.imu_v_n = 0
        self.imu_v_e = 0
        self.imu_v_g = 0
        self.imu_v = 0
        self.imu_lat = 0
        self.imu_lon = 0
        self.imu_alt = 0
        self.vcu_steering = 0
        self.vcu_throttle = 0
        self.vcu_wheel_spd = 0

    def vcu_upload(self, data):
        self.vcu_steering = data.steering
        self.vcu_throttle = data.pedal_ratio
        self.vcu_wheel_spd = data.speed_left_front

    def imu_upload(self, data):
        self.imu_v_n = data.north_velocity
        self.imu_v_e = data.east_velocity
        self.imu_v_g= data.ground_velocity

        self.imu_v = math.sqrt(math.pow(self.imu_v_n, 2) + math.pow(self.imu_v_e, 2) + math.pow(self.imu_v_g, 2))
        self.imu_lat = data.latitude
        self.imu_lon= data.longitude
        self.imu_alt = data.altitude

    # def download(self):
    #     socket = web.connected_socket
    #     if socket != None:
    #         web.connected_socket(json.dumps(self.__dict__))
    #         print("\n\n\nFrom main(connected): ")
    #         pprint.pprint(web.connected_socket.__dict__)
    #         # web.socketio.emit("message", json.dumps(self.__dict__))
    #     else:
    #         rospy.logwarn("socket retrived is None")