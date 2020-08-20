#!/usr/bin/env python3
# -*- coding: utf-8 -*

import UdpClient

def listen_enter(opts, vars):
    pass

def update(event, board, opts, vars):    
    #print('time    = %d' %event.time)
    #print('data    = %s' %str(event.data))

    data = event.data

    emotion = max(data.keys(), key=(lambda key: data[key]))
   
    #print("{\"emotion\":\"" + emotion + "\"}")

    UdpClient.send(str.encode("{\"emotion\":\"" + emotion + "\"}"))

   
def listen_flush(opts, vars):
    pass