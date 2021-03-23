#REFERENCES:
#https://pythonprogramming.net/client-chatroom-sockets-tutorial-python-3/
#https://realpython.com/python-sockets/

#############################################!!!IMPORTANT!!!#############################################
#allow 1234 port on BOTH raspberry pi and PC server. For that, on linux command line, type :sudo ufw allow 1234
#########################################################################################################
import socket
import select
from ast import literal_eval
import os
import random
import errno
import sys


LENGTH = 1000
IP = '192.168.1.71'
PORT = 1234
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()
socket_list = [server_socket]
clients = {}


def receive_message(client_socket):
    try:            
        message = client_socket.recv(LENGTH)
        if not len(message):
            return False
        message = message.decode('utf-8')
        return {"data": message}

    except:
        return False
        


while True:
        read_sockets, _, execption_sockets = select.select(socket_list, [], socket_list)
        for notified_socket in read_sockets:
            if notified_socket == server_socket:

                # with context.wrap_socket(server_socket, server_side=True) as server_socket:
                client_socket, client_address = server_socket.accept()
                device = receive_message(client_socket)
                print(device)
                if device is False:
                    continue

                msg = literal_eval(device["data"])
                
                socket_list.append(client_socket)
                save_msg = {"data":msg}
                clients[client_socket] = save_msg

                print("New connection from {client_address[0]}:{client_address[1]} device id:{msg[0]}, device type:{msg[1]}, key:{msg[2]}")
                client_socket.sendall(b"connection success!\n")

            else:
                message = receive_message(notified_socket)
                
                client = clients[notified_socket]['data'][0]

                if message is False:
                    print("Closed connection from {client}")
                    socket_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue


                else:
                    
                    device_overall_msg = literal_eval(message["data"])
                    print(device_overall_msg);
                    from_device_id = device_overall_msg[0]
                    to_device_id = device_overall_msg[1]
                    sent_message = device_overall_msg[2]

                    from_device_key = ''
                    to_device_key = ''

                    from_device_type = ''
                    to_device_type = ''

                    from_socket = ''
                    to_socket = ''

                    print("Received message from {from_device_id} to {to_device_id}, message: {sent_message}")

                    for client_socket in clients:
                        saved_device = clients.get(client_socket)
                        device_data = saved_device["data"]

                        if device_data[0] == from_device_id:
                            from_device_type = device_data[1]
                            from_device_key = device_data[2]
                            from_socket = client_socket

                        elif device_data[0] == to_device_id:
                            to_device_type = device_data[1]
                            to_device_key = device_data[2]
                            to_socket = client_socket

                    if from_device_key == to_device_key and from_device_type == 'phone' and to_device_type == 'raspberrypi':
                        to_socket.send(bytes(sent_message,'utf-8'))
                        from_socket.send(b"data sent!\n")
                    else:
                        from_socket.send(b"device not connected with the server\n")

        for notified_socket in execption_sockets:
            socket_list.remove(notified_socket)
            del clients[notified_socket]
    
