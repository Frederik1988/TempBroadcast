BROADCAST_TO_PORT = 7000
from sense_hat import SenseHat
import time
from socket import *
from datetime import datetime

s = socket(AF_INET, SOCK_DGRAM)
#s.bind(('', 14593))     # (ip, port)
# no explicit bind: will bind to default IP + random port
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
counter = 0

while True:
  temp = "Temperaturen er: " + str(sense.get_temperature())
  pres = "Lufttrykket er: " + str(sense.get_pressure())
  hum = "Luftfugtigheden er: " + str(sense.get_humidity())
  
	s.sendto(bytes(pres, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
	print(pres)
	
	s.sendto(bytes(hum, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
	print(hum)
	
	
	if (counter==5):
	  s.sendto(bytes(temp, "UTF-8), ")('<broadcast>', BROADCAST_TO_PORT))
	  print(temp)
	  counter = 0
	  
	 counter++
	 
	 time.sleep(1)
