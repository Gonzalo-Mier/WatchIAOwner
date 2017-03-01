#!/usr/bin/env python

from scapy.all import *
from random import random
from math import sin, floor

#########################################################
#							#
#  The program get_normal.py get de data base of hashes	#
#      and compute the parameters of the normal		#
#  	  	   distribution.			#
#							#
#########################################################


# The function normal_calculus use a data vector to compute
# the parameters and save them on a file
def normal_calculus(x):
	global dst_ip
	global data_file_out
	# Compute the median
	media = f_median(x)
	# Compute the variance
	var = f_variance(x, median)
	print(median)
	print(var)
	# Write de parameters on a file
	data_file_out.write(dst_ip+ ','+ str(median) +','+ str(var) +'\n')


# The function f_median get the median of a data vector 'data'
def f_median(data):
	Median = 0
	if len(data)>0:
		for i in data:
			Median += i
		return Median / len(data)
	else:
		return 0

# The function f_median get the variance of a data vector 'data'
def f_variance(data, median):
	var = 0
	for i in data:
		var += (median - float(i))**2
	var = float(var)/len(data)
	return var




dst_ip = []
hashes = []
# Open the data base of hashes (produced by received.py)
infile = open('hashes.txt', 'r')
# Read the file by lines
infile.readline()
for line in infile:
	# The space of the hash could be blank, so we have to make this comprobation
	try:
		hash_n = line.split(",")
		# If dst_ip is not selected yet, get it
		if not dst_ip:
			dst_ip = hash_n[0]
			print(dst_ip)
		# Only use the hashes of the first IP of the data base
		# Pass the hash (hex) to int and divide it to make it easy to handle
		elif dst_ip != hash_n[2]:
			hash_n = hash_n[2].split("\n")
			hash_n = hash_n[0]
			hash_n = int(hash_n, 16)/(10.0**84)
			hashes.append(hash_n)
		else:
			pass
	except:
		pass
# open the file 'datos_normal.txt' to save the parameters
data_file_out = open('datos_normal.txt', 'w') 
# Use the normal_calculus function
normal_calculus(hashes)
# Close the files
data_file_out.close()
infile.close()

