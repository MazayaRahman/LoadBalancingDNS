import sys
import socket as mysoc
import threading
import select

# server task
def server(lsPort, ts1Host, ts1Port, ts2Host, ts2Port):
    try:
        ss=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[S]: Server socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))

    lsPort = int(lsPort)
    ts1Port = int(ts1Port)
    ts2Port = int(ts2Port)
    server_binding=('',lsPort)
    ss.bind(server_binding)
    ss.listen(1)
    host=mysoc.gethostname()

    print("[S]: Server host name is: ",host)
    localhost_ip=(mysoc.gethostbyname(host))
    print("[S]: Server IP address is  ",localhost_ip)


    # Listen for connections from client
    while(True):
        # accept client

        csockid, addr = ss.accept()
        print ("[S]: Got a connection request from a client at", addr)
        hostname = csockid.recv(200).decode('utf-8')

        if not hostname:
            break
        print("[S]: Data received from client::  ",hostname.decode('utf-8'))

        if(hostname == "END"):
            ss.close
            exit()

        #Connect to ts1 and ts2
        try:
            cs1 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
            #cs1.setblocking(0)
            cs2 = mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
            #cs2.setblocking(0)
            print("[C]: Client sockets created")
        except mysoc.error as err:
            print('{} \n'.format("socket open error ",err))

        #cs1.setblocking(0)
        #cs2.setblocking(0)
        sa_sameas_myaddr1 = mysoc.gethostbyname(ts1Host)
        sa_sameas_myaddr2 = mysoc.gethostbyname(ts2Host)
        server_binding1 = (sa_sameas_myaddr1, ts1Port)
        server_binding2 = (sa_sameas_myaddr2, ts2Port)
        cs1.connect(server_binding1)
        cs2.connect(server_binding2)
        #cs1.setblocking(0)
        #cs2.setblocking(0)
        socks = [];
        socks.append(cs1)
        socks.append(cs2)
        print socks
        message = "test message"
        cs1.send(hostname.encode('utf-8'))
        cs2.send(hostname.encode('utf-8'))
        data = None

        # this will block until at least one socket is ready
        ready_socks,_,_ = select.select(socks, [], [], 5)
        for sock in ready_socks:
            data, addr = sock.recvfrom(1024) # This is will not block
            print "received message:", data
            print("succesfully connected")


        if data is None:
            #Send some error to client
            print("no data sent in time?")
            data = "No hostname found"
            print("[S]: Data sent to client ::  ",data)
            csockid.send(record.encode('utf-8'))
        else:
            print("[S]: Data sent to client ::  ",data)
            csockid.send(record.encode('utf-8'))


    # close server socket
    ss.close()
    exit()

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

lsPort = sys.argv[1]
ts1Host = sys.argv[2]
ts1Port = sys.argv[3]
ts2Host = sys.argv[4]
ts2Port = sys.argv[5]

t1 = threading.Thread(name='server', target=server, args=(lsPort, ts1Host, ts1Port, ts2Host, ts2Port,))
t1.start()

t1.join()

exit()
