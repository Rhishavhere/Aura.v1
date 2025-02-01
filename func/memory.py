import json

system_msg = (" ")

def save_conversation():
    with open('./screens/conversation_history.json', 'w') as f:
        json.dump(convo, f)

def load_conversation():
    global convo
    try:
        with open('./screens/conversation_history.json', 'r') as f:
            convo = json.load(f)
    except FileNotFoundError:
        convo = [{'role':'system', 'content':system_msg}]

while True:
    prompt = input('USER : ')
    
    if prompt.lower() in ['load']:
        load_conversation()
        print("Previous conversation loaded")
        continue

    
    # before the response generation
    save_conversation()