#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
from ros_basics_tutorials.msg import iotSensor
import random

def iot_sensor_info():

	pub = rospy.Publisher('iot_sensor', iotSensor, queue_size=10)

	rospy.init_node('iot_sensor_pub_node', anonymous=True)
	
	rate = rospy.Rate(1) 

	i = 0
	while not rospy.is_shutdown():
		iot_sensor = iotSensor()
		iot_sensor.id = i
		iot_sensor.name = 'iot_parking_' + str(i)
		iot_sensor.temperature = 24.33 + (random.random() * 2)
		iot_sensor.humidity = 33.41 + (random.random() * 2)

		rospy.loginfo('Publicacao:')
		rospy.loginfo(iot_sensor)
		rospy.loginfo('='*100)

		pub.publish(iot_sensor)
		rate.sleep()

		i+=1

		
if __name__ == '__main__':

	try:
		iot_sensor_info()

	except rospy.ROSInterruptException:
		pass