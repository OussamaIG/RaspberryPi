import sounddevice as sd
import speech_recognition as sr
import numpy as np
import io

def record_audio(duration):
    print("Recording started. Speak into the microphone...")
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1)
    sd.wait()  # Wait until recording is complete
    print("Done")
    return audio


def convert_audio_to_text(audio):
    r = sr.Recognizer()
    audio_data = audio.flatten()
    text = ""

    audio_file = io.BytesIO()
    np.save(audio_file, audio_data)
    audio_file.seek(0)

    with sr.AudioFile(audio_file) as audio_src:
        audio_data = audio_file.read()
        audio_src.write_frames(audio_data)

        try:
            audio = r.record(audio_src)
            text = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service: {e}")

    return text


record_duration = 5  # Specify the duration of the recording in seconds
audio = record_audio(record_duration)
text = convert_audio_to_text(audio)
print("Transcription:", text)