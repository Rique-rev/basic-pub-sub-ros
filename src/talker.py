#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Importando as bibliotecas do ROS
import rospy
from std_msgs.msg import String

'''
Quando o node é criado em Python, nós não precisamos colocar nada no arquivo CMakeList.txt
Apenas é necessário gerar um arquivo executavel do arquivo .py em questão
'''

def talker():

	#Criando topico 'chatter' que envia mensagem do tipo String 
	pub = rospy.Publisher('chatter', String, queue_size=10)

	#Iniciando o node com o nome 'talker'
	rospy.init_node('talker', anonymous=True)

	#Frequencia em que as mensagens serão publicadas
	rate = rospy.Rate(1) #1hz 1 mensagem por segundo


	while not rospy.is_shutdown():
		hello_str = 'hello from Python %s' % rospy.get_time()

		#Printando 'hello_str'
		rospy.loginfo(hello_str)

		#Publicando a variavel 'hello_str'
		pub.publish(hello_str)

		rate.sleep()


if __name__ == '__main__':

	try:
		talker()

	except rospy.ROSInterruptException:
		pass