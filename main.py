from ollama import chat
from PIL import ImageGrab
import cv2
import pyperclip

web_cam = cv2.VideoCapture(0)

MODEL_NAME = 'hf.co/cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf:Q5_K_M'
history = []

def gen(prompt):
  system = ('Answer in short and very brief. do not exceed one line')

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

def take_screenshot():
  path = 'screen.jpg'
  screen = ImageGrab.grab()
  rgb_screen = screen.convert('RGB') 
  rgb_screen.save(path, quality=15)

def web_cam_capture():
  if not web_cam.isOpened():
    print('Error opening camera')
    exit()

  path = 'webcam.jpg'
  ret,frame = web_cam.read()
  cv2.imwrite(path, frame)

def clipboard():
  clipboard_content = pyperclip.paste()
  if isinstance(clipboard_content, str):
    return clipboard_content
  else:
    print("No clipboard text found")
    return None

while True:
  prompt = input('USER : ')
  response = gen(prompt)
  function_call = call(prompt)

  print(f'CALL : {function_call}')
  print(f'AI : {response}')
