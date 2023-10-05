#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import rospy, web, math, json, time, pprint
from common_msgs.msg import HUAT_ASENSING, vehicle_status

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
        self.download()

    def download(self):
        pprint.pprint(json.dumps(self.__dict__))
        web.update(json.dumps(self.__dict__))

def imu_callback(data):
    vehicleData.imu_upload(data)

def vcu_callback(data):
    vehicleData.vcu_upload(data)

if __name__ == "__main__":
    vehicleData = VehicleData()
    rospy.init_node("status_panel")
    rospy.Subscriber("/INS/ASENSING_INS", HUAT_ASENSING, imu_callback)
    # rospy.Subscriber("/vehicleStatus", vehicle_status, vcu_callback)
    # not sure the real topic name

    rospy.spin()


