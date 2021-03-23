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
import time
import math
import os
import random

#whole_program_run = time.time()
#counter=30
#x = 0
#timer_list = []
start_time = time.time()
counter=10
while counter > 0:
    HEADER_LENGTH = 1000
    IP = "192.168.1.71"
    PORT = 1234
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))
    #start_time=time.time()
    #print(start_time)
    client_socket.send(b"{0:'raspberry1',1:'raspberrypi',2:'nfcDemo'}")
 

    #while True:
            #try:
                #while True:
    msg = client_socket.recv(1000).decode('utf-8')
    #end_time = time.time() #test end time
    #print(end_time) #test end time
    #print((end_time - start_time)) ##print elapse_time
    #print(msg)
    if msg=='ON':
        print("LED on")
        GPIO.output(21,GPIO.HIGH)         
    elif msg=='OFF':
        print("LED off")
        GPIO.output(21,GPIO.LOW)          

    #sys.exit()
#                        
#            except IOError as e:
#                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
#                    print('Reading error: {}'.format(str(e)))
#                    sys.exit()
#
#                # We just did not receive anything
#                continue
#
#            except Exception as e:
#                # Any other exception - something happened, exit
#                print('Reading error: '.format(str(e)))
#                sys.exit()
#    counter-=1
#    if counter == 0:
#        x +=1
#        counter = 30
#        timer_list.append(time.time() - start_time)
#        start_time = time.time()
#    if x == 3:
#        break
#print(timer_list)
#print("total program runtime: ", time.time() - whole_program_run)

#######################################
#start_time = time.time()
#counter=30
#while counter > 0:
#    HEADER_LENGTH = 100
#    IP = "192.168.43.229"
#    PORT = 1234
#    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    client_socket.connect((IP, PORT))
#    #start_time=time.time()
#    #print(start_time)
#    client_socket.send(b"{0:'raspberry1',1:'raspberrypi',2:'nfcDemo'}")
# 
#
#    #while True:
#            #try:
#                #while True:
#    msg = client_socket.recv(1000).decode('utf-8')
#    #end_time = time.time() #test end time
#    #print(end_time) #test end time
#    #print((end_time - start_time)) ##print elapse_time
#    #print(msg)
#    if msg=='ON':
#        print("LED on")
#        GPIO.output(21,GPIO.HIGH)         
#    elif msg=='OFF':
#        print("LED off")
#        GPIO.output(21,GPIO.LOW)          
#
#    #sys.exit()
##                        
##            except IOError as e:
##                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
##                    print('Reading error: {}'.format(str(e)))
##                    sys.exit()
##
##                # We just did not receive anything
##                continue
##
##            except Exception as e:
##                # Any other exception - something happened, exit
##                print('Reading error: '.format(str(e)))
##                sys.exit()
    counter-=1
print("Execution time: ", time.time() - start_time)