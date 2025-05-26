import speech_recognition as sr
import webbrowser #built-in module
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer() #it will recognize the voice
engine = pyttsx3.init() #it will speak
#it will take the voice input from the microphone
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
        if "open google" in c.lower():
            speak("opening google")
            webbrowser.open("www.google.com")
        elif "open youtube" in c.lower():
                speak("opening youtube")
                webbrowser.open("www.youtube.com")
        elif "open facebook" in c.lower():
                speak("opening facebook")
                webbrowser.open("www.facebook.com")
        elif "open instagram" in c.lower():
                speak("opening instagram")
                webbrowser.open("www.instagram.com")
        elif "open whatsapp" in c.lower():
                speak("opening whatsapp")
                webbrowser.open("https://web.whatsapp.com/")
        elif "open linkedin" in c.lower():
                speak("opening linkedin")
                webbrowser.open("www.linkedin.com")
        elif "open github" in c.lower():
                speak("opening github")
                webbrowser.open("www.github.com")
        elif "open w3schools" in c.lower():
                speak("opening w3schools")
                webbrowser.open("www.w3schools.com")
        elif "open geeksforgeeks" in c.lower():
                speak("opening geeksforgeeks")
                webbrowser.open("www.geeksforgeeks.com")
        elif "open hackerrank" in c.lower():
                speak("opening hackerrank")
                webbrowser.open("www.hackerrank.com")
        elif "open gmail" in c.lower():
                speak("opening gmail")
                webbrowser.open("www.gmail.com")
        elif "open yahoo" in c.lower():
                speak("opening yahoo")
                webbrowser.open("www.yahoo.com")
        elif "open amazon" in c.lower():
                speak("opening amazon")
                webbrowser.open("www.amazon.com")
        elif "open flipkart" in c.lower():
                speak("opening flipkart")
                webbrowser.open("www.flipkart.com")

                #it will play the songs 
        elif c.lower().startswith("play"):
               song =c.lower().split(" ")[1]
               link = musiclibrary.music[song]
               webbrowser.open(link)



if __name__=="__main__":
     speak("Hello, I am Anshika assistent. How can I help you?")
while True: 
        #recognizing the voice 
         r=sr.Recognizer()#recognize the voice


         print("recognizing...")
         try:
            with sr.Microphone() as source:#it will take the voice input from the microphone
                print("Listening...")
                r.pause_threshold=1#it will wait for 1 second
                audio=r.listen(source)#it will listen the voice
                command=r.recognize_google(audio)
            print(command)
            if(command.lower()=="jarvis"):#if the command is jarvis then it will listen the command
                speak("Yes, I am listening")#it will speak
                #it will take the command from the user
                with sr.Microphone() as source:
                    print("jarvis active...")
                    r.pause_threshold=1
                    audio=r.listen(source)
                command=r.recognize_google(audio)

               
                processcommand(command)#it will process the command

         except Exception as e:#if there is any error then it will print the error
               print("Error; {0}".format(e))