#! /usr/bin/env python3 

import rospy 
import sys
from sensor_msgs.msg import LaserScan

rospy.init_node("LaserScan_node")
msg = rospy.wait_for_message("/scan", LaserScan)
print(sys.getsizeof(msg))