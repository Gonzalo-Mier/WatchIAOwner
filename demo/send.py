#!/usr/bin/env python

#########################################################
#							#
#  The program send.py send the temperature through	#
#  the protocol IP/TCP in raw data to dst_ip.		#
#  The temperature is simulated by a sinus with the 	#
#  the range of the temp, plus the mean temp plus 	#
#  a noise						#
#							#
#########################################################


from scapy.all import *
from random import random
from math import sin, floor

# sender function create a package with the temp
def sender(message):
	# Split the temp in decimal and integer parts
	x1 = floor(message) 
	x2 = (message-x1)*100
	# Transform the ints to string to send it
	line = str(unichr(int(x1)))+","+str(unichr(int(x2)))
	# Create the package
	sendp(Ether()/IP(dst=dst_ip)/TCP()/line)
	print(line)

# Temp_reader function simulates the output of a temp sensor
def Temp_reader(t):
	Temp_mean = 20;
	Temp_range = 10;
	Temp_noise = 0.3;	
	Temp = round(Temp_mean + (sin(t)*0.5)*Temp_range + (2*random()-1)*Temp_noise,2)
	return Temp


t=0
# IP destination
dst_ip ="192.168.1.16"
i = 1
# Infinite loop
while i <= 3:
	# Read the temp and send it
	T = Temp_reader(t)
	sender(T)
	t = t + 0.01

