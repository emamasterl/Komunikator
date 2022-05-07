from xml.etree import ElementTree as ET
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import os
file_xml=r"app\ssml.xml"
tree = ET.parse(file_xml)
subscription_key=os.environ["subscription_key"]="b285947fe5a945edae22c7161fec9bf2"
def text_to_speech(text):
    speech_config = SpeechConfig(subscription=subscription_key, region="westeurope")
    audio_config = AudioOutputConfig(use_default_speaker=True)
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    #print("text= "+text)
    tree.find('voice').text = text
    tree.write(file_xml)
    ssml_string = open(file_xml, "r", encoding="utf-8-sig").read()
    synthesizer.speak_ssml_async(ssml_string).get()