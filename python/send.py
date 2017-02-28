#!/usr/bin/env python

from scapy.all import *
from random import random
from math import sin, floor

def sender(message):
	x1 = floor(message)
	x2 = (message-x1)*100
	line = str(unichr(int(x1)))+","+str(unichr(int(x2)))
	sendp(Ether()/IP(dst="10.66.0.92")/ICMP()/line)
	print(line)
	
	#p=sendp(Ether()/IP(dst="127.0.0.1")/ICMP()/"Prueba")

def Temp_reader(t):
	Temp_av = 20;
	Temp_range = 10;
	Temp_noise = 0.3;	
	Temp = round(Temp_av + (sin(t)*0.5)*Temp_range + (2*random()-1)*Temp_noise,2)
	return Temp


t=0

i = 1
while i <= 3:
	T = Temp_reader(t)
	sender(T)
	t = t + 0.01

