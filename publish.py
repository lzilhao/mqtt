import paho.mqtt.client as mqtt
import time
message = 'ON'
payload = "0123456789"

def on_connect(mosq, obj, rc):
    print("rc: " + str(rc))

def on_publish(mosq, obj, mid):
    global count
    f.write(str(count) + " publ " + str(time.time()) + '\n')
    print("on publish " + str(time.time()))
    print("mid: " + str(mid) + '\n')

def on_log(mosq, obj, level, string):
    print(string)

mqttc = mqtt.Client()
# Assign event callbacks
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
# Connect
mqttc.connect("localhost", 1883,60)

f = open('pubtimes.txt', 'w')
start_time = time.time()
count = 0
for j in range(5):      #for each j payload increases tenfold
    for i in range(100):
        f.write(str(count) + " sent " + str(time.time()) + '\n')
        mqttc.publish("topic", payload)        
        print("sent at " + str(time.time()) + '\n')
        print(int(len(payload)))
        count+=1
    payload = payload*10



# Continue the network loop
#mqttc.loop_forever()
