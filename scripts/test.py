#! /usr/bin/env python3
import rospy
import numpy as np
from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
    x = msg.ranges
    print(len(x))

rospy.init_node("test_node")
rospy.Subscriber("/avb_bot/laser/scan", LaserScan, clbk_laser)
# rospy.Publisher("/new_scan", LaserScan, queue_size=3)
rospy.spin()
