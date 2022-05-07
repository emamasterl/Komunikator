import requests
def get_walking_time(kraj):
    key = 'AIzaSyBeDjju_WZqy_qfbIXXt0RbC4UWTC664SE'     
    origin = 'place_id:ChIJvfl5OEMtZUcRH4phdGnSJps'     
    url = 'https://maps.googleapis.com/maps/api/directions/json?' 
    res3 = requests.get(url + 'origin=' + origin + '&destination=' + kraj + '&mode=walking'+ '&key=' + key)
    data3 = res3.json()
   #print(data3)

    z = data3['routes'][0]['legs'][0]['duration']['text']
    z2 = str.split(z)
    if z2[1] == 'mins':
        z4 = z2[0]
    elif z2[1] == 'hour':
        z4 = 60 + int(z2[2])
    elif z2[1] == 'hours':
        z4 = int(z2[0])*60 + int(z2[2])
    return z4