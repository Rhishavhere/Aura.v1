from ollama import chat

MODEL_NAME = 'hf.co/cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf:Q5_K_M'
history = []

def gen(prompt):
  system = ('Answer in short and very brief. do not exceed two lines')

  messages = [{'role':'system','content': system}]
  messages.extend(history)
  messages.append({'role':'user','content': prompt})
  
  try:
    response = chat(model=MODEL_NAME, messages=messages)

    history.append({'role':'user','content': prompt})
    history.append({'role':'assistant','content': response.message.content})
    return response.message.content
  except Exception as e:
    print(f'ERROR : {e}')


def call(prompt):
  system = (
    'You are an AI function callling model. You will determine whether extracting the users clipboard content, '
    'taking a screenshot, capturing the webcam or calling no functions is best for a voice assistant to respond '
    'to the users prompt. The webcam can be assumed to be a normal laptop webcam facing the user. You will '
    'respond with only one selection from this list: ["extract clipboard", "take screenshot", "capture webcam", "None"] \n'
    'You MUST NOT respond with anything but the most logical selection from the list with no explanations. Format the '
    'function call name exactly as I listed'
  )

  func_convo = [{'role':'system','content': system},
                {'role':'user','content': prompt}]
  
  try:
    response = chat(model=MODEL_NAME, messages=func_convo)
    return response.message.content
  except Exception as e:
    print(f'ERROR : {e}')

while True:
  prompt = input('USER : ')
  response = gen(prompt)
  function_call = call(prompt)

  print(f'CALL : {function_call}')
  print(f'AI : {response}')
