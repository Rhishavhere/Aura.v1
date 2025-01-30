from PIL import ImageGrab

def take_screenshot():
  path = 'screen.jpg'
  screen = ImageGrab.grab()
  rgb_screen = screen.convert('RGB') 
  rgb_screen.save(path, quality=15)

take_screenshot()