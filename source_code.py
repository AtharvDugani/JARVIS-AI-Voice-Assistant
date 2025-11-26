import re
import os
import time
import subprocess
import win32com.client
from datetime import datetime
from google import genai
import speech_recognition as sr
# import google.generativeai as genai


#Todo: To convert text to speech
speaker = win32com.client.Dispatch("SAPI.SpVoice")
def say(text):
    speaker.speak(text)


# Todo: To take command from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2
        try:
            query = r.recognize_google(r.listen(source), language="en-in")
            print("Recognizing....")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. Sorry from Jarvis"


# Todo: To remove emojis from the text
def remove_emojis(text):
    # Define the regex pattern to match all emoji characters
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002700-\U000027BF"  # Dingbats
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U00002600-\U000026FF"  # Miscellaneous Symbols
        u"\U00002B50-\U00002B50"  # star
        u"\U00002300-\U000023FF"  # various symbols
        u"\U00002500-\U000025FF"  # geometric shapes
        "]+", flags=re.UNICODE
    )
    
    return emoji_pattern.sub(r'', text)


def the_time():
    t = time.strftime("%I:%M %p")
    return t      


def store_ai_response(query):

    say("Your query is in the process")
    text = f"JARVIIS's response for prompt: {query} \n\n\t\t\t***************************\n\n"

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=query
    )
    text += response.text
    with open(f"{query}.docx","w") as file:
        file.write(text)

    say("Your result for the query is ready. If you want I can open it for you.")
    print("Listening....")
    reply = takeCommand()
    if "yes".lower() in reply.lower():
        def open_file(file_path):
            try:
                subprocess.run(['start', '', file_path], check=True, shell=True)
            except subprocess.CalledProcessError as e:
                print(f"Error opening file: {e}")

        # Example usage
        file_path = f"E:\Programming languages\JARVIS Project\\{query}.txt"
        open_file(file_path)
    say("Here you go")
    say("Anything else I can assist you with")



