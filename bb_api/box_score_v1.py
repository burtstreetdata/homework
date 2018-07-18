

import base64
import requests
import json



def getpwd():
       with open("/mnt/c/tmp/bbpwd.txt") as secretfile:
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
            "gameid": "20180624-CHC-CIN",
#            "gameid": "20180624-SD-SF",
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
i=0
for inning in innings:
    print (f"There's {inning['awayScore']} for {inning['@number']} and home gets {inning['homeScore']}")


