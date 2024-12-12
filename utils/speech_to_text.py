
import speech_recognition as sr

def speech_to_text_from_mic():
    recognizer = sr.Recognizer()

    
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... Speak now!")
        
        try:
           
            audio = recognizer.listen(source, timeout=10)
            print("Recognizing speech...")

          
            text = recognizer.recognize_google(audio)
            print(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Error with the speech recognition service: {e}")
            return None
