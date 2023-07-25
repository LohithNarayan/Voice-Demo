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
    "extensionNumber": "307",
  "type": "Department",
  "contact": {
    "firstName": "Marketing Q",
    "email": "marketing@example.com"  }
  }
#To read all members (user extensions) of a call queue:
resp = platform.get('/restapi/v1.0//account/11111111/call-queues/22223333/members')

print(resp.text())