import requests
base_url="https://api.telegram.org/bot6972924516:AAEHdyRRedcFqwTn18FO8PMoMkEFzRWFdro"

def readMessage():
    parameters = {
        "offset": "900908021",
        "limit": "2"
    }
    response = requests.get(base_url + "/getUpdates", params=parameters)
    data = response.json()

    # Print the entire JSON response for debugging
    print("JSON Response:", data)

    # Check if 'result' key is present in the response
    if 'result' in data:
        for result in data["result"]:
            # Check if 'message' key is present in each message
            if 'message' in result:
                # Check if 'text' key is present in the message
                if 'text' in result['message']:
                    print(result['message']['text'])
                else:
                    print("No 'text' key in the message.")
            else:
                print("No 'message' key in the result.")
    else:
        print("No 'result' key in the response.")

readMessage()



import requests
import time

base_url="https://api.telegram.org/bot6972924516:AAEHdyRRedcFqwTn18FO8PMoMkEFzRWFdro"


def readMessage(offset):
    parameters = {
        "offset": offset
        # "limit": "3"
    }
    response = requests.get(base_url + "/getUpdates", data=parameters)
    data = response.json()

    for result in data.get("result", []):
        update_id = result.get("update_id")
        message_text = result.get("message", {}).get("text")

        if update_id is not None:
            print(update_id)
        if message_text is not None:
            print(message_text)

            if "Hi" in message_text:
                sendMessage(message_text)

    if data.get("result"):
        return data["result"][-1]["update_id"] + 1



def sendMessage(message):
   #messageid=message["message"]["message_id"]
   parameters = {
        "chat_id": "-1001990182506",
        "text": "Hello...",
        #"reply_to_message_id": messageid
        # "text": i
    }
   resp2 = requests.get(base_url + "/sendMessage", data=parameters)
   print(resp2.text)
  
   

offset=0
while True:
  time.sleep(2)
  offset= readMessage(offset)

