import speech_recognition as sr
from dotenv import load_dotenv
import os
import pyttsx3
import openai

load_dotenv()

API_KEY = os.getenv("API_KEY")
openai.api_key = API_KEY

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

names = []

name  = "trisha"



if name not in names:
    names.append(name)
    

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_response(text):
    model_id = "gpt-3.5-turbo"
    completion = openai.ChatCompletion.create(
    model=model_id,
    messages=[{"role": "user", "content": text}]
    )
    return completion.choices[0].message.content

def model_riya():
    values = {'ques': "", "answer" : ""}
    flag = True
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source,phrase_time_limit=6)
            command = listener.recognize_google(voice)
            question = question = f"just ask a single question related to '{command}' without anything other than question"
            response = get_response(question)
            print(response , ">>" , command)
            while flag:
                if values['ques'] != "":
                    talk(values['ques'])
                    print(values['ques'],">>>>>")
                    voice = listener.listen(source,phrase_time_limit=6)
                    command = listener.recognize_google(voice)
                    question = question = f'''
                                        ask simple related question to this question and reply  . 
                                        question - "{values['ques']}" 
                                        reply  - "{command}"'''
                    
                    if "come again" in command:
                        talk(values['ques'])
                        voice = listener.listen(source,phrase_time_limit=6)
                        command = listener.recognize_google(voice)
                        question = question = f'''
                                            ask simple related question to this question and reply  . 
                                            question - "{values['ques']}" 
                                            reply  - "{command}"'''
                        response = get_response(question)
                        values['ques'] = response
                        continue
                    if "stop" in command:
                        talk(f"YOU are doing great, come again fast")
                
                        return
                    response = get_response(question)
                    values['ques'] = response
                else:
                    talk(response)
                    voice = listener.listen(source,phrase_time_limit=6)
                    command = listener.recognize_google(voice)
                    question = question = f'''
                                        ask simple related question to this question and reply  . 
                                        question - "{response}" 
                                        reply  - "{command}"'''
                    if "stop" in command:
                        talk(f"YOU are doing great, come again fast")
                        return
                    response = get_response(question)
                    values['ques'] = response
    except:
        pass
    
def main(name):
    try:
        talk(f"hey {name}, on which topic we can speak today")
        model_riya()
            
    except:
        talk("facing some problem with the software")
        
        
if st.button("submit"):
    main(name)