#!/usr/bin/env python

import message_filters
import rospy
from geometry_msgs.msg import PoseStamped


class DummySyncActor(object):
    def __init__(self):
        
        self.sub = [message_filters.Subscriber('/foo_{}'.format(i), PoseStamped, queue_size=1) for i in range(rospy.get_param('~topics'))]
        self.sync = message_filters.ApproximateTimeSynchronizer(self.sub, 100, 0.5)
        self.pub = rospy.Publisher('/sync', PoseStamped, queue_size=10)

        self.sync.registerCallback(self.__call__)

    def __call__(self, *poses):
        self.pub.publish(poses[0])

if __name__ == '__main__':
    try:
        rospy.init_node(name='dummy_syncronizer', anonymous=True)
        a = DummySyncActor()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
