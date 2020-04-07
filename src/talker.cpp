/*
 * Copyright (C) 2008, Morgan Quigley and Willow Garage, Inc.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *   * Redistributions of source code must retain the above copyright notice,
 *     this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer in the
 *     documentation and/or other materials provided with the distribution.
 *   * Neither the names of Stanford University or Willow Garage, Inc. nor the names of its
 *     contributors may be used to endorse or promote products derived from
 *     this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

//http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29


#include "ros/ros.h" //biblioteca do ROS
#include "std_msgs/String.h" //tipo de mensagem enviada: String.h
#include <sstream>


/**
 * This tutorial demonstrates simple sending of messages over the ROS system.
 */
int main(int argc, char **argv)
{
  /*
  * Para criar um node eu preciso inicializa-lo e defenir o nome dele
  */
  ros::init(argc, argv, "talker");


  /**
   * NodeHandle -> É uma referencia ao node criado (no caso o talker)
   */
  ros::NodeHandle n;


  /**
   * Criar um Publisher com o topico chamado 'chatter' que enviará uma mensagem do tipo String
   * A função adververtise() avisa a Master que há um publisher chamado 'chatter' que está publicando mensagens do tipo String
   * 100 é o número de mensagens que podem ser acumuladas dentro do buffer antes de serem processadas
   */
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);

  /*
  * Definir quantas mensagens serão criadas por segundo
  * no caso serão criadas 1 mensagem por segundo
  * se eu quisesse enviar 100 mensagens por segundo, o código ficaria assim: ros::Rate loop_rate(100.0);
  */
  ros::Rate loop_rate(1.0);
  
  int count = 0;
  while (ros::ok()) // Isso daqui será verdadeiro até o usuário pressionar Ctrl+C
  { 
      
    //Estou criando uma variável 'msg' do tipo String que armazenará os meus dados que serão publicados
    std_msgs::String msg;

    std::stringstream ss;
    ss << "hello world " << count; 
    msg.data = ss.str(); //Estou populando a variável 'msg' com 'hello world' + 'count'

    //Printando o conteudo da mensagem no terminal
    ROS_INFO("[Talker] Eu publiquei isso: %s", msg.data.c_str());

    /**
     * The publish() function is how you send messages. The parameter
     * is the message object. The type of this object must agree with the type
     * given as a template parameter to the advertise<>() call, as was done
     * in the constructor above.
     */
    chatter_pub.publish(msg); // Poe a mensagem no Buffer

    ros::spinOnce(); //Preciso chamar essa função para habilitar o ROS processar/enviar todas as mensagens que estão no Buffer

    loop_rate.sleep(); //Dou um delay de 1 segundo (valor do loop_rate)

    ++count; //incremento a variável 'count'
  }

  return 0;
}
