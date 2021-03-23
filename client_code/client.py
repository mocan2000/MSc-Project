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


HEADER_LENGTH = 30
IP = "192.168.1.71"
PORT = 1234
#start_time=time.time()
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.send(b"{0:'raspberry1',1:'raspberrypi',2:'nfcDemo'}")

 
while True:

    try:
        while True:
            msg = client_socket.recv(1000).decode('utf-8')
            print(msg)
            if msg=='ON':
                print("LED on")
                GPIO.output(21,GPIO.HIGH)         
            elif msg=='OFF':
                print("LED off")
                GPIO.output(21,GPIO.LOW)          
               
    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error: {}'.format(str(e)))
            sys.exit()

        # We just did not receive anything
        continue

    except Exception as e:
        # Any other exception - something happened, exit
        print('Reading error: '.format(str(e)))
        sys.exit()