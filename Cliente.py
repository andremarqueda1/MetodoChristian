# -*- coding: utf-8 -*-
"""
Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
Método de Christian para la sincronización de relojes
Implementación a través de ZeroMQ
"""

import zmq

context = zmq.Context()
from datetime import datetime
tiempoP=datetime.now()
#  Socket to talk to server
print("Conectandose al proceso S…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:4595")


print("Solicitando tiempo a S")
msg = "solicitud de tiempo"
socket.send(msg.encode('utf-8'))

    #  Get the reply.
message = socket.recv()
print("Recibiendo tiempo y realizando ajuste ",message.decode('utf-8'))