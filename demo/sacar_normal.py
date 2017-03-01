#!/usr/bin/env python


from random import random
from math import sin, floor




def normal_calculus(x):
	global dst_ip
	global data_file_out
	media = f_media(x)
	var = f_varianza(x, media)
#	desv = f_desviacion(var)	
	print(media)
	print(var)
#	print(desv)
	data_file_out.write(dst_ip+ ','+ str(media) +','+ str(var) +'\n')



def f_media(data):
	Media = 0
	if len(data)>0:
		for i in data:
			Media += i
		return Media / len(data)
	else:
		return 0

def f_varianza(data, media):
	var = 0
	for i in data:
		var += (media - float(i))**2
	var = float(var)/len(data)
	return var




dst_ip = []
hashes = []
infile = open('hashes.txt', 'r')
infile.readline()
for line in infile:
	try:
		hash_n = line.split(",")
		if not dst_ip:
			dst_ip = hash_n[0]
			print(dst_ip)
		elif dst_ip != hash_n[2]:
			hash_n = hash_n[2].split("\n")
			hash_n = hash_n[0]
			hash_n = int(hash_n, 16)/(10.0**84)
			hashes.append(hash_n)
		else:
			pass
	except:
		pass

data_file_out = open('datos_normal.txt', 'w') 
normal_calculus(hashes)
data_file_out.close()
infile.close()

