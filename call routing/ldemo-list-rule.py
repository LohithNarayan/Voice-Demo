import os
import sys

from dotenv import load_dotenv
from ringcentral import SDK
load_dotenv()

rcsdk = SDK( os.environ.get('RC_CLIENT_ID'),
             os.environ.get('RC_CLIENT_SECRET'),
             os.environ.get('RC_SERVER_URL') )
platform = rcsdk.platform()
try:
  platform.login( jwt=os.environ.get('RC_JWT') )

except Exception as e:
  sys.exit("Unable to authenticate to platform: " + str(e))

params = {
    'enabled': True,
    'type': 'Custom',
    'name': "My weekly meetings",
    'schedule' : {
      'weeklyRanges': {
    'monday': [{ 'from': "09:00",'to': "10:00" }],
    'friday': [{ 'from': "10:00", 'to': "15:00" }]
      }
    },
    'callHandlingAction': "TakeMessagesOnly"
  }
#To get a list of all user answering rules for an extension, make a GET request to the following endpoint:

resp = platform.get('/restapi/v1.0/account/343161004/extension/808557005/answering-rule')

print(resp.text())