#!/usr/bin/python


import base64
import requests
import json
import psycopg2




def send_request():
    with open("/tmp/bbpwd.txt") as secretfile:
        p=secretfile.readline().strip()
        username="burtstreetdata"
        password=p
        pullurl= "https://api.mysportsfeeds.com/v1.2/pull/mlb/2018-regular/full_game_schedule.json"
        authstring="Basic " + base64.b64encode('{}:{}'.format(username,password).encode('utf-8')).decode('ascii')
    try:
        response = requests.get(
            url=pullurl,
            params={
                "date": "from-20180426-to-20180430"
            },
            headers={
                "Authorization": authstring
            }
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        if not response.ok :
            print('\nThe submitted headers were ' + authstring)
            return None
        else:
            return  response
        
        
    except requests.exceptions.RequestException:
        print('HTTP Request failed and said: ' + response.content)
        print('The headers were ' + headers)
        
response= send_request()
if response != None:
    parsed= json.loads(response.content.decode('utf-8'))

else:
    print ("it broke")
    exit

hostname = "localhost"
username="innings"
password="innings"
dbname="bigly"

myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=dbname )
for g in parsed["fullgameschedule"]["gameentry"]:
    (away,home) = g["awayTeam"], g["homeTeam"]
    (awayAbbv,homeAbbv) = (away["Abbreviation"], home["Abbreviation"])
    dateX = g["date"].replace("-", "")
    gameid=f"{dateX}-{awayAbbv}-{homeAbbv}"
    print ( g["date"], g["time"],  away["Name"],  home["Name"], gameid)
    

myConnection.close()
print ("dog closed")



        
