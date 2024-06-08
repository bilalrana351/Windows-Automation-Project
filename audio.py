import pyaudio
import wave
import keyboard
import datetime
import os
import WhisperModel

# Now we will load the model here
# However in production it will be more favourable if the model was loaded in the application workflow
WhisperModel.loadWhisperModel("base.en")

def getTranscribedAudio(): 
    # Set up parameters for recording
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024

    now = datetime.datetime.now()
    WAVE_OUTPUT_FILENAME = f"recording.wav"

    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    frames = []

    recording = True  # Flag to control recording

    # TODO: This statement will be removed at the time of the production
    print("Recording")

    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

        # Check if the SPACE key has been pressed
        # We will have to change it to the desired key
        # TODO : In actual production we will like it to be a button like the tab button, will have to be decided later
        if keyboard.is_pressed(' '):
            recording = False

    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    # TODO : This will have to be removed at the time of production
    print(WAVE_OUTPUT_FILENAME + " has been saved")

    # Now this will be the code that will call the openai whisper model
    transcript = WhisperModel.callWhisperModel(WAVE_OUTPUT_FILENAME)

    os.remove(WAVE_OUTPUT_FILENAME)

    # TODO : This will have to be removed at the time of production
    print("Removed the file")

    # TODO : This will have to be removed at the time of production
    print(transcript)

    return transcript 

# This file is not meant to be run directly, if anyone tries to run it directly we will raise an error
if __name__ == "__main__":
    raise Exception("This file is not meant to be run directly")