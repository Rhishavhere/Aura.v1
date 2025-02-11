# **AURA.v1**

*`Under Active Development`*

**AURA** (Advanced Unsupervised Reinforcement Architecture) is a multi-modal AI assistant that provides intelligent, context-aware responses via both text and voice. It seamlessly integrates data from various inputs—including textual prompts, visual content (screenshots and webcam captures), clipboard contents, and voice input—to deliver concise and relevant answers.

## Key Features

- **Multi-Modal Input Processing**:
  - **Text Input:** Interact using typed commands.
  - **Voice Input:** Engage in hands-free interactions through speech recognition.
  - **Visual Input:** Incorporates screenshots and live webcam captures.
  - **Clipboard Analysis:** Uses clipboard content to add context when needed.

- **Context-Aware Responses**:
  - Leverages detailed image analysis and conversation history.
  - Combines multiple input sources into coherent, brief answers.
  - Automatically determines the appropriate function based on the user prompt.

- **Real-Time Interaction & Conversation Management**:
  - Provides immediate feedback through both on-screen text and synthesized voice.
  - Maintains conversation history, logs interactions, and allows for history clearing.
  - Custom commands support including help, exit, and even custom file creation.

- **Custom Command Support**:
  - **Voice Tone Selection:** Switch between male and female voices.
  - **Simple System Operations:** Generate text files through spoken or written prompts.

## Current Capabilities

- **AI Generation & Vision Analysis**:
  - **Text Generation:** Uses a finetuned model of Llama.
  - **Vision Analysis:** Employs "Gemma vision" (via Google Generative AI) to extract semantic details from images.
  - Integrates multi-modal context—combining visual and textual inputs—to enhance response quality.

- **Voice & Speech Integration**:
  - **Speech-to-Text:** Converts spoken input into text using SpeechRecognition.
  - **Text-to-Speech:** Responds audibly using pyttsx3, with selectable voice options.
  
- **Visual Context Extraction**:
  - **Screenshot Capture:** Automatically captures and processes desktop screenshots.
  - **Webcam Capture:** Accesses and captures images from the device's webcam.
  - Analyzes images for relevant data, logging information to aid in enhanced context processing.

- **Additional Functionality**:
  - **Clipboard Extraction:** Integrates clipboard text when deemed relevant.
  - **Conversation Logging:** Saves dialogues and vision analysis in designated log files (`./logs/conversation_log.txt` and `./logs/vision_log.txt`).
  - **Custom File Creation:** Allows the creation of text files based on in-conversation voice or text commands.

## Technical Specifications

- **Core Dependencies & Technologies**:
  - Google Generative AI
  - Ollama
  - OpenCV:
  - Pillow (PIL):
  - Pyperclip:
  - Pyttsx3:
  - SpeechRecognition:
  - python-dotenv:

- **Logging & Debugging**:
  - **Vision Log:** Captures image analysis results in `./logs/vision_log.txt`.
  - **Conversation Log:** Archives dialogue in `./logs/conversation_log.txt`.

## Usage

1. **Startup**:
   - On launch, AURA starts with a brief boot-up sequence.
   - Users choose their preferred input method: **text** or **voice**.
   
2. **Interaction**:
   - Communicate naturally using your chosen input mode.
   - AURA detects when additional context is needed and may request a screenshot, webcam capture, or clipboard extraction.
   - Issue commands such as:
     - **Help:** Displays available commands.
     - **Clear/Reset:** Resets the conversation history.
     - **Exit/Quit/Bye:** Shuts down the assistant.

3. **Voice-Specific Options**:
   - Switch between male and female voice modes with simple commands.
   - Enjoy hands-free interaction with prompt voice responses generated in real time.

## Future Development

- **Enhanced Voice Processing**:
  - Improved natural language voice interaction and emotion detection.
  
- **Expanded System Integration**:
  - Greater connectivity with external APIs and system-level automation.
  - Incorporation of advanced predictive, sentiment analysis, and multi-turn conversation features.

- **Optimization & Feature Expansion**:
  - Refinements in processing speed and response accuracy.
  - Continuous improvement in context extraction and logging mechanisms.

## Disclaimer

AURA is a work in progress and remains under active development. The current build represents a fraction of its intended full functionality. Users are encouraged to expect iterative updates and improvements over time, as experimental features are refined and new capabilities are added.

