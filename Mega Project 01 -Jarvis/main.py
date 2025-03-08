import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclilb
import google.generativeai as genai
import os
import pywhatkit

# pip install pocketsphinx
recognizer = sr.Recognizer()
engine = pyttsx3.init()

genai.configure(api_key="AIzaSyAt0LgM3prsEo5wbb3_TykRJ38bP2XSXZo")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-2.0-flash")

'''genai.configure(api_key="AIzaSyBQ33EsjqRxdiJzBtG_oe6lNBaArWIDaYU")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-pro-exp-02-05",
    generation_config=generation_config,
)
# Start a chat session (allows context retention)
chat_session = model.start_chat(history=[])'''

def speak(text):
    engine.say(text)
    engine.runAndWait()

# def speak(text):
    # tts = gTTS(text)
    # tts.save('temp.mp3')

'''def aiProcess(command):
    try:
        response = chat_session.send_message(command)
        return response.text if hasattr(response, "text") else "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"Error processing AI response: {e}" '''

def aiProcess(command):
    try:
        response = model.generate_content(command)
        return response.text if hasattr(response, "text") else "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"Error processing AI response: {e}" 

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open linked in" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play "):
        song = c.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song) 
    elif c.lower().startswith("playsong"):
        song=c.lower().split(" ")[1]
        link=musiclilb.music[song]
        webbrowser.open(link)

    else:
        # Let integrate open AI
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__" :
    speak("Hello......Welcome to Jarivis.....How can i help you")
    while True:
        # obtain audio from microphone
        r = sr.Recognizer() 
        print("recognizing.....") 
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                 print("Listening....")
                 audio = r.listen(source,timeout=2,phrase_time_limit=3)
            word=r.recognize_google(audio)
            if(word.lower()== "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("jarvis Active")
                    audio = r.listen(source,timeout=2)
                    command=r.recognize_google(audio)

                    processCommand(command)

            
        except Exception as e:
            print("error; {0}".format(e))