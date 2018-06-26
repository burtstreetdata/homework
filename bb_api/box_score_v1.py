#!/usr/bin/python


import base64
import requests
import json
import psycopg2



def getpwd():
    with open("/tmp/bbpwd.txt") as secretfile:
        p=secretfile.readline().strip()
    return  p

    
url='https://api.mysportsfeeds.com/v1.2/pull/mlb/2018-regular/game_boxscore.json'
username="burtstreetdata"
password=getpwd()

authstring="Basic " + base64.b64encode('{}:{}'.format(username,password).encode('utf-8')).decode('ascii')
try:
    response = requests.get(
        url=url,
        params={
#            "gameid": "20180504-BOS-TEX",
            "gameid": "20180624-SD-SF",
            "teamstats": "none",
            "playerstats": "none"
        },
        headers={
            "Authorization": authstring
        }
    )
    print('Response HTTP Status Code: {status_code}'.format(status_code=response.status_code))
    if not response.ok :
        print('\nThe submitted headers were ' + authstring)
        # return None
        print ('fail')
    else:
        pass
except requests.exceptions.RequestException:
    print('HTTP Request failed and said: ' + response.content)
    print('The headers were ' + headers)

parsed = json.loads(response.content.decode('utf-8'))

innings = parsed["gameboxscore"]["inningSummary"]["inning"]
for inning in innings:
    print (inning)

    
# response= send_request()
# if response != None:
#     parsed= json.loads(response.content.decode('utf-8'))

# else:
#     print ("it broke")
#     exit

# hostname = "localhost"
# username="innings"
# password="innings"
# dbname="bigly"

# myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=dbname )
# for g in parsed["fullgameschedule"]["gameentry"]:
#     (away,home) = g["awayTeam"], g["homeTeam"]
#     (awayAbbv,homeAbbv) = (away["Abbreviation"], home["Abbreviation"])
#     dateX = g["date"].replace("-", "")
#     gameid=f"{dateX}-{awayAbbv}-{homeAbbv}"
#     print ( g["date"], g["time"],  away["Name"],  home["Name"], gameid)
    

# myConnection.close()
# print ("dog closed")



        
