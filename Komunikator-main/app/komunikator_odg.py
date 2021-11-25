#-*- coding: utf-8 -*-

#pip install nltk	
#pip install requests uuid	
#pip install googlemaps	
#pip install  dialogflow	
#pip install azure-cognitiveservices-speech	
#pip install numpy	
#pip install matplotlib	

from tkinter import *
import tkinter
import sys
import os
import matplotlib
matplotlib.use('Agg')

import random
import json
import numpy as np
import pickle
import nltk
import Lokacija #zajem govora
import sendToMqtt_2021_4_15  #pošiljanje podatkov
import subcribeToMqtt_2021_4_4 #subscribe
import decision_2021_4_18  #pamet
import time


def zajemiSporocilo(sporocilo):
    
    msg = Lokacija.user_input(sporocilo)
    print("message :", msg)
    sendToMqtt_2021_4_15.mqtt_activate(msg)
    time.sleep(4)
    sub = subcribeToMqtt_2021_4_4.podatki()
    print(sub)
    answer = decision_2021_4_18.pot(sub)        
    return answer
