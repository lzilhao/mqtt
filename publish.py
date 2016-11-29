import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import sys

payload = "0123456789"

def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_publish(mosq, obj, mid):
    #f1.write(str(mid) + " publ " + str(time.time()) + '\n')
    f1.write(str(time.time()) + '\n')
    print(str(mid) + " on publish " + str(time.time()))

def on_log(mosq, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
#mqttc.on_log = on_log

mqttc.connect("localhost", 1883,60) # Connect
mqttc.loop_start()  # Start thread to process network traffic


f1 = open('pubtimes.txt', 'w')
f2 = open('senttimes.txt', 'w')

for j in range(5):      #for each j payload increases tenfold
    for i in range(100):
        msgInfo=mqttc.publish("topic", payload, qos=1)
        #f2.write(str(msgInfo.mid) + " sent " + str(time.time()) + '\n')
        f2.write(str(time.time()) + '\n')
        #print(msgInfo.is_published())
        print(str(msgInfo.mid) + " sent at " + str(time.time()))
        #print(msgInfo.mid)
        #msgInfo.wait_for_publish()
    payload = payload*10

mqttc.loop_stop()   # Stop network thread previously created
f1.close()
f2.close()

# Continue the network loop
#mqttc.loop_forever()
#mqttc.loop_start()
