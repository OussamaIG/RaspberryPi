import speech_recognition as sr

def listen_and_transcribe():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for 5 seconds...")
        audio = r.listen(source, phrase_time_limit=5)
    
    try:
        text = r.recognize_google(audio)
        print("Transcription:", text)
        if 'weather' in text.lower():
            return 1
        else:
            return 0
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
        return 0
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return 0

result = listen_and_transcribe()
print("Result:", result)
