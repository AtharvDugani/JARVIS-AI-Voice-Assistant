import os
import google.generativeai as genai
from source_code import takeCommand, remove_emojis, say, the_time
from source_code import store_ai_response


# Store chat history
conversations = []


# Get API key from environment
def get_api_key():
    return os.getenv("AIzaSyBd5jdZqL7-oQLVwhdu6W1OR7AhZXp7VQE")


# Save conversation to file
def save_conversation(query, response):
    with open("conversation_log.txt", "a", encoding="utf-8") as file:
        file.write(f"User: {query}\n")
        file.write(f"Jarvis: {response}\n\n")


# Load previous conversations to inject into session
def load_previous_conversations(session):
    if os.path.exists("conversation_log.txt"):
        with open("conversation_log.txt", "r", encoding="utf-8") as file:
            history = file.read()
            if history:
                session.send_message(f"Here is the previous conversation:\n{history}")

# Clear chat history
def clear_chat():
    global conversations
    conversations = []
    if os.path.exists("conversation_log.txt"):
        os.remove("conversation_log.txt")
        print("Chat history cleared.")
    else:
        print("No chat history to clear.")


def create_chat_session():
    genai.configure(api_key=get_api_key())
    generation_config = {
        "temperature": 0.5,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 100,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        generation_config=generation_config,
    )

    session = model.start_chat(history=[
        {
            "role": "user",
            "parts": [
                "You are Jarvis, a smart AI voice assistant developed by Atharv Dugani. "
                "You must act like a real assistant. "
                "If asked 'Who are you?' or 'Tell me about yourself', clearly say you were created by Atharv. "
                "Keep short answers short and long answers a little compressed. "
                "Be polite, helpful, and clear like a true assistant."
            ]
        }
    ])

    return session


chat_session = create_chat_session()

# AI response and history logging
def ai(prompt):
    global conversations
    try:
        response = chat_session.send_message(prompt)
        answer = remove_emojis(response.text)
        say(answer.replace('*', ''))
        conversations.append((prompt, answer))  # Log conversation
        save_conversation(prompt, answer)
        return answer
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred. Please try again."
    




# Main loop
def main():
    say("Hello Atharv! Jarvis here, how can i Assist you today? ")

    while True:
        print("Listening....")
        # query = takeCommand()
        query = input("Write your command: ")

        if "quit" in query.lower():
            say("Okay, see you.")
            break
        elif "clear chat" in query.lower():
            clear_chat()
            global chat_session
            chat_session = create_chat_session()  # Reset session after clearing

        elif "the time" in query.lower():
            say(the_time())

        elif "write" in query.lower():
            store_ai_response(query)
        
        else:
            ai(query)

if __name__ == "__main__":
    main()
