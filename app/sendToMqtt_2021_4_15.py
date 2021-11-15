######Pošlje testna verzija

import time
import paho.mqtt.client as paho
import json

import logging
import logging.handlers
logging.basicConfig(filename = 'mylog.log', filemode = 'a', level=logging.WARNING,  format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

broker="broker.hivemq.com"

topic = "vhod2"
naslov= "Samova ulica 5"

#define callback
def on_message(client, userdata, message):
    time.sleep(0.4)
    print("received message =",str(message.payload.decode("utf-8")))

#def on_connect(client, userdata, flags, rc):
#    client.subscribe(topic)

def mqtt_activate(naslov):
    client= paho.Client("Pokus1") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
    ######Bind function to callback
    client.on_message=on_message
    #####
    print("connecting to broker ",broker)
    #client.on_connect=on_connect  #bind call back function
    try: 
        client.connect(broker)#connect
        client.loop_start() #start loop to process received messages
        print("subscribing ")
        client.subscribe(topic)#subscribe
        time.sleep(0.4)
        print("publishing " )
        #print(data)
        client.publish(topic , naslov, retain=True)#retain=Truepublish, RETAIN pomemben, če ga nedaš se poročilo ne shrani in potem ga drugi client ne dobi
        time.sleep(0.3)
        client.disconnect() #disconnect
        client.loop_stop() #stop loop
        #client.loop_forever()
    except Exception:
        logging.warning("Neuspešna povezava na broker")
        napaka = "Imamo težave s pridobivanjem podatkov, prosimo poskusite kasneje"
        return napaka
    


#mqtt_activate()
