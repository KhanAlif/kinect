#! /usr/bin/env python3

import rospy 
# from tf2_msgs.msg import TFMessage 
import numpy as np
from nav_msgs.msg import Odometry  
from tf.transformations import euler_from_quaternion

rospy.init_node("extra_message_node")

msgtf = rospy.wait_for_message("/tf", TFMessage)
print("Full message: \n")
x = msg.transforms[0].translation.z
y = msg.transforms[0].translation.x