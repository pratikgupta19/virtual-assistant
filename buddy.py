import speech_recognition as sr    
import pyttsx3   #Text to speech
import datetime
import pywhatkit
import wikipedia
import webbrowser
import pyjokes


lr = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Buddy. Please tell me how may I help you")

def take_command():
    with sr.Microphone() as source:  #take user voice as a command
        print('Listening...')
        lr.pause_threshold=1
        voice = lr.listen(source)
    try:
        print('Recognizing...')
        command = lr.recognize_google(voice, language='en-in')
        command = command.lower()
        print(f"You said: {command}\n")
        #check buddy in the command if it there return the conmmand else return none 
        if 'buddy' in command:       
            command = command.replace('buddy', '')
            #print(command)
            return command
        else:
            print("Say that again please...")
            speak("Say that again please...")
            return "none"
    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "none"
    #return command

if __name__ == "__main__":
    wishMe()
    while True:
        command = take_command()
        if 'play' in command:    #if play is in the command take the song name play the song in youtube
            song = command.replace('play', '')
            speak('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:  #It will tell u the current time
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('Current time is ' + time)
        elif 'wikipedia' in command:   #it will search the command in wikipedia
            print("Searching Wikipedia...")
            speak('searching Wikipedia')
            command = command.replace('wikipedia', '')
            info = wikipedia.summary(command, sentences=3)  # it will speak and show 3 sentences
            print(info)
            speak(info)
        elif 'joke' in command:   #it will tell u the joke
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        elif 'open youtube' in command:  
            webbrowser.open("youtube.com")
        elif 'open google' in command:
            webbrowser.open("google.com")
        elif 'search' in command:
            print("Searching...")
            speak("Searching...")
            command = command.replace('search', '')
            pywhatkit.search(command)
        elif 'send message' in command:   #for sending whatsapp message 
            if 'pratik home' in command:    
                speak('What message do you want to send')
                msg = take_command()
                speak('Message will be send within 1 minute')
                hour = int(datetime.datetime.now().hour)
                minu = int(datetime.datetime.now().minute)
                pywhatkit.sendwhatmsg("+919*******00", msg, hour, minu+1)
                speak('message sent Successfully')
            elif 'Sagar Bhai' in command:
                speak('What message do you want to send')
                msg = take_command()
                speak('Message will be send within 1 minute')
                hour = int(datetime.datetime.now().hour)
                minu = int(datetime.datetime.now().minute)
                pywhatkit.sendwhatmsg("+919*******54", msg, hour, minu+1)
                speak('message sent Successfully')
        elif  ('+' or 'plus' or 'add') and 'what is' in command:
            command = command.replace('add', '')
            command = command.replace('plus', '')
            command = command.replace('what is', '')
            print(command + ' = ', end="")
            if '+' in command:
                x = command.split(' + ')
                s=0
                for i in x:
                    s+=float(i)
                print(s)
                s= str(s)
                speak(command + '=' + s)
            elif '-' in command:
                x = command.split(' - ')
                s1= float(x[0])
                for i in range(1, len(x)):
                    s1-=float(i)
                print(s1)
                s1= str(s1)
                speak(command + '=' + s1) 

        elif  ('-' or 'minus' or 'subtract') and 'what is' in command:
            command = command.replace('minus', '')
            command = command.replace('subtract', '')
            command = command.replace('what is', '')
            print(command + '=')
            x = command.split(' - ')
            s1=0
            for i in x:
                s1-=float(i)
            print(s1)
            s1= str(s1)
            speak(command + '=' + s1)
