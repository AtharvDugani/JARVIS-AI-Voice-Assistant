# Jarvis – AI Voice Assistant (Python Project)

## **Overview**

This project is a Python-based voice assistant named **Jarvis**. It listens to user commands, processes them using speech recognition and an AI model, and performs tasks like searching online, opening applications, writing files, and speaking responses. The project is structured into two Python files:

* **jarvis.py** – The main executable file that starts the assistant and handles the flow of commands.
* **source code.py** – Contains all core utility functions such as speech-to-text, text-to-speech, saving files, opening files, etc.

This modular structure makes the project clean, maintainable, and easy to expand.

---

## **Features**

* Voice input using speech recognition
* AI-generated responses
* Text-to-speech output
* Ability to save AI responses to text or documents
* Ability to open saved files
* Executes system-level tasks (tell time/date, etc.)
* Keyword-based command recognition
* Easy to add new commands

---

## **Project Structure**

```
│
├── jarvis.py            # Main file to run the assistant
├── source code.py       # Contains all functions (takeCommand, say, save file, etc.)
└── README.md
```

---

## **How It Works**

1. Run **jarvis.py**.
2. Jarvis initializes the microphone and greets the user.
3. The `takeCommand()` function (inside source code.py) listens for user input.
4. The command is processed and matched with predefined functions.
5. Jarvis speaks the result using the `say()` function.
6. If the user requests saving the output, Jarvis writes it to a file.

---

## **Key Functions (inside source code.py)**

### **takeCommand()**

Listens to the microphone and converts speech to text.

### **say(text)**

Speaks the given text out loud using text-to-speech.

### **save_to_file(text)**

Writes AI-generated responses to a `.txt` file.

### **open_saved_file()**

Opens the last saved text/document file.

### **user_wants_to_save(query)**

Detects if the user wants the response stored.

---

## **How to Run the Project**

1. Install required libraries:

```
pip install speechrecognition
pip install pyttsx3
pip install python-docx
```

(Optional libraries may vary based on your setup.)

2. Ensure your microphone is working.

3. Run the project:

```
python jarvis.py
```

4. Speak commands like:

* "Tell me the time"
* "Write a python code to explain exception handling"
* "Open the file"

---

## **Future Enhancements**

* Add GUI interface
* Add continuous listening mode
* Add chat history storage
* Add more advanced NLP-based command detection

---

## **Author**

* **Atharv Dugani**

---

## **License**

This project is for learning and personal use only.

