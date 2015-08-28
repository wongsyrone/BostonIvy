# !/usr/bin/python
# -*- coding: UTF-8 -*-

__author__ = 'fp'

import paho.mqtt.client as mqtt


class MQTTClient(object):

    client = None

    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect('127.0.0.1',1883,60)
        pass

    # callback of function connect()
    def on_connect(self,client, userdata, flags, rc):
        # print 'userdata', userdata
        # print 'flag', flags
        # print 'rc', str(rc)
        '''
        userdata None
        flag {'session present': 0}
        rc 0
        '''

        # subscribe the topic /s2c (server to client)
        self.client.subscribe('/s2c')
        pass

    # callback of coming message
    def on_message(self, client, userdata, msg):
        print msg.payload
        pass

if __name__ == '__main__':
    a = MQTTClient()
    a.client.loop_forever()