from telethon import TelegramClient, events
from config import *
import re
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

client = TelegramClient('choregayie', api_id, api_hash)

def placeOrder(target):
    print(f'Target: {target}')

def check_statement(statement):
    
    regex = r"Address:"
    match = re.search(regex, statement, re.IGNORECASE)
    return bool(match)

def find_next_word_after_word(statement, target_word):
    regex = r'{}:\s*(\S+)'.format(re.escape(target_word))
    match = re.search(regex, statement, re.IGNORECASE)
    if match:
        return match.group(1)
    else:
        return None

loop_counter = 0  # Initialize loop counter

@client.on(events.NewMessage(chats=-1001383758776))
async def my_event_handler(event):
    global loop_counter  # Declare loop_counter as a global variable
    if loop_counter >= 1:  # Check if loop_counter has reached 1 or more
        return  # Exit the event handler
    loop_counter += 1  # Increment loop counter

    statement = event.raw_text
    if check_statement(statement):
        address = find_next_word_after_word(statement, 'Address')
        if address:
            await client.send_message(5486942816, f'{address}')
        placeOrder(address)
        print(f'Pattern match for entry {statement}')
        time.sleep(60)
    else:
        print("ignore")

client.start()
client.run_until_disconnected()

