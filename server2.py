import socket
import sys
import desv4s
import desv4k
import math
# sys.float_info.max

from desv4s import *
from desv4k import *

server_address = ('', 11000)

keya = 3
keyq = 353

hm = input('Masukkan random key: ')
print >> sys.stderr, 'starting up on %s port %s' % server_address

hasil = (keya ** hm) % keyq
hasil3 = str(hasil)
print hasil
cekpoin = 0
while True:
    cekpoin += 1
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    sock.bind(server_address)
    sock.listen(1)

    # Wait for a connection
    # print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    if cekpoin==1:
        connection.sendall(hasil3)
        datu = connection.recv(10)
        print datu
        hasill = (int(datu) ** hm) % keyq
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

    try:
        print >>sys.stderr, 'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(150)
            print >> sys.stderr, 'data enkripsi "%s"' % data
            with open('terima.txt', 'wb') as f:
                data1 = f.write(data)
            execfile("desv4s.py")
            with open('dekrip.txt', 'rb') as file:
                data2 = file.read()
            print >>sys.stderr, 'received "%s"' % data2
            if data2:
                message = raw_input('Risma : ')
                with open('kirim.txt', 'wb') as f:
                    data3 = f.write(message)
                execfile("desv4k.py")
                with open('kirimen.txt', 'rb') as file:
                    data4 = file.read()
                print >> sys.stderr, 'sending "%s"' % message
                #print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data4)
            else:
                print >>sys.stderr, 'no more data from', client_address
            break
    finally:
        # Clean up the connection
        connection.close()