#! /usr/bin/env python3

import rospy
import numpy as np
from sensor_msgs.msg import LaserScan

def callback(msg):
    # this code is for counting the missing data
    # count = 0
    # x = msg.ranges
    # for item in x:
    #     if str(item) == 'nan':
    #         count= count + 1  
    
    # print(count)
    # this code is for removing them and dividing them 
    x=msg.ranges
    y = list(x)
    z = []
    for item in x:
        if str(item) != 'nan':
          z.append(item)

    p = tuple(z)
    print(len(p)) 

rospy.init_node('length_range')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()