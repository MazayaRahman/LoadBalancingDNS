import sys
import socket as mysoc
import threading

#client task
def client(host, lsport):



    lsport = int(lsport)
    print("the lsport is:",lsport)

    file_write = open("RESOLVED.txt", "w")
    for hn in hostname:
       # create client socket and connect to LS
       try:
           cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
           print("[C]: Client socket created")
           print("\n")
       except mysoc.error as err:
           print('{} \n'.format("socket open error ",err))
       sa_sameas_myaddr = mysoc.gethostbyname(host)
       server_binding = (sa_sameas_myaddr, lsport)
       cs.connect(server_binding)
       print ("Sending Hostname: ", hn)
       # convert to lowercase
       hn = hn.lower()
       cs.send(hn.encode('utf-8'))
       data_from_ls = cs.recv(200).decode('utf-8') #data received from rs server.
       file_write.write(data_from_ls.decode('utf-8')+ '\n') #putting data from rs into resolved.txt
       print("the data from ls is:", data_from_ls)
       #file_write.write(data_from_ls.decode('utf-8')+ '\n')
       cs.close()



    try:
        cs=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
         #cs1 = mysoc.socket(sysoc.AF_INET, mysoc.SOCK_STREAM)
        print("[C]: Client socket created")
    except mysoc.error as err:
        print('{} \n'.format("socket open error ",err))
        #cs1=mysoc.socket(mysoc.AF_INET, mysoc.SOCK_STREAM)
    sa_sameas_myaddr = mysoc.gethostbyname(host)
    server_binding = (sa_sameas_myaddr, lsport)
    cs.connect(server_binding)
    print ("Sending message: ", "END")
    # convert to lowercase
    message = "END"
    cs.send(message.encode('utf-8'))
    cs.close
    


    exit()

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)
host = sys.argv[1]
lsport = sys.argv[2]
#rsport = sys.argv[2]
#tsport = sys.argv[3]
print 'host: ', host, 'lsport: ', lsport
hostname =[]
with open("PROJ2-HNS.txt", 'r') as f:
    for lines in f:
        #print(lines)
        hostname.append(lines.strip())


t2 = threading.Thread(name='client', target=client, args=(host,lsport,))
t2.start()
t2.join()
exit()
