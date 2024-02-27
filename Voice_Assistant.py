import sys
import threading

import speech_recognition as sp
import pyttsx3 as tts

from neuralintents import GenericAssistant

class Assistant:
    def __init__(self):
        self.recognizer = sp.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty('rate', 150)
        
        self.assistant = GenericAssistant('intents.json')
        self.assistant.train_model()
        
        threading.Thread(target=self.start_listening).start()
        
        
    def start_listening(self):
        while True:
            try:
                with sp.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
                    audio = self.recognizer.listen(mic)
                    
                    message = self.recognizer.recognize_google(audio)
                    message = message.lower()
                    
                    if "wake up" in message:
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()
                        if text == "stop":
                            self.speaker.say("Goodbye")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            sys.exit(0)
                        
                        else:
                            if text is not None:
                                response = self.assistant.request(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
                        
                        
                    response = self.assistant.request(message)
                    print(response)
                    
                    self.speaker.say(response)
                    self.speaker.runAndWait()
                    
            except:
                continue
                
if __name__ == '__main__':
    Assistant()