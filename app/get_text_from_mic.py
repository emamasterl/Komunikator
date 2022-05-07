import logging


import azure.cognitiveservices.speech as speechsdk
import os

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
    return result.text