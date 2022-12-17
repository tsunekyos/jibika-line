import requests
import json
import config

URL = 'https://api.line.me/v2/bot/message/push'
HEADERS = {
  'Content-Type': 'application/json' ,
  'Authorization': 'Bearer ' + config.LINE_CHANNEL_ACCESS_TOKEN,
}

PAYLOAD_BASE = {
    "to": config.LINE_USER_ID,
    "messages":[
      {
        "type": "text",
        "text": '',
      }
    ]
}

print(config.LINE_CHANNEL_ACCESS_TOKEN)
print(config.LINE_USER_ID)

def create_payload(text):
  payload = PAYLOAD_BASE
  payload['messages'][0]['text'] = text
  return json.dumps(payload)

def post_line_notify(text):
  
  payload = create_payload(text)
  response = requests.post(URL, data=payload, headers=HEADERS)

  print(response)
  print('done: post_line_notify')
