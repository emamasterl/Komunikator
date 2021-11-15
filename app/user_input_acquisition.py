#pip install azure-cognitiveservices-speech
#pip install requests uuid
#pip install --upgrade google-cloud-translate
#pip install googlemaps

# -*- coding: utf-8 -*-

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

import logging

logging.basicConfig(filename = 'logiranje.log', filemode = 'a', level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
subscription_key=os.environ["subscription_key"]="81be4d6ff7e345c99cf694c6bea3282d"

def get_text_from_mic():
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region="westeurope")
    speech_config.speech_recognition_language="sl-SI"
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()

    log.info("Govor: "+ result.text)
    #print("from mic= "+result.text)
    return result.text

def extractPlacesFrom(text):
    #print("\nInput: "+text)
    API_KEY = 'AIzaSyBOC3bEyo9sp7MwqT7dYvuiBvQSWinw8jI'
    gmaps= googlemaps.Client(key = API_KEY)
    resultset = gmaps.places(text)['results']  
    return resultset

def get_intent_from_question(question):
    response=get_response(question)
    intent=get_intent(response)
    return_value=""
    if intent == "lokacija":
        if response.parameters["street-address"] == "":
            log.warning("Location not found: " + question)
            raise Exception("location not found")
        location=response.parameters["street-address"]["street-address"]
        return_value =  extractPlacesFrom(location)[0]["formatted_address"]
    elif intent=="busna":
        return_value = response.parameters.fields["busna"].list_value[0]
    else: 
        return_value = response.fulfillment_text

    print_out(question, return_value)
    return return_value

def get_intent(response):
    return response.intent.display_name

def print_out(question, response):
    intents_data = {}
    intents_data["tag"] =["{}".format(response)]
    intents_data["patterns"] = ["{}".format(question)]
    intents_data["responses"] = [""]
    intents_data["codex"] = [""]

    fileName=r'C:\Users\emama\OneDrive\Documents\Coding\Seca projekt\Komunikator2\app\intents2.json'
    with open(fileName, 'r',encoding="utf8") as fp:
        data = json.load(fp)

    data['intents'].append(intents_data)                 

    with open(fileName, 'w',encoding="utf8") as fp:
        json.dump(data, fp, ensure_ascii=False ,indent=2)

def get_response(text):
    #print("text type: ", type(text))
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\Users\emama\OneDrive\Documents\Coding\Seca projekt\Komunikator2\app\vaja-stqi-a94d4033cbd5.json'
    client = dialogflow.SessionsClient()
    session = client.session_path('vaja-stqi', '1234')
    #print("session: ", session)

    query_input = {
        "text": {
            "text": text,
            "language_code": "sl"
        }
    }
    #print("query_input type: ", type(query_input))
    response = client.detect_intent(session, query_input)
    #print('response: ', response)
    return response.query_result