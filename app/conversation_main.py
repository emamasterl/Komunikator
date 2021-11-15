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
import user_input_acquisition #zajem govora
import output_to_user
import decision_2021_4_18  #pamet
import time
import get_directions
from get_directions import request_directions
import check_route_data_integrity
import conversation_intelligence as ci



def question_to_answer(userinput_sound):
    #get_user_input = user_input_acquisition.get_intent_from_question(userinput_sound)
    address = output_to_user.talk_back(userinput_sound)
    #place_address = input('Address: ')
    route_data = request_directions(address)
    all_data_received = check_route_data_integrity.get_route_data_integrity(route_data)
    if all_data_received == 0:
        return "Imamo težave pri pridobivanju podatkov, poskuite kasneje."
    else:
        answer_text = ci.get_answer_text(route_data)     
        return answer_text