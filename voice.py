import speech_recognition as sr

class demo:
    
    def __init__(self):
        self.text=None
       
    def audio(self):     # string will have local scope, use self.<Var> for class-level scope
        print ("inside function")
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
      
        try:
            
             st=r.recognize_google(audio)
             if st is not None:
                   self.text=st
                   return self.text                                   
           
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))



