# Server

### **Usage:**

usage: server3.py [-h] [-ipv6] [-ipv4] port

positional arguments:
  port

optional arguments:
  -h, --help  show this help message and exit
  -ipv6       enable only IPv6
  -ipv4       enable only IPv4
  
  
  ## **Examples:**
 * `server3.py 1234` Runs a local Server which is listening on port 1234 for incoming connections (accepts either IPv4 or IPv6 Connections)
 
 * `server3.py -ipv6 1234` Runs a local Server which is listening on port 1234 for incoming connections (accepts only IPv6 Connections)

***

# Client
***Tries to connect to a host listening on the specified IP(default IPv4) and Port
*** Either use this client as a file transmitter or a basic echo out to server
### **Usage:**
usage: client3.py [-h] [-ipv6] [-f [File [File ...]]] port IP-Address

positional arguments:
  port
  IP-Address

optional arguments:
  -h, --help            show this help message and exit
  -ipv6                 enable IPv6
  -f [File [File ...]]  transmitts files
  
  
## **Examples:**
* `client3.py 1234 127.0.0.1` Tries to connect to the localhost on port 1234 and loops back every input to the remote host

* `client3.py -ipv6 1234 ::1` Tries to connect to the localhost(ipv6) on port 1234 and loops back every input to the remote host

* `client3.py 1234 127.0.0.1 -f file1 file2` Tries to connect to the localhost on port 1234 and transmitts the files: file1 and file2
