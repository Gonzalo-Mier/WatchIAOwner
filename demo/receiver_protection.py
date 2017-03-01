#! /usr/bin/env python

from scapy.all import *
import tlsh
import math

#########################################################
#							#
#  The program receiver_protection.py sniff all the 	#
#  traffic that recieve and send the IP save on 	#
#  'datos_normal.txt' (our IoT) and analyze if each 	#
#  new package is a typical communication or an attack	#
#							#
#########################################################

# The norm_pdf compute the probability density function of a normal
def norm_pdf(x, median, var):
	pi = 3.1415926
	denom = (2*pi*var)**.5
	num = math.exp(-(float(x)-float(median))**2/(2*var))
	return num/denom

# The analyzer function predict if the new package is an attack or not
def analyzer(x):
	global median 
	global var
	global attack
	global pktdump
	# Extract the hex string from the new package
	hex_pack = str(str(x).encode("hex") + str(x).encode("hex") + str(x).encode("hex"))
	# Compute the tlsh function to extract the hash
	key = tlsh.hash(str(hex_pack))
	print(key)
	if key!="":
		# Use the same normalization constant that the receiver.py
		hash_k = int(key, 16)/(10.0**84)
		print(hash_k)
		# Compute the probability of the new hash to belong to the normal distribution
		prob=(hash_k-(media))/(media+var)
		
		#comentado para demo
		#prob = norm_pdf(hash_k, media, var)
		print(prob)
		#comentado para la demo
		#if prob<0.05 or prob>0.95:
		#	pktdump.write(x)
		#	print("Esta siendo atacado por la IP:")
		#	print(x.src)
		
		# If the algorithm are not at 90% sure about if it belongs to the normal distribution
		# the new package is considered an attack, the package is saved and the IP of the 
		# agressor is shown.
		if prob<0.05 or prob>0.95:
			pktdump.write(x)
			print("Esta siendo atacado por la IP:")
			print(x.src)

	
# Open 'datos_normal.txt' (produced by get_normal.py) 
infile = open('datos_normal.txt', 'r')
# Open the file where the attacks are going to be saved
pktdump = PcapWriter("packages_infected.pcap", append=True, sync=True)
# Extract the information of 'datos_normal.txt'
line = infile.readline() 
info = line.split(",")
# First parameter is the IP that te program are listening
dst_ip = info[0]
# Second parameter is the median of the normal distribution
median = float(info[1])
info = info[2].split("\n")
# Third parameter is the variance of the normal distribution
var = float(info[0])
# Sniff all the packages sent or received by the IP 'dst_ip' and launch the analyzer
sniff(prn = analyzer, count = 0, filter = str("host " + str(dst_ip)))
# Close the file
infile.close()

