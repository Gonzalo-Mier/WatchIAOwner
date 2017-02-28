#! /usr/bin/env python

from scapy.all import *
import tlsh
from bitstring import BitArray



def analyzer(x):
	global cont 
	global data_file_out
	cont = cont + 1
	pktdump = PcapWriter("packages.pcap", append=True, sync=True)
	pktdump.write(x)
	hex_pack = str(str(x).encode("hex") + str(x).encode("hex") + str(x).encode("hex"))
	key = tlsh.hash(str(hex_pack))
	data_file_out.write(str(cont) +','+ str(key) +'\n')
	print(key)


	
	
cont = 0
data_file_out = open('hashes.txt', 'w') # Indicamos el valor 'w'.
#sniff(prn = analyzer, count = 0)

sniff(prn = analyzer, count = 0, filter = "host 10.66.0.92")
#sniff(prn = analyzer, count = 0, filter = "host 127.0.01")
data_file_out.close()
