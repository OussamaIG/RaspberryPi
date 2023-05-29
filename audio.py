import speech_recognition as sr

def convert_audio_to_text():
    r = sr.Recognizer()

    # Initialize the microphone as the audio source
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")

        # Adjust the microphone for ambient noise
        r.adjust_for_ambient_noise(source)

        # Capture the audio input from the microphone
        audio = r.listen(source)

    try:
        # Use the Google Speech Recognition API to convert speech to text
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Unable to recognize speech.")
    except sr.RequestError as e:
        print("Error occurred; {0}".format(e))

# Call the function to convert audio to text
converted_text = convert_audio_to_text()
print("Converted Text: ", converted_text)
