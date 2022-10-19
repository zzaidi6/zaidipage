import socket
from colored import fg

#colors
red=fg('red')
green=fg('green')
blue=fg('blue')

#banner
print(green)
print("-----Welcome to the ZaidiShell!------")
print(red)
print("type run to start and then,")
print("type domain in the entry box.")
print(green)

#main script
def code():
  print(red)
  ip = input("domain: ")
  host = socket.gethostbyname(ip)
  print(green)
  print(host+ " is the ip address of " +ip)
  print(blue)
  print("url:- http://"+host)
  print(green)

#shell script
def shell():
  entry=input("ZaidiShell@=> ")
  if "run" == entry :
       code()
  else :
       print(red+"error: wrong argument!")
       print(green)
       return shell()

shell()
