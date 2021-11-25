import json
import timeDifference_2021_3_28
import datetime
import pstats
from pstats import SortKey
#from pyinstrument import Profiler
#profiler = Profiler()
import logging
import logging.handlers
import get_directions
from get_directions import request_directions


logging.basicConfig(filename = 'logiranje.log', filemode = 'a', level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

# @brief 
def get_route_data_integrity(route_data):
    #print(type(route_data))
    parsed_json = list(route_data)
    #print('parsed json: ', parsed_json)
    #print(type(parsed_json))
    contextual_info = parsed_json

    if contextual_info == "Danes na lokacijo ne pelje noben avtobus":
        can_continiue = 0
        return can_continiue
    
    else:
        weather = list(contextual_info[0])
        route_data = list(contextual_info[1])
        
        temperature = weather[0]
        print("temperature: ", temperature)
        weather_desc=weather[1]
        print("weather: ", weather)
        departure_time = route_data[0]
        print('departure_time: ',departure_time)
        arival_time = route_data[1]
        print('arival time: ',arival_time)
        bus_stop_name1 = route_data[2]
        print('bus stop name1: ',bus_stop_name1)
        bus_stop_name2 = route_data[3]
        print('bus stop name2: ',bus_stop_name2)
        bus_number = route_data[5]
        print('bus number: ',bus_number)
        

        if departure_time != "" and arival_time != "" and bus_stop_name1 != "" and bus_stop_name2 != "" and bus_number != "":
            log.info("Podatki so bili uspesno pridobljeni.")
            print('dela')
            can_continiue = 1

        else:
            log.warning("Nismo uspeli pridobiti vseh podatkov.")
            can_continiue = 0
            


        return can_continiue
            
"""while(True):
    address=input('input: ')
    route_data = request_directions(address)
    get_route_data_integrity(route_data)"""