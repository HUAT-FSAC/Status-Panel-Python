#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import rospy, json
from common_msgs.msg import HUAT_ASENSING, vehicle_status
from VehicleData import VehicleData

# TODO improve logic here
def imu_callback(data):
    vData.imu_upload(data)
    json_data = json.dumps(vData.__dict__)
    write(json_data)


def vcu_callback(data):
    vData.vcu_upload(data)

def write(data):
    with open("data.json", "w+") as f:
        f.write(data)


if __name__ == "__main__":
    vData = VehicleData()
    rospy.init_node("status_panel")
    rospy.Subscriber("/INS/ASENSING_INS", HUAT_ASENSING, imu_callback)
    # rospy.Subscriber("/vehicleStatus", vehicle_status, vcu_callback)
    # not sure the real topic name

    rospy.spin()


