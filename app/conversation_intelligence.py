import timeDifference_2021_3_28
from timeDifference_2021_3_28 import get_time_difference
import datetime

import logging
import logging.handlers
logging.basicConfig(filename = 'logiranje.log', filemode = 'a', level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

# @brief
def get_answer_text(weather_data,route_data,walking):
    #print('route_Data: ', route_data)
    temperature = weather_data[0]
    weather_desc=weather_data[1]
    departure_time = route_data[0]
    arival_time = route_data[1]
    bus_stop_name1 = route_data[2]
    bus_stop_name2 = route_data[3]
    bus_number = route_data[5]


    # del, ki uro razčleni uro v tekstovni obliki
    if len(departure_time) == 6:
        departure_time_hour=int(departure_time[0:1])
        departure_time_minutes=int(departure_time[2:4])
    else:
        departure_time_hour=int(departure_time[0:2])
        departure_time_minutes=int(departure_time[3:5])
    
    hour = datetime.datetime.now().hour
    minutes = datetime.datetime.now().minute

    arrives_in=timeDifference_2021_3_28.get_time_difference( hour, minutes,departure_time_hour,departure_time_minutes)
    
    #oblikuje stavek čez koliko časa pride trola na postajo
    if arrives_in[0]!=0:
        bus = "Trola " + bus_number + " pride na postajo " + bus_stop_name1 + " v smeri " + bus_stop_name2 + " čez " + str(arrives_in[0]) + " ur in " +  str(arrives_in[1]) + " minut"
    else: 
        bus = "Trola " + bus_number + " pride na postajo " + bus_stop_name1 + " v smeri " + bus_stop_name2 +" čez " + str(arrives_in[1]) + " minut"
    
    #odločanje, ali gre oseba na bus ali peš
    if weather_desc == 'nevihta' or weather_desc == 'sneg' or weather_desc == 'rosi' or weather_desc == 'dežuje' or weather_desc == 'piha veter' or temperature <= 5 or walking >10:
        log.info("Oseba naj gre na bus")
        decided_outcome = bus

    else:
        log.info("Oseba naj gre peš")
        decided_outcome = "Do cilja greste lahko peš."

    return decided_outcome


# @brief send data to server
def get_communicator_mood(contextual_info):
    
    if contextual_info.a < 1:
        mood = 1
    else:
        mood = 2 
        
    return mood
    