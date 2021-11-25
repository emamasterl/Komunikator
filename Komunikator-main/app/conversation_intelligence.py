import json
import timeDifference_2021_3_28
from timeDifference_2021_3_28 import get_time_difference
import datetime

import logging
import logging.handlers
logging.basicConfig(filename = 'logiranje.log', filemode = 'a', level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

# @brief
def get_answer_text(contextual_info):
    
    weather = list(contextual_info[0])
    route_data = list(contextual_info[1])
    temperature = weather[0]
    weather_desc=weather[1]
    departure_time = route_data[0]
    arival_time = route_data[1]
    bus_stop_name1 = route_data[2]
    bus_stop_name2 = route_data[3]
    bus_number = route_data[5]
    
    if departure_time[2:3] == ":":
            departure_time_hour = int(departure_time[0:2])
            if departure_time[6:7] == "m":
                departure_time_minutes = int(departure_time[3:5])
                am_pm = departure_time[5:7]
            else:
                departure_time_minutes = int(departure_time[3:4])
                am_pm = departure_time[4:6]
    else:
        departure_time_hour = int(departure_time[0:1])
        if departure_time[5:6] =="m":
            departure_time_minutes = int(departure_time[2:4])
            am_pm = departure_time[4:6]
        else:

            departure_time_minutes = int(departure_time[2:3])
            am_pm = departure_time[3:5]
            
    hour = datetime.datetime.now().hour
    minutes = datetime.datetime.now().minute

    arrives_in=timeDifference_2021_3_28.get_time_difference( hour, minutes,departure_time_hour,departure_time_minutes,am_pm)
    print(type(arrives_in[1]))
    
    
    if arrives_in[0]!=0:
        bus = "Trola " + bus_number + " pride na postajo " + bus_stop_name1 + " v smeri " + bus_stop_name2 + " čez " + str(arrives_in[0]) + " ur in " +  str(arrives_in[1]) + " minut"
    else: 
        bus = "Trola " + bus_number + " pride na postajo " + bus_stop_name1 + " v smeri " + bus_stop_name2 +" čez " + str(arrives_in[1]) + " minut"
    
    if weather_desc == 'thunderstorm' or weather_desc == 'snow' or weather_desc == 'drizzle' or weather_desc == 'rain' or weather_desc == 'wind':
        decided_outcome = bus

    elif temperature <= 5:
        decided_outcome = bus

    else:
        decided_outcome = "Do cilja greste lahko peš."

    return decided_outcome


# @brief send data to server
def get_communicator_mood(contextual_info):
    
    if contextual_info.a < 1:
        mood = 1
    else:
        mood = 2 
        
    return mood
    