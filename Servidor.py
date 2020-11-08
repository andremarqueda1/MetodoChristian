# -*- coding: utf-8 -*-
"""
Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
Método de Christian para la sincronización de relojes
Implementación a través de ZeroMQ
"""
from datetime import datetime
import zmq
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

context=zmq.Context() 
socket=context.socket(zmq.REP)
string=socket.bind("tcp://*:5555")
tiempoS=datetime.now()

print(type(tiempoS))
"""
while True:
    Pmessage=socket.recv()
    print("Received request:" + Pmessage.decode('utf-8'))
    socket.send()
"""
