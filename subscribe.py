import paho.mqtt.client as mqtt
import time
import sys

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("topic", qos=1)

def on_message(client, userdata, msg):
    #print(str(msg.payload))
    f1.write(str(client) + " " + str(msg.payload) + str(time.time()) + '\n')


def on_subscribe(client, userdate, mid, granted_qos):
    print("granted_qos: " + str(granted_qos))

# The callback for when a PUBLISH message is received from the server.

f1 = open('subtimes.txt', 'w+')
'''i=0
j=0
f1 = open('subtimes', 'w+')

iterations = int(input("measure time after how many iterations? "))
def on_message(client, userdata, msg):
    f1.write(str(client) + " " + str(msg.payload) + str(time.time()) + '\n')
    global i, j, start_time
    if i==0:
        start_time = time.time()
    i+=1
    print(str(i)+" "+msg.topic+" "+str(msg.payload))
    if i==iterations:
        print(time.time() - start_time)
        sys.exit()'''




client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

client.connect("localhost", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
