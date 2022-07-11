#directions_api
import requests
import json
#import jason_zapis
import pprint

'''kraj = input('Kraj : ')
key = 'AIzaSyDIs83FUp8tjOQcVU5cmjyAGn2uFwt5vEs'     
origin = 'place_id:ChIJvfl5OEMtZUcRH4phdGnSJps'     
url = 'https://maps.googleapis.com/maps/api/directions/json?' 
res2 = requests.get(url + 'origin=' + origin + '&destination=' + kraj + '&mode=transit&key=' + key)
data2 = res2.json()
global ura_odhoda, ura_prihoda,departure_stop,arrival_stop, ura_prihoda2, arrival_stop2, smer, stevilka, smer2, stevilka2, test'''
pp = pprint.PrettyPrinter(width=1, compact=True)
#x = 10

def request_directions(kraj):
    key = 'AIzaSyDIs83FUp8tjOQcVU5cmjyAGn2uFwt5vEs'     
    origin = 'place_id:ChIJvfl5OEMtZUcRH4phdGnSJps'     
    url = 'https://maps.googleapis.com/maps/api/directions/json?' 
    res2 = requests.get(url + 'origin=' + origin + '&destination=' + kraj + '&mode=transit'+ '&key=' + key + '&region=SL' + '&language=sl')
    
    #pp.pprint(data3)
    
    #pp.pprint(z)
    #print(z)
    data2 = res2.json()
    #&alternatives=true
    #pp.pprint(data2)
    n = 0

    #print(z4)

    try: 
        for n in range(10):
            x = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['line']['agencies'][0]['name']
            if x == 'Ljubljanski Potniški Promet':
                break
    except(IndexError) :
            y = "Danes na lokacijo ne pelje noben avtobus"
            #print(y)
            return y
  
        #print(n)

    
    try:
        ura_odhoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_time']['text']
        ura_prihoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_time']['text']
        departure_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_stop']['name']
        arrival_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_stop']['name']
        smer = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['headsign']
        stevilka = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['line']['short_name']
        ura_prihoda2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['arrival_time']['text']
        arrival_stop2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['arrival_stop']['name']
        smer2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['headsign']
        stevilka2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['line']['short_name']
        ura_prihoda3 = data2['routes'][n]['legs'][0]['steps'][5]['transit_details']['arrival_time']['text']
        arrival_stop3 = data2['routes'][n]['legs'][0]['steps'][5]['transit_details']['arrival_stop']['name']
        smer3 = data2['routes'][n]['legs'][0]['steps'][5]['transit_details']['headsign']
        stevilka3 = data2['routes'][n]['legs'][0]['steps'][5]['transit_details']['line']['short_name']
        #print('ODHOD:', ura_odhoda, departure_stop,'PRVI PRESTOP:', ura_prihoda, arrival_stop,'CILJ1:', ura_prihoda2, arrival_stop2, smer, stevilka,"CILJ2:", smer2, stevilka2, "konec:", ura_prihoda3, arrival_stop3, smer3, stevilka3)
        return ura_odhoda, ura_prihoda, departure_stop, arrival_stop, ura_prihoda2, arrival_stop2, smer, stevilka, smer2, stevilka2
    except (IndexError, KeyError)  :
        pass
    
    try:
        ura_odhoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_time']['text']
        ura_prihoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_time']['text']
        departure_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_stop']['name']
        arrival_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_stop']['name']
        smer = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['headsign']
        stevilka = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['line']['short_name']
        ura_prihoda2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['arrival_time']['text']
        arrival_stop2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['arrival_stop']['name']
        smer2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['headsign']
        stevilka2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['line']['short_name']
        ura_prihoda3 = data2['routes'][n]['legs'][0]['steps'][4]['transit_details']['arrival_time']['text']
        arrival_stop3 = data2['routes'][n]['legs'][0]['steps'][4]['transit_details']['arrival_stop']['name']
        smer3 = data2['routes'][n]['legs'][0]['steps'][4]['transit_details']['headsign']
        stevilka3 = data2['routes'][n]['legs'][0]['steps'][4]['transit_details']['line']['short_name']
        #print('ODHOD:', ura_odhoda, departure_stop,'PRVI PRESTOP:', ura_prihoda, arrival_stop,'CILJ1:', ura_prihoda2, arrival_stop2, smer, stevilka,"CILJ2:", smer2, stevilka2, "konec:", ura_prihoda3, arrival_stop3, smer3, stevilka3)
        return ura_odhoda, ura_prihoda, departure_stop, arrival_stop, ura_prihoda2, arrival_stop2, smer, stevilka, smer2, stevilka2
    except (IndexError, KeyError)  :
        pass

    try:
        ura_odhoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_time']['text']
        ura_prihoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_time']['text']
        departure_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_stop']['name']
        arrival_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_stop']['name']
        smer = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['headsign']
        stevilka = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['line']['short_name']
        ura_prihoda2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['arrival_time']['text']
        arrival_stop2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['arrival_stop']['name']
        smer2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['headsign']
        stevilka2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['line']['short_name']
        ura_prihoda3 = data2['routes'][n]['legs'][0]['steps'][4]['transit_details']['arrival_time']['text']
        arrival_stop3 = data2['routes'][n]['legs'][0]['steps'][4]['transit_details']['arrival_stop']['name']
        smer3 = data2['routes'][n]['legs'][0]['steps'][4]['transit_details']['headsign']
        stevilka3 = data2['routes'][n]['legs'][0]['steps'][4]['transit_details']['line']['short_name']
        #print('ODHOD:', ura_odhoda, departure_stop,'PRVI PRESTOP:', ura_prihoda, arrival_stop,'CILJ1:', ura_prihoda2, arrival_stop2, smer, stevilka,"CILJ2:", smer2, stevilka2, "konec:", ura_prihoda3, arrival_stop3, smer3, stevilka3)
        return ura_odhoda, ura_prihoda, departure_stop, arrival_stop, ura_prihoda2, arrival_stop2, smer, stevilka, smer2, stevilka2
    except (IndexError, KeyError)  :
        pass
            

    try:
        ura_odhoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_time']['text']
        ura_prihoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_time']['text']
        departure_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_stop']['name']
        arrival_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_stop']['name']
        smer = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['headsign']
        stevilka = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['line']['short_name']
        ura_prihoda2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['arrival_time']['text']
        arrival_stop2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['arrival_stop']['name']
        smer2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['headsign']
        stevilka2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['line']['short_name']
        ura_prihoda3 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['arrival_time']['text']
        arrival_stop3 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['arrival_stop']['name']
        smer3 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['headsign']
        stevilka3 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['line']['short_name']
        #print('ODHOD:', ura_odhoda, departure_stop,'PRVI PRESTOP:', ura_prihoda, arrival_stop,'CILJ1:', ura_prihoda2, arrival_stop2, smer, stevilka,"CILJ2:", smer2, stevilka2, "konec:", ura_prihoda3, arrival_stop3, smer3, stevilka3)
        return ura_odhoda, ura_prihoda, departure_stop, arrival_stop, ura_prihoda2, arrival_stop2, smer, stevilka, smer2, stevilka2
    except (IndexError, KeyError)  :
        pass
            


    try:
        ura_odhoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_time']['text']
        ura_prihoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_time']['text']
        departure_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_stop']['name']
        arrival_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_stop']['name']
        smer = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['headsign']
        stevilka = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['line']['short_name']
        ura_prihoda2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['arrival_time']['text']
        arrival_stop2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['arrival_stop']['name']
        smer2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['headsign']
        stevilka2 = data2['routes'][n]['legs'][0]['steps'][3]['transit_details']['line']['short_name']
        #print('ODHOD:', ura_odhoda, departure_stop,'PRVI PRESTOP:', ura_prihoda, arrival_stop,'CILJ:', ura_prihoda2, arrival_stop2, smer, stevilka,"presledek:", smer2, stevilka2)
        return ura_odhoda, ura_prihoda, departure_stop, arrival_stop, ura_prihoda2, arrival_stop2, smer, stevilka, smer2, stevilka2
    except (IndexError, KeyError)  :
        pass
            
    try:
        ura_odhoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_time']['text']
        ura_prihoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_time']['text']
        departure_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_stop']['name']
        arrival_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_stop']['name']
        smer = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['headsign']
        stevilka = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['line']['short_name']
        ura_prihoda2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['arrival_time']['text']
        arrival_stop2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['arrival_stop']['name']
        smer2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['headsign']
        stevilka2 = data2['routes'][n]['legs'][0]['steps'][2]['transit_details']['line']['short_name']
        #print('ODHOD:', ura_odhoda, departure_stop,'PRVI PRESTOP:', ura_prihoda, arrival_stop,'CILJ:', ura_prihoda2, arrival_stop2, smer, stevilka,"presledek:", smer2, stevilka2)
        return ura_odhoda, ura_prihoda, departure_stop, arrival_stop, ura_prihoda2, arrival_stop2, smer, stevilka, smer2, stevilka2
    except (IndexError, KeyError)  :
        pass
        
    try:
        ura_odhoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_time']['text']
        ura_prihoda = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_time']['text']
        departure_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['departure_stop']['name']
        arrival_stop = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['arrival_stop']['name']
        smer = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['headsign']
        stevilka = data2['routes'][n]['legs'][0]['steps'][1]['transit_details']['line']['short_name']
        #print('ODHOD: ', ura_odhoda, departure_stop,'CILJ: ', ura_prihoda, arrival_stop)
        return ura_odhoda, ura_prihoda, departure_stop, arrival_stop, smer, stevilka
    except (IndexError, KeyError):
        pass

def get_directions(kraj):
    p6 = request_directions(kraj)
    return p6




