#! /usr/bin/env python

#########################################################
#							#
#  The program receiver.py sniff all the traffic	#
#  that go or come to dst_ip, and save a data base 	#
#  of the hash of the packet when tlsh is applied.	#
#  This base save an example of good behaviour		#
#							#
#########################################################


from scapy.all import *
import tlsh

# Analyzer function get a package, save in Pcap format and compute the hash
def analyzer(x):
	global cont 
	global data_file_out
	global pktdump
	cont = cont + 1
	# Save the packet
	pktdump.write(x)
	# Write 3 times the package to fulfill the hash input
	hex_pack = str(str(x).encode("hex") + str(x).encode("hex") + str(x).encode("hex"))
	# Compute the hash	
	key = tlsh.hash(str(hex_pack))
	# Save the hash
	data_file_out.write( str(dst_ip) + ',' + str(cont) +','+ str(key) +'\n')
	# Show that the code is receiving packages
	print(cont)
	print(key)
	#x.show()


	
# Open a Pcap doc to save the packages
pktdump = PcapWriter("packages.pcap", append=True, sync=True)
# Tell to which IP send the packages
dst_ip 	= "192.168.1.15"
# Counter of packages sent
cont = 0
# Open a file to save the hashes
data_file_out = open('hashes.txt', 'w')
# Sniff packages from dst_ip and aply analyzer function 
sniff(prn = analyzer, count = 0, filter = str("host " + str(dst_ip)))
# Close the file
data_file_out.close()
