import time
from umqtt.simple import MQTTClient
# make sure to give clients different names !!
c = MQTTClient("umqtt_client7",’192.168.4.4’)
c.connect()
cnt=0
while 1:                                                                                                                 
  time.sleep(5)                                                                                              
  c.connect()                                                                                                       
  c.publish(b"vineyard/temp/vine7",str(cnt)) 
  cnt = cnt + 1
