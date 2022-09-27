#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray

def clbk(msg):
	print(len(msg.data))


rospy.init_node('object_data')
sub = rospy.Subscriber('/objects', Float32MultiArray, clbk)
rospy.spin()

