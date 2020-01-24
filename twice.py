#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32,Float32

pub = rospy.Publisher('twice', Float32, queue_size=1)

def cb(message):
        pub.publish(message.data*2.0)

if __name__ == '__main__':
        rospy.init_node('twice')
        sub = rospy.Subscriber('count_up', Int32, cb)
        rospy.spin()
