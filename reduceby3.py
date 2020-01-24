#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32,Float32

def cb(message):
    rospy.loginfo(message.data/3.)

if __name__ == '__main__':
    rospy.init_node('halve')
    sub = rospy.Subscriber('twice', Float32, cb)
    rospy.spin()

