from ollama import chat

MODEL_NAME = 'llama3.2:1b'
history = []

def gen(prompt):
  system = ('Answer in short and very brief. do not exceed two lines')

  messages = [{'role':'system','content': system}]

  messages.extend(history)

  messages.append({'role':'user','content': prompt})
  print('----------')
  print(messages)
  print('----------')
  
  try:
    response = chat(model=MODEL_NAME, messages=messages)

    history.append({'role':'user','content': prompt})
    history.append({'role':'assistant','content': response.message.content})
    return response.message.content
  except Exception as e:
    print(f'ERROR : {e}')

while True:
  prompt = input('USER : ')
  response = gen(prompt)
  print(f'AI : {response}')
