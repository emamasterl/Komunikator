import json
import timeDifference_2021_3_28
import datetime
import logging
import logging.handlers
logging.basicConfig(filename = 'logiranje.log', filemode = 'a', level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

# @brief
def get_answer_text(contextual_info):
    
    departure_time = contextual_info[0]
    arival_time = contextual_info[1]
    bus_stop_name1 = contextual_info[2]
    bus_stop_name2 = contextual_info[3]
    bus_number = contextual_info[4]

    

    hour = contextual_info[0]

    try:
        if hour[2:3] == ":":
            h = int(hour[0:2])
            if hour[6:7] == "m":
                print("a")
                m = int(hour[3:5])
                e = hour[5:7]
            else:
                print("b")
                m = int(hour[3:4])
                e = hour[4:6]
        else:
            h = int(hour[0:1])
            if hour[5:6] =="m":
                print("c")
                m = int(hour[2:4])
                e = hour[4:6]
            else:
                print("d")
                m = int(hour[2:3])
                e = hour[3:5]


        j = datetime.datetime.now().hour
        n = datetime.datetime.now().minute
    

        if timeDifference_2021_3_28.differenceh(j,n,h,m,e) != 0:
            bus = "Trola " + bus_number + " pride na postajo " + bus_stop_name1 + " v smeri " + bus_stop_name2 + " čez " + str(timeDifference_2021_3_28.differenceh(j,n,h,m,e)) + " ur in " +  str(timeDifference_2021_3_28.differencem(j,n,h,m,e)) + " minut"
            
        elif timeDifference_2021_3_28.differenceh(j,n,h,m,e) == 0  and timeDifference_2021_3_28.differencem(j,n,h,m,e) == 0:
            bus = "Trola prihaja na postajo"

        else: 
            bus = "Trola " + bus_number + " pride na postajo " + bus_stop_name1 + " v smeri " + bus_stop_name2 +" čez " + str(timeDifference_2021_3_28.differencem(j,n,h,m,e)) + " minut"
        log.info("Podatki za bus: "+ bus)

        """bus = "Trola " + contextual_info[0]['stevilka'] + " pride na postajo " + contextual_info[0]['postaja(odhod)'] + " v smeri " + contextual_info[0]['smer']"""
        decided_outcome = bus




        answer_text = decided_outcome

        return answer_text
    except:
        answer_text="Imamo težave pri pridobivanju podatkov. Prosimo, poskusite kasneje"
    
        return answer_text


# @brief send data to server
def get_communicator_mood(contextual_info):
    
    if contextual_info.a < 1:
        mood = 1
    else:
        mood = 2 
        
    return mood
    