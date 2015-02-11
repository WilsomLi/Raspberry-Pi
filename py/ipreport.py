# report ip to instapush

import pycurl,json,socket
from StringIO import StringIO

appID = "54d825d7a4c48a2f53ff7ea6"

appSecret = "2840c1ad1f0d7a27b6d5e2f8402913d2"

pushEvent = "IPReport"
pushMessage = "IP:"

localIP = socket.gethostbyname(socket.gethostname())

buffer = StringIO()

c = pycurl.Curl()
c.setopt(c.URL,'https://api.instapush.im/post')
c.setopt(c.HTTPHEADER, ['x-instapush-appid: ' + appID,
'x-instapush-appsecret: ' + appSecret,
'Content-Type: application/json'])

json_fields = {}
json_fields['event'] = pushEvent
json_fields['trackers'] = {}
json_fields['trackers']['message'] = pushMessage + localIP

postfields = json.dumps(json_fields)

c.setopt(c.POSTFIELDS, postfields)
c.setopt(c.WRITEFUNCTION,buffer.write)

c.setopt(pycurl.SSL_VERIFYPEER, 0)

c.perform()
body = buffer.getvalue()
print(body)

buffer.truncate(0)
buffer.seek(0)
c.close()
