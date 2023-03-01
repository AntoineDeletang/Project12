#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist 


def callback(data):
    rospy.loginfo('%s', data.data)
    if(data.data == "good"):
        pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size = 1)
        msg = Twist()
        msg.linear.x = 1
        for i in range(0,3):
            pub.publish(msg)
            rospy.sleep(1)
        while not rospy.is_shutdown():
            rospy.sleep(1)
   

        
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('chatter', String, callback)


    #spin() simply keeps python from exiting until this node is stopped
    rospy.spin()



if __name__ == '__main__':
    listener()

