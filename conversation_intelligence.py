import json
import timeDifference_2021_3_28
import datetime
import logging
import logging.handlers
logging.basicConfig(filename = 'logiranje.log', filemode = 'a', level=logging.INFO, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

# @brief
def get_answer_text(contextual_info):

     #print(contextual_info[0]['padavine'])
    ura = contextual_info[0]['ura odhoda']

    try:
        if ura[2:3] == ":":
            h = int(ura[0:2])
            if ura[6:7] == "m":
                print("a")
                m = int(ura[3:5])
                e = ura[5:7]
            else:
                print("b")
                m = int(ura[3:4])
                e = ura[4:6]
        else:
            h = int(ura[0:1])
            if ura[5:6] =="m":
                print("c")
                m = int(ura[2:4])
                e = ura[4:6]
            else:
                print("d")
                m = int(ura[2:3])
                e = ura[3:5]


        j = datetime.datetime.now().hour
        n = datetime.datetime.now().minute
        #print(contextual_info[0]['stevilka'])
        #print(h,m,e,j,n)"""

        if timeDifference_2021_3_28.differenceh(j,n,h,m,e) != 0:
            bus = "Trola " + contextual_info[0]['stevilka'] + " pride na postajo " + contextual_info[0]['postaja(odhod)'] + " v smeri " + contextual_info[0]['smer'] + " čez " + str(timeDifference_2021_3_28.differenceh(j,n,h,m,e)) + " ur in " +  str(timeDifference_2021_3_28.differencem(j,n,h,m,e)) + " minut"
            
        elif timeDifference_2021_3_28.differenceh(j,n,h,m,e) == 0  and timeDifference_2021_3_28.differencem(j,n,h,m,e) == 0:
            bus = "Trola prihaja na postajo"

        else: 
            bus = "Trola " + contextual_info[0]['stevilka'] + " pride na postajo " + contextual_info[0]['postaja(odhod)'] + " v smeri " + contextual_info[0]['smer'] +" čez " + str(timeDifference_2021_3_28.differencem(j,n,h,m,e)) + " minut"
        log.info("Podatki za bus: "+ bus)

        """bus = "Trola " + contextual_info[0]['stevilka'] + " pride na postajo " + contextual_info[0]['postaja(odhod)'] + " v smeri " + contextual_info[0]['smer']"""




        if contextual_info[0]['padavine'] == 'thunderstorm' or contextual_info[0]['padavine'] == 'snow' or contextual_info[0]['padavine'] == 'drizzle' or contextual_info[0]['padavine'] == 'rain' or contextual_info[0]['padavine'] == 'wind':
            log.info("Odločitev: slabo vreme - bus")
                    
            odlocitev = bus

        elif contextual_info[0]['temp'] <= 5:
            log.info("Odločitev: nizka temperatura - bus")
            
            odlocitev = bus

        elif contextual_info[0]['hoja'] > 15:
            log.info("Odločitev: Predolga hoja - bus.")
            
            odlocitev = bus


        elif contextual_info[0]['avtobus'] <= contextual_info[0]['hoja']:
            log.info("Odločitev: Cas hoje krajsi od casa voznje- bus")
            
            odlocitev = bus

        else:
            log.info("oseba naj gre pes")
            odlocitev = "Do cilja greste lahko peš."

        #profiler.stop()
        #txt = profiler.output_text()
        """with open("mylog.log", "a") as f:
            f.write(txt)"""
        
        
    except:
        nobus = contextual_info[0]['BUS NE VOZI VE\u010c, bistevno hitreje bo \u010de gre\u0161 pe\u0161']
        if "nobus" in locals():
            odg = "Trola ne vozi več, bistveno hitreje bo, če greste peš."
            logging.info("Odločitev: Bus ne vozi več")

    answer_text = odlocitev
    
    return answer_text


# @brief send data to server
def get_communicator_mood(contextual_info):
    
    if contextual_info.a < 1:
        mood = 1
    else:
        mood = 2 
        
    return mood
    