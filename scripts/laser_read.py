#! /usr/bin/env python3

import rospy

from sensor_msgs.msg import LaserScan

def clbk_laser(msg):
    # 720 / 5 = 144
    regions = [
        min(msg.ranges[0:29]),
        min(msg.ranges[30:59]),
        min(msg.ranges[60:99]),
        min(msg.ranges[100:125]),
        min(msg.ranges[126:140]),
    ]
    rospy.loginfo(regions)

def main():
    rospy.init_node('reading_laser')

    sub = rospy.Subscriber('/bunny/laser/scan', LaserScan, clbk_laser)

    rospy.spin()

if __name__ == '__main__':
    main()