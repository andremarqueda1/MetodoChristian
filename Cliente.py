# -*- coding: utf-8 -*-
"""
Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
Método de Christian para la sincronización de relojes
Implementación a través de ZeroMQ
"""

import zmq
import datetime
import time
import random
context = zmq.Context()
print("Conectandose al proceso S…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6865")
print("Solicitando tiempo a S") 
msg = "solicitud de tiempo"
socket.send(msg.encode('utf-8'))
RTTstart=time.time() #inicio del cronómetro
tiempoPold=datetime.datetime.now()#Hora de P
        
"""
        Restando segundos aleatorios para simular una desincronización
"""
        
tiempoP=tiempoPold-datetime.timedelta(seconds=random.randint(0,9))
print("La hora actual en P previo a la sincronización es:\n",tiempoP.strftime("%H:%M:%S"))
        
        
"""
        Recibiendo respuesta del servidor S
"""
        
tiempoServidor = socket.recv().decode('utf-8') 
        
"""
        Una vez recibido la respuesta de S, podemos calcular el Round Trip Time
"""
        
RTTend=time.time()-RTTstart #fin del cronómetro calculando el Round Trip Time
print("El tiempo que entre envío de solicitud y recepción de la hora (RTT) fue de:\n\tRTT: ",RTTend)
print("Recibiendo tiempo de servidor ",tiempoServidor)
        
        
"""
        Convirtiendo el mensaje decodificado a su respectivo formato datetime para su manipulación
""" 
tiempoS=datetime.datetime.strptime(tiempoServidor, "%H:%M:%S")
        
"""
        Calculando el nuevo tiempo del proceso P
"""
tiempoP=tiempoS-(datetime.timedelta(seconds=(int(RTTend/2))))
print ("Nueva hora del proceso P\n\t", tiempoP.strftime("%H:%M:%S"))
print("""    
                            REPORTE DE SINCRONIZACIÓN
            ______________________________________________________________________________________________
            |  Tiempo original   | Comienzo de solicitud    | Promedio Trans-Rec   |     Hora ajustada    |
            |    del cliente     |     (System Clocks)      |        (RTT)         |                      |
            |----------------------------------------------------------------------|----------------------
            """)
print("\t\t",tiempoPold.strftime("%H:%M:%S"),"\t     ",round(RTTstart),"\t\t ",RTTend,"\t",tiempoP.strftime("%H:%M:%S"))
     