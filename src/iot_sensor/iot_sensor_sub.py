#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from ros_basics_tutorials.msg import iotSensor
# import random


def callback(message):
	rospy.loginfo('NAME ==========> %s', message.name)
	rospy.loginfo('TEMPERATURA ===> %s', message.temperature)


def iot_sensor_sub():
	
	rospy.init_node('iot_sub', anonymous=True)
	rospy.Subscriber('iot_sensor', iotSensor, callback)

	rospy.spin()




if __name__ == '__main__':
	try:
		iot_sensor_sub()

	except rospy.ROSInterruptException:
		pass