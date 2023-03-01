#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist 

rospy.init_node('bot')

def movement():
    pub = rospy.Publisher ("/cmd_vel", Twist, queue_size = 1)
    msg = Twist()
    msg.linear.x = 1
    for i in range (0,3):
        pub.publish(msg)
        rospy.sleep(1)
    msg.linear.x = 0 
    rospy.sleep(1)
    for i in range(0,1):
        pub.publish(msg)
        rospy.sleep(1)

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    #while not rospy.is_shutdown():
    for i in range(0,10):
        hello_str = "hehe"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    movement()
    talker()

#pub = rospy.Publisher ("canal", String, queue_size = 10)
#rate = rospy.Rate(10) # 10hz
#good_str = "good"
#pub.publish(good_str)
