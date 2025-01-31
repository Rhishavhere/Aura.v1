from ollama import chat
from PIL import ImageGrab, Image
import cv2
import pyperclip
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

web_cam = cv2.VideoCapture(0)
MODEL_NAME = 'hf.co/cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf:Q5_K_M'
history = []

genai.configure(api_key = os.getenv('GEMINI_API'))
genai_config = {
  'temperature':0.7,
  'top_p':1,
  'top_k':1,
  'max_output_tokens':2048
}
model = genai.GenerativeModel('gemini-1.5-flash-latest', generation_config=genai_config)

system_msg = (
  'You are a multi-modal AI voice assistant. Your user may or may not have attached a photo for context '
  '(either a screenshot or a webcam capture). Any photo has already been processed into a highly detailed '
  'text prompt that will be attached to their transcribed voice prompt. Generate the most useful and '
  'factual response possible, carefully considering all previous generated text in your response before '
  'adding new tokens to the response. Do not expect or request images, just use the context if added. '
  'Use all of the context of this conversation so your response is relevant to the conversation. Make '
  'your responses clear and concise, avoiding any verbosity. ANSWER IN VERY SHORT AND BRIEF. DO NOT OVER EXPLAIN'
)
convo = [{'role':'system', 'content':system_msg}]

def gen(prompt, img_context):
  if img_context:
    prompt = f'USER PROMPT: {prompt}\n\n  IMAGE CONTEXT: {img_context}'
  convo.append({'role':'user','content':prompt})
  
  response = chat(model=MODEL_NAME, messages=convo)
  convo.append({'role':'assistant', 'content': response.message.content})
  return response.message.content

def function_call(prompt):
  system = (
    'You are an AI function callling model. You will determine whether extracting the users clipboard content, '
    'taking a screenshot, capturing the webcam or calling no functions is best for a voice assistant to respond '
    'to the users prompt. The webcam can be assumed to be a normal laptop webcam facing the user. You will '
    'respond with only one selection from this list: ["extract clipboard", "take screenshot", "capture webcam", "None"] \n'
    'You MUST NOT respond with anything but the most logical selection from the list with no explanations. Format the '
    'function call name exactly as I listed'
  )

  # func_convo = [{'role':'system','content': system},
  #               {'role':'user','content': prompt}]
  func_convo = f"System: {system}\nUser: {prompt}"

  response = model.generate_content(func_convo)
  return response.text
  # response = chat(model=MODEL_NAME, messages=func_convo)
  # return response.message.content

def take_screenshot():
  path = './screens/screenshot.jpg'
  screen = ImageGrab.grab()
  rgb_screen = screen.convert('RGB') 
  rgb_screen.save(path, quality=15)

def web_cam_capture():
  if not web_cam.isOpened():
    print('Error opening camera')
    exit()

  path = './screens/webcam.jpg'
  ret,frame = web_cam.read()
  cv2.imwrite(path, frame)

def clipboard():
  clipboard_content = pyperclip.paste()
  if isinstance(clipboard_content, str):
    return clipboard_content
  else:
    print("No clipboard text found")
    return None
  
def vision_prompt(prompt, photo_path):
  img  = Image.open(photo_path)
  prompt = (
    'You are the vision analysis AI that provides semtantic meaning from images to provide context '
    'to send to another AI that will create a response to the user. Do not respond as the AI assistant '
    'to the user. Instead take the user prompt input and try to extract all meaning from the photo '
    'relevant to the user prompt. Then generate as much as objective data about the image for the AI '
    f'assistant who will respond to the user. \nUSER PROMPT: {prompt}'
  )
  response = model.generate_content([prompt, img])
  return response.text

while True:
  prompt = input('USER : ')
  call = function_call(prompt)

  if 'take screenshot' in call:
    print('Taking Screenshot')
    take_screenshot()
    visual_context = vision_prompt(prompt=prompt, photo_path='./screens/screenshot.jpg')
  elif 'capture webcam' in call:
    print('Capturing Webcam')
    web_cam_capture()
    visual_context = vision_prompt(prompt=prompt, photo_path='./screens/webcam.jpg')
  elif 'extract clipboard' in call:
    print('copying Clipboard')
    paste = clipboard()
    prompt = f'{prompt}\n\n CLIPBOARD CONTENT: {paste}'
    visual_context = None
  else:
    visual_context = None

  response = gen(prompt=prompt, img_context = visual_context)
  # print(f'CONTEXT : {visual_context}')
  print(response)