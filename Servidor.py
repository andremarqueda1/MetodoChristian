# -*- coding: utf-8 -*-
"""
Python 3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]
Método de Christian para la sincronización de relojes
Implementación a través de ZeroMQ
"""
import zmq
import datetime



context=zmq.Context() 
socket=context.socket(zmq.REP)
string=socket.bind("tcp://*:4595")


print ("En espera de solicitud de tiempo....")
solicitudP=socket.recv()
print (solicitudP.decode('utf-8'))
print("Solicitud de tiempo recibida satisfactoriamente")    
tiempoS=datetime.datetime.now().strftime("%H:%M:%S")
print("Enviando respuesta a P\n\t Hora del servidor:\t",tiempoS)
socket.send(tiempoS.encode('utf-8'))
print("Tiempo enviado satisfactoriamente")
    

