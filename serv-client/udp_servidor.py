# Enrique Adrian Gonzalez Martinez
# programa que crea un servidor udp en la ip y puerto indicada
# 24/10/2020  10:33 a.m.
import socket

direccion = ('127.0.0.1', 2000)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
    servidor.bind(direccion)
    while True:
        recivido = servidor.recvfrom(1024)
        mensaje = recivido[0].decode()
        ip = recivido[1]
        print("Cliente", ip, ":", mensaje)
        mensaje2 = input("Servidor: ")
        servidor.sendto(mensaje2.encode("utf-8"), ip)