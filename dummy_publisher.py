#!/usr/bin/env python

from std_msgs.msg import Header
from geometry_msgs.msg import PoseStamped
import rospy
import random


if __name__ == '__main__':
    try:
        rospy.init_node(name='dummy_publisher', anonymous=True)
        rate = rospy.Rate(rospy.get_param('~rate'))
        pub = rospy.Publisher('/foo', PoseStamped, queue_size=10)

        while True:
            dummy_pose = PoseStamped()
            dummy_pose.header.stamp = rospy.Time.now()
            i = random.randint(0, 42)
            if i % 3 != 0:
                pub.publish(dummy_pose)
            
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
