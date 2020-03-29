# LoadBalancingDNS

Siddhi Kasera(smk339) & Mazaya Rahman(mr1411)

2. In the LS we used an array to store the two client sockets that connected to the two servers TS1 and TS2.  We used the select interface which returns an array of sockets that have received a response from the servers (TS1 or TS2). We set a timeout parameter for 5 seconds which blocks for 5 seconds or until one of the servers respond.  A loop goes over the array returned and checks if any data is received from either of the sockets.  We can figure out which server sent the data by checking the index of the socket in our socket array.  This data received is stored. In the case that no data is received from either of the servers, an error message ERROR: HOST NOT FOUND is stored. The data is then sent to the client.

3. There are no known issues in the code.

4. One of the problems was figuring out how to receive data from 2 servers in parallel and differentiate between which server it was received from. Using the select interface simplified the process.

5. Learned the implementation of load balancing to improve the performance and reduce traffic on the main DNS server. Learned to use the select interface to connect and receive data from different servers simultaneously. 

