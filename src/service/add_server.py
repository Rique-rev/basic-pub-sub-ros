#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ros_basics_tutorials.srv import AddTwoInts
from ros_basics_tutorials.srv import AddTwoIntsRequest
from ros_basics_tutorials.srv import AddTwoIntsResponse

import rospy


def handle_add_two_ints_response(req):
    print('Returning [%s + %s = %s]'%(req.a, req.b, (req.a + req.b)))
    return AddTwoIntsResponse(req.a + req.b)

def add_two_ints_server():
    #Iniciando um no com o nome add_two_ints_server
    rospy.init_node('add_two_ints_server')

    #Iniciando um servidor que vai começar a ouvir as request
    #nome do servidor -> add_two_ints
    #tipo de mensagem -> AddTwoInts
    #função que cuidara das requests -> handle_add_two_ints_response
    server = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints_response)

    print('Ready to add two ints')
    
    rospy.spin()

if __name__ == '__main__':
    add_two_ints_server()
