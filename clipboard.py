import pyperclip

def clipboard():
  clipboard_content = pyperclip.paste()
  if isinstance(clipboard_content, str):
    return clipboard_content
  else:
    print("No clipboard text found")
    return None

print(clipboard())