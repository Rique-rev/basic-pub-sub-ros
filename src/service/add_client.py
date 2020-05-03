#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import rospy
from ros_basics_tutorials.srv import AddTwoInts
from ros_basics_tutorials.srv import AddTwoIntsRequest
from ros_basics_tutorials.srv import AddTwoIntsResponse

def add_two_ints_client(x, y):

    '''
    Responsavel por preparar a request e enviar para o servidor
    '''
    #Esperar o servidor estar pronto para receber requests
    rospy.wait_for_service('add_two_ints')

    try:
        #ServiceProxy -> Responsavel por enviar a resquest para:
        #o servidor: add_two_ints
        #que possui o tipo de mensagem> AddTwoInts
        add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)

        #conectar com o servidor e enviar os parametros x e y atraves do cliente criado acima 'add_two_ints'
        resp1 = add_two_ints(x, y)

        #sum -> nome da variavel que o servidor vai retornar
        #foi definido dentro do arquivo srv/AddTwoInts.srv
        return resp1.sum


    except rospy.ServiceException as e:
        print('Service Error: %e'%e)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Params "x" "y" are missing!')

    elif len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])

        print('Requesting %s + %s'%(x,y))
        print('%s + %s = %s'%(x, y, add_two_ints_client(x, y)))
    