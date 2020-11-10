# -*- coding: utf-8 -*-
"""
Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
Método de Christian para la sincronización de relojes
Implementación a través de ZeroMQ
"""

import zmq
import datetime
import random
context = zmq.Context()


print("Conectandose al proceso S…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:4595")
print("Solicitando tiempo a S")

msg = "solicitud de tiempo"
socket.send(msg.encode('utf-8'))
tiempoEnvio=datetime.datetime.now() #hora de solicitud
tiempoP=datetime.datetime.now()#Hora de P

"""
Restando segundos aleatorios para simular una desincronización
"""

tiempoP=tiempoP-datetime.timedelta(seconds=random.randint(0,9))
print("La hora actual en P previo a la sincronización es:\n",tiempoP.strftime("%H:%M:%S"))


"""
Recibiendo respuesta del servidor S
"""

message = socket.recv() #Recibiendo tiempo
"""
Una vez recibido la respuesta de S, podemos calcular el Round Trip Time
"""
tiempoRecibo=datetime.datetime.now() #Hora de recibido
roundTripTime=tiempoRecibo-tiempoEnvio
print("El tiempo que se tardó en recibir el mensaje (RTT) fue de:\n\tRTT: ",roundTripTime)
print("Recibiendo tiempo y realizando ajuste ",message.decode('utf-8'))

