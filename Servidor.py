# -*- coding: utf-8 -*-
"""
Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
Método de Christian para la sincronización de relojes
Implementación a través de ZeroMQ
"""
from datetime import datetime
import zmq
import random

context=zmq.Context() 
socket=context.socket(zmq.REP)
string=socket.bind("tcp://*:4595")


while True:
    solicitudP=socket.recv()
    print (solicitudP.decode('utf-8'))
    print("Solicitud de tiempo recibida satisfactoriamente")
    
    tiempoS=datetime.now().strftime("%H:%M:%S")
    socket.send(tiempoS.encode('utf-8'))
    

