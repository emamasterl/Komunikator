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
    log.info('ZAČETEK')
    log.info(userinput_text)
    address,intent=speech_act_module(userinput_text)
    log.info('Address: '+ address)
    log.info('Intent: '+ str(intent))
    if intent != 'lokacija' and intent != 'busna':
        log.info('KONEC')
        return address

    route_data = get_directions.get_directions(address)
    walking_time=get_walking_time(address)
    weather_data=ow()
    log.info('Podatki o poti: '+ str(route_data))
    log.info('Čas hoje v minutah: '+ str(walking_time))
    log.info('Vremenski podatki: '+ str(weather_data))
    all_data_received = check_route_data_integrity.get_route_data_integrity(route_data)
    
    temperature = weather_data[0]
    weather_desc=weather_data[1]
    
    if all_data_received == 0:
        log.info('KONEC')
        return "Imamo težave pri pridobivanju podatkov, poskusite kasneje."
    elif all_data_received == 2:
        log.info('KONEC')
        return "Danes na lokacijo ne pelje noben avtobus, pojdite peš ali z drugo obliko prevoza. Vremenski podatki: ", "Temperatura: ", temperature, "Vreme: ", weather_desc
    else:
        answer_text = ci.get_answer_text(weather_data,route_data,int(walking_time))
        suggested_path= str(answer_text) +"Vremenski podatki:\n"+ "Temperatura:"+ str(temperature)+ "\n Vreme:"+ str(weather_desc)
        log.info(suggested_path)
        log.info('KONEC')
        return suggested_path