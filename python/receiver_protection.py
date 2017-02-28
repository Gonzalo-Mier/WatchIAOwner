#! /usr/bin/env python

from scapy.all import *
import scipy.stats
import tlsh




def analyzer(x):
	global media 
	global var
	global attack
	global pktdump
	hex_pack = str(str(x).encode("hex") + str(x).encode("hex") + str(x).encode("hex"))
	key = tlsh.hash(str(hex_pack))
	if not key:
		pass
	else:
		hash_k = int(key, 16)/(10.0**84)
		print(hash_k)
		prob = scipy.stats.norm(media,var).pdf(hash_k)
		print(prob)
		if prob>0.05 and prob<0.95:
			pass
		else:
			pktdump.write(x)
			print("Esta siendo atacado por la IP:")
			print(x.src)




	

attack = 0
dst_ip = "www.google.com"
media = 0
var = 0
infile = open('datos_normal.txt', 'r')
data_file_out = open('datos_normal.txt', 'w') 
pktdump = PcapWriter("packages_infected.pcap", append=True, sync=True)
lines = infile.readline()
for line in lines:
	global media
	global var
	global dst_ip
	info = line.split(",")
	dst_ip = info[0]
	print(dst_ip)
	media = info[1]
	print(media)
	info = hash_n[2].split("\n")
	var = info[0]
	print(var)
print(dst_ip)
try:
	sniff(prn = analyzer, count = 0, filter = str("host " + str(dst_ip)))
except:
	pass
data_file_out.close()
infile.close()

