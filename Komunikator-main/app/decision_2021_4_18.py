import json
import timeDifference_2021_3_28
import datetime
import pstats
from pstats import SortKey
#from pyinstrument import Profiler
#profiler = Profiler()
import logging
import logging.handlers

import conversation_intelligence as ci

logging.basicConfig(filename = 'logiranje.log', filemode = 'a', level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

# @brief 
def pot(MyGlobalVar):
    #profiler.start()
    parsed_json = json.loads(MyGlobalVar)
    #print(parsed_json)
    global contextual_info
    contextual_info = parsed_json['intents']

    
    
    ura_odhoda = contextual_info[0]['ura odhoda']
    temp = contextual_info[0]['temp']
    padavine = contextual_info[0]['padavine']
    postaja = contextual_info[0]['postaja(odhod)']
    stevilka = contextual_info[0]['stevilka']
    
    

    if "ura_odhoda" in locals() and "temp" in locals() and "padavine" in locals() and "postaja" in locals() and "stevilka" in locals():
        log.info("Podatki so bili uspesno pridobljeni.")

    else:
        log.warning("Nismo uspeli pridobiti vseh podatkov.")
        return "Imamo težave pri pridobivanju podatkov, poskusite kasneje."



    return answer_text
            
        