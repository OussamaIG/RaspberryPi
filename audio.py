import sounddevice as sd

def record_audio(duration):
    print("Recording started. Speak into the microphone...")
    audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1)
    sd.wait()  # Wait until recording is complete
    print("Done")

record_duration = 5  # Specify the duration of the recording in seconds
record_audio(record_duration)
