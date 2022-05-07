import dialogflow_v2beta1 as dialogflow
#import dialogflowcx_v3beta1
import os, requests, time
from xml.etree import ElementTree as ET
import azure.cognitiveservices.speech as speechsdk
import requests, uuid, json
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig
from google.cloud import translate
import googlemaps 
#import user_input_acquisition
subscription_key=os.environ["subscription_key"]="b285947fe5a945edae22c7161fec9bf2"

import logging

logging.basicConfig(filename = 'logiranje.log', filemode = 'a', level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

def talk_back(question):
    log.info("Govor: "+ question)
    speech_config = SpeechConfig(subscription=subscription_key, region="westeurope")
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    file_xml=r"app/ssml.xml"
    tree = ET.parse(file_xml)

    '''try:
        answer, intent=user_input_acquisition.get_intent_from_question(question)
        #pove postajo
        print("answer= "+answer)
        tree.find('voice').text = answer
        tree.write(file_xml)
        ssml_string = open(file_xml, "r", encoding="utf-8-sig").read()
        synthesizer.speak_ssml_async(ssml_string).get()
        print(answer)
        return answer, intent
    except Exception as e:
        print("something went terribly wrong")
        print('e: ',e)
        a = "Se opravičujem, lahko ponovite? Kam želite it?"
        return'''