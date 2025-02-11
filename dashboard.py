#not skilled enough with tkinter. Made with AI

import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class AuraDashboard(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Aura Graphical Dashboard")
        self.geometry("900x600")
        self.configure(bg="black")  # Set the overall background to black

        # Create a top frame for conversation (left) and images (right)
        top_frame = tk.Frame(self, bg="black")
        top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left frame: Conversation Log
        conversation_frame = tk.Frame(top_frame, bg="black")
        conversation_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.create_conversation_section(conversation_frame)

        # Right frame: Images (stacked vertically)
        images_frame = tk.Frame(top_frame, bg="black")
        images_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        self.create_images_section(images_frame)

        # Create a bottom frame for Vision Log (spanning full width)
        vision_frame = tk.Frame(self, bg="black")
        vision_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.create_vision_section(vision_frame)

    def create_conversation_section(self, parent):
        """Creates the conversation log section within the specified parent frame."""
        title = tk.Label(parent, text="Conversation Log",
                         bg="black", fg="white", font=("Helvetica", 16, "bold"))
        title.pack(anchor="n", pady=5)

        text_frame = tk.Frame(parent, bg="black")
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.conversation_text = tk.Text(text_frame, wrap="word",
                                         bg="black", fg="white", insertbackground="white")
        self.conversation_text.pack(side=tk.LEFT, fill="both", expand=True)

        conv_scrollbar = ttk.Scrollbar(text_frame, command=self.conversation_text.yview)
        conv_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.conversation_text.config(yscrollcommand=conv_scrollbar.set)

        refresh_btn = ttk.Button(parent, text="Refresh", command=self.load_conversation_log)
        refresh_btn.pack(pady=5)

        self.load_conversation_log()
    
    def load_conversation_log(self):
        """Loads the conversation logs from a file."""
        log_path = "./logs/conversation_log.txt"
        if os.path.exists(log_path):
            with open(log_path, 'r') as f:
                content = f.read()
        else:
            content = "No conversation log found."
        
        self.conversation_text.delete(1.0, tk.END)
        self.conversation_text.insert(tk.END, content)
        
    def create_vision_section(self, parent):
        """Creates the vision log section within the specified parent frame."""
        title = tk.Label(parent, text="Vision Log",
                         bg="black", fg="white", font=("Helvetica", 16, "bold"))
        title.pack(anchor="n", pady=5)

        text_frame = tk.Frame(parent, bg="black")
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.vision_text = tk.Text(text_frame, wrap="word",
                                   bg="black", fg="white", insertbackground="white")
        self.vision_text.pack(side=tk.LEFT, fill="both", expand=True)

        vision_scrollbar = ttk.Scrollbar(text_frame, command=self.vision_text.yview)
        vision_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.vision_text.config(yscrollcommand=vision_scrollbar.set)

        refresh_btn = ttk.Button(parent, text="Refresh", command=self.load_vision_log)
        refresh_btn.pack(pady=5)

        self.load_vision_log()
    
    def load_vision_log(self):
        """Loads vision analysis logs from a file."""
        log_path = "./logs/vision_log.txt"
        if os.path.exists(log_path):
            with open(log_path, 'r') as f:
                content = f.read()
        else:
            content = "No vision log found."
        self.vision_text.delete(1.0, tk.END)
        self.vision_text.insert(tk.END, content)
    
    def create_images_section(self, parent):
        """Creates the images section within the specified parent frame."""
        title = tk.Label(parent, text="Images",
                         bg="black", fg="white", font=("Helvetica", 16, "bold"))
        title.pack(anchor="n", pady=5)

        inner_frame = tk.Frame(parent, bg="black")
        inner_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Labels for displaying the screenshot and webcam images.
        self.screenshot_label = tk.Label(inner_frame, text="Screenshot",
                                         bg="black", fg="white")
        self.screenshot_label.pack(pady=10)

        self.webcam_label = tk.Label(inner_frame, text="Webcam Capture",
                                     bg="black", fg="white")
        self.webcam_label.pack(pady=10)

        refresh_images_btn = ttk.Button(parent, text="Refresh Images", command=self.load_images)
        refresh_images_btn.pack(pady=5)
        
        self.load_images()
    
    def load_images(self):
        """Loads and displays images from disk."""
        # Paths to the images.
        screenshot_path = "./screens/screenshot.jpg"
        webcam_path = "./screens/webcam.jpg"
        
        # Load screenshot if available
        if os.path.exists(screenshot_path):
            screenshot = Image.open(screenshot_path)
            screenshot.thumbnail((300, 300))
            self.screenshot_image = ImageTk.PhotoImage(screenshot)
            self.screenshot_label.config(image=self.screenshot_image, text="")
        else:
            self.screenshot_label.config(text="Screenshot not found", image="")

        # Load webcam image if available
        if os.path.exists(webcam_path):
            webcam = Image.open(webcam_path)
            webcam.thumbnail((300, 300))
            self.webcam_image = ImageTk.PhotoImage(webcam)
            self.webcam_label.config(image=self.webcam_image, text="")
        else:
            self.webcam_label.config(text="Webcam image not found", image="")

if __name__ == "__main__":
    app = AuraDashboard()
    app.mainloop() 