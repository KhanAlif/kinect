#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Vector3
import tf 

def clbk(msg):
	print(msg)
	print(ok)


rospy.init_node('object_pose')
sub = rospy.Subscriber('/tf', Vector3, clbk)
rospy.spin()