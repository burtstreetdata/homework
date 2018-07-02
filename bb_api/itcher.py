#!/usr/bin/python


import base64
import requests
import json
import psycopg2



def getpwd():
       with open("/mnt/c/tmp/bbpwd.txt") as secretfile:
              p=secretfile.readline().strip()
              return  p

    
url='https://api.mysportsfeeds.com/v1.2/pull/mlb/2018-regular/game_playbyplay.json'
username="burtstreetdata"
password=getpwd()

authstring="Basic " + base64.b64encode('{}:{}'.format(username,password).encode('utf-8')).decode('ascii')
try:
    response = requests.get(
        url=url,
        params={
            "gameid": "20180630-MIN-CHC",
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

batters = parsed["gameplaybyplay"]["atBats"]["atBat"]
for batter in batters :
       abp = batter['atBatPlay']
       for bu in abp:
              ispitch =  type(bu) is dict and 'pitch' in bu
              if ispitch:
                     pitch = bu["pitch"]
                     batsman=str.format(f"{pitch['battingPlayer']['LastName']}, {pitch['battingPlayer']['FirstName']}")
                     pitcher=str.format(f"{pitch['pitchingPlayer']['LastName']}, {pitch['pitchingPlayer']['FirstName']}")
                     if 'ballStartSpeed' in pitch and 'ballEndSpeed' in pitch:
                            startEnd = str.format(f"{pitch['ballStartSpeed']}=>{pitch['ballEndSpeed']}")
                     else:
                            startEnd = "speeds N/A"
                     print (f"{batsman}/{pitcher} : {startEnd} : {pitch['result']}")



