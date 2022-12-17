import requests
import json
import env

URL = 'https://api.line.me/v2/bot/message/push'
HEADERS = {
  'Content-Type': 'application/json' ,
  'Authorization': 'Bearer ' + env.LINE_CHANNEL_ACCESS_TOKEN,
}

PAYLOAD_BASE = {
    "to": env.LINE_USER_ID,
    "messages":[
      {
        "type": "text",
        "text": '',
      }
    ]
}

def create_payload(text):
  payload = PAYLOAD_BASE
  payload['messages'][0]['text'] = text
  return json.dumps(payload)

def post_line_notify(text):
  
  payload = create_payload(text)
  response = requests.post(URL, data=payload, headers=HEADERS)

  print(response)
  print('done: post_line_notify')
