#! /usr/bin/env python

from scapy.all import *
import tlsh




def analyzer(x):
	global cont 
	global data_file_out
	global pktdump
	cont = cont + 1
	pktdump.write(x)
	hex_pack = str(str(x).encode("hex") + str(x).encode("hex") + str(x).encode("hex"))
	key = tlsh.hash(str(hex_pack))
	data_file_out.write( str(dst_ip) + ',' + str(cont) +','+ str(key) +'\n')

	print(cont)
	print(key)


	
pktdump = PcapWriter("packages.pcap", append=True, sync=True)
dst_ip 	= "192.168.1.13"
cont = 0
data_file_out = open('hashes.txt', 'w') 
sniff(prn = analyzer, count = 0, filter = str("host " + str(dst_ip)))
data_file_out.close()
