#REFERENCES : https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins
#https://pythonprogramming.net/client-chatroom-sockets-tutorial-python-3/
#https://realpython.com/python-sockets/

#####################################!!!!!IMPORTANT!!!!!!##############################################
#This is the PYTHON 3 code for the Raspberry PI client. To run this code, raspberry PI should have PYTHON 3 and it should be connected 
#to the same local network. 

#set the IP variable below to the IP of your PC where server.py runs. To find the PC IP address, run ifconfig on Linux/Mac PC or ipconfig on 
#windows PC

#To run this, open terminal on the project directory and enter: python client_raspberry.py

#when using with RPi uncomment following four lines and the lines on the while loop to turn lights ON and OFF
#######################################################################################################

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)
import errno
import sys
import socket
import ssl
import pprint
import itertools
import time
import math

start_time = time.time()
counter=100
while counter > 0:

    def start_client_side_TLS():
        HOST = '192.168.1.71'
        PORT = 1234
        pemServer = 'server4096.pem'
        keyClient = 'client4096.key'
        pemClient = 'client4096.pem'

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(1);
        sock.connect((HOST, PORT))

        context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
        context.verify_mode = ssl.CERT_REQUIRED
        context.load_verify_locations(pemServer)
        context.load_cert_chain(certfile=pemClient, keyfile=keyClient)

        if ssl.HAS_SNI:
            secure_sock = context.wrap_socket(sock, server_side=False, server_hostname=HOST)
        else:
            secure_sock = context.wrap_socket(sock, server_side=False)

        cert = secure_sock.getpeercert()
        print(pprint.pformat(cert))
        print(secure_sock.cipher())

        # verify server
        if cert != cert: raise Exception("ERROR")
        #secure_sock.send(b"{0:'raspberry1',1:'raspberrypi',2:'nfcDemo'}")
        secure_sock.sendall(b'hello server')
        receive_data=secure_sock.read(1024)
        secure_sock.write(receive_data)
        print(receive_data)

    

    counter-=1
print("Execution time: ", time.time() - start_time)

start_client_side_TLS()
#    counter=2
#    while counter > 0:
#        while True:
#                try:
#                    while True:
#                        msg = secure_sock.recv(1000).decode('utf-8')
#                        end_time = time.time() #test end time
#                        print(end_time) #test end time
#                        print((end_time - start_time)) ##print elapse_time
#                        print(msg)
#                        if msg=='ON':
#                            print("LED on")
#                            GPIO.output(21,GPIO.HIGH)         
#                        elif msg=='OFF':
#                            print("LED off")
#                            GPIO.output(21,GPIO.LOW)          
#
#                        sys.exit()
#                            
#                except IOError as e:
#                    if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
#                        print('Reading error: {}'.format(str(e)))
#                        sys.exit()
#
#                    # We just did not receive anything
#                    continue
#
#                except Exception as e:
#                    # Any other exception - something happened, exit
#                    print('Reading error: '.format(str(e)))
#                    sys.exit()
#        counter-=1
#
#    secure_sock.close()
#    sock.close()
#    
#start_client_side_TLS()



 
