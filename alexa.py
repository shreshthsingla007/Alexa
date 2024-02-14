import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyjokes
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am momo! Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def send_Email():
    
    email_lst = {"Shreshth":"221030348@juitsolan.in"}

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ranaaryan2100@gmail.com', 'dbxnkaeonoarwqfw')
    speak("What do you want in your mail?")
    content = takeCommand()
    speak("To whom do you want to send your mail?")
    mail = takeCommand()
    sendm = email_lst[mail]
    to_me = sendm
    server.sendmail(sendm, to_me, content)
    server.close()

def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}+weather&sca_esv=593522059&sxsrf=AM9HkKmOH-tuzZMCk7EI_ZWvhufttyZn-Q%3A1703483068191&ei=vBaJZbacC7vU4-EPgLOgmA4&ved=0ahUKEwi26qP58KmDAxU76jgGHYAZCOMQ4dUDCBA&uact=5&oq={city}+weather&gs_lp=Egxnd3Mtd2l6LXNlcnAiD3BhbmlwYXQgd2VhdGhlcjIQEAAYgAQYsQMYgwEYRhiAAjIFEAAYgAQyBRAAGIAEMgsQABiABBixAxiDATIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIcEAAYgAQYsQMYgwEYRhiAAhiXBRiMBRjdBNgBAUisFVAAWN4RcAB4AZABAJgBzwOgAeENqgEJMC43LjEuMC4xuAEDyAEA-AEBwgIEECMYJ8ICChAAGIAEGIoFGEPCAg0QLhiABBiKBRhDGLED4gMEGAAgQYgGAboGBggBEAEYEw&sclient=gws-wiz-serp', headers=headers)
    speak("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    speak("The weather in " + location + " is " + weather + " degrees celsius and " + info + " at " + time)

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'movie' in query:
            webbrowser.open("netflix.in")

        elif 'weight' in query:
            speak(f"in 4 days")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
       
        elif 'joke' in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            speak(My_joke)
        
        elif 'news' in query:
            
            url = 'https://www.bbc.com/news/world/asia/india'
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h3')
            for x in headlines:
                speak(x.text.strip())
                
        elif 'send email' in query:
            send_Email()
            speak("Email has been sent!")

        
        elif 'weather' in query:
            speak("Please tell the Name of City ")
            city=takeCommand()
            city = city+" weather"
            weather(city)
            
                
        elif 'hello' in query:
            speak("Hello Sir, How are you?")
        
        elif 'fine' in query:
            speak("Nice to hear that")
            
        elif 'bye' in query:
            speak("Bye Sir, have a nice day")
            break