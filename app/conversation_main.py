#-*- coding: utf-8 -*-

#pip install nltk	
#pip install requests uuid	
#pip install googlemaps	
#pip install  dialogflow	
#pip install azure-cognitiveservices-speech	
#pip install numpy	
#pip install matplotlib	
from audioop import add
from ctypes import addressof
import logging
from tkinter import *


from get_walking_time import get_walking_time



import get_directions
import check_route_data_integrity
import conversation_intelligence as ci
from text_to_speech import text_to_speech as tts
from get_weather_report import openweather as ow
from speech_act_module import speech_act_module
from get_walking_time import get_walking_time
import logging

logging.basicConfig(filename = 'logiranje.log', filemode = 'a', level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

def question_to_answer(userinput_text):
    log.info(userinput_text)
    address,intent=speech_act_module(userinput_text)
    print('address_ ', address)
    if address == 'napaka' or address == 'Se opravičujem, lahko ponovite? Kam želite it?':
        return 'Se opravičujem, lahko ponovite? Kam želite it?'
    route_data = get_directions.get_directions(address)
    walking_time=get_walking_time(address)
    weather_data=ow()
    all_data_received = check_route_data_integrity.get_route_data_integrity(route_data)

    bus_info = list(route_data[1])
    
    temperature = weather_data[0]
    weather_desc=weather_data[1]
    
    if all_data_received == 0:
        #tts("Imamo težave pri pridobivanju podatkov, poskusite kasneje.")
        return "Imamo težave pri pridobivanju podatkov, poskusite kasneje."
    elif all_data_received == 2:
        #tts("Danes na lokacijo ne pelje noben bus, pojdite peš ali z drugo obliko prevoza.")
        return "Danes na lokacijo ne pelje noben bus, pojdite peš ali z drugo obliko prevoza. Vremenski podatki: ", "Temperatura: ", temperature, "Vreme: ", weather_desc
    else:
        answer_text = ci.get_answer_text(weather_data,route_data,int(walking_time))
        suggested_path= str(answer_text) +"Vremenski podatki:\n"+ "Temperatura:"+ str(temperature)+ "\n Vreme:"+ str(weather_desc)
        #tts(answer_text)
        return suggested_path