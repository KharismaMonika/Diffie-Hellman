import socket
import sys
import desv4
import desv4c

from desv4 import *
from desv4c import *

keya = 3
keyq = 353
# hm = 233

hm = input('Masukkan random key: ')
hasil = (keya ** hm) % keyq
hasil3 = str(hasil)
print hasil
cekpoin=0
while True:
    cekpoin+=1
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        server_address = ('localhost', 11000)
        #print >> sys.stderr, 'connecting to %s port %s' % server_address
        sock.connect(server_address)
        # Send data
        if cekpoin==1:
            data7 = sock.recv(10)
            print data7
            sock.sendall(hasil3)
            hasill = (int(data7) ** hm) % keyq
            print hasill
            hasill2 = str(hasill)
            if len(hasill2) < 8:
                oj = len(hasill2)
                while oj < 8:
                    oj += 1
                    hasill2 = hasill2 + str(oj)
            print hasill2
            with open('key.txt', 'wb') as f:
                data = f.write(hasill2)

        message = raw_input('Faishal : ')
        with open('plain.txt', 'wb') as f:
            data1 = f.write(message)
        execfile("desv4.py")
        with open('hasil.txt', 'rb') as file:
            data2 = file.read()
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(data2)
        # Look for the response
        data = sock.recv(150)
        amount_received = 0
        amount_expected = len(data)
        while amount_received < amount_expected:
            print >> sys.stderr, 'data enkripsi "%s"' % data
            with open('terima2.txt', 'wb') as f:
                data3 = f.write(data)
            execfile("desv4c.py")
            with open('dekrip2.txt', 'rb') as file:
                data4 = file.read()
            amount_received += len(data4)
            print >>sys.stderr, 'received "%s"' % data4

    finally:
        sock.close()