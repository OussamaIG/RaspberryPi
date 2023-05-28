import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

def record_audio(duration):
    # Set the sample rate and channels for recording
    sample_rate = 44100
    channels = 1

    # Record audio for the specified duration
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()

    return recording, sample_rate

def convert_audio_to_text(audio_file):
    r = sr.Recognizer()
    text = ""

    with sr.AudioFile(audio_file) as audio_src:
        audio = r.record(audio_src)
        text = r.recognize_google(audio)

    return text

# Record audio for 5 seconds
duration = 5
audio, sample_rate = record_audio(duration)

# Save the recorded audio as a WAV file
file_path = "recorded_audio.wav"
sf.write(file_path, audio, sample_rate)

# Convert the audio file to text
text = convert_audio_to_text(file_path)
print(text)
