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

    if "Danes na lokacijo ne pelje noben avtobus" in route_data:
        print('Ni busa')
        can_continiue = 2
        return can_continiue
    
    else:
        
        departure_time = route_data[0]
        arival_time = route_data[1]
        bus_stop_name1 = route_data[2]
        bus_stop_name2 = route_data[3]
        bus_number = route_data[5]

        if departure_time != "" and arival_time != "" and bus_stop_name1 != "" and bus_stop_name2 != "" and bus_number != "":
            log.info("Podatki so bili uspesno pridobljeni.")
            #print('dela')
            can_continiue = 1

        else:
            log.warning("Nismo uspeli pridobiti vseh podatkov.", route_data)
            can_continiue = 0
            


        return can_continiue
            
"""while(True):
    address=input('input: ')
    route_data = request_directions(address)
    get_route_data_integrity(route_data)"""