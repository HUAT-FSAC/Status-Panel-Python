#!/usr/bin/python
# coding:utf-8

import rospy
import web
import math
import json
from common_msgs.msg import HUAT_ASENSING

class VehicleData():
    json_data = "{}"
    imu_v_n = 0
    imu_v_e = 0
    imu_v_g = 0
    imu_v = 0
    imu_lat = 0
    imu_lon = 0

    def __init__(self):
        pass

    def imu_upload(self, data):
        self.imu_v_n = data.north_velocity
        self.imu_v_e = data.east_velocity
        self.imu_v_g = data.ground_velocity

        self.imu_v = math.sqrt(math.pow(self.imu_v_n, 2) + math.pow(self.imu_v_e, 2) + math.pow(self.imu_v_g, 2))
        self.imu_lat = data.latitude
        self.imu_lon = data.longitute
        self.download()

    def download(self):
        #TODO return jsonlifed data of self
        self.json_data = json.dumps(self.__dict__)

def imu_callback(data):
    # rospy.loginfo(data.north_velocity)
    vehicleData.imu_upload(data)

if __name__ == "__main__":
    vehicleData = VehicleData()
    rospy.init_node("status_panel")
    rospy.Subscriber("/INS/ASENSING_INS", HUAT_ASENSING, imu_callback)
    web.run()

    rospy.spin()


