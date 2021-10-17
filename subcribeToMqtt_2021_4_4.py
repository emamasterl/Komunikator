#-*- coding: utf-8 -*-
import time
import paho.mqtt.client as paho


#broker="iot.eclipse.org"

#define callback

def on_message(client, userdata, msg): 
    global MyGlobalVar
    msg.payload = msg.payload.decode("utf-8")
    MyGlobalVar = str(msg.payload)
        
      
def podatki():
        client= paho.Client("TEstiranje_podatkov") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
        ######Bind function to callback
        client.on_message=on_message
        #####
        print("connecting to broker ","broker.hivemq.com")
        client.connect("broker.hivemq.com")#connect
        client.loop_start() #start loop to process received messages
        print("subscribing ")
        client.subscribe("podatki2")#subscribe
        time.sleep(0.5)
        client.on_message=on_message
        time.sleep(0.5)
        client.disconnect() #disconnect
        client.loop_stop()
        #client.loop_forever()
        return MyGlobalVar
