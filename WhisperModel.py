# This will be the file that will contain the code to load the whisper model first and then call it to transcribe the audio file.
import whisper
# TODO : THis will have to be removed later on
import os

# This will be the global variable for the model
model = None

# This will be the method that will be called to load the whisper model
def loadWhisperModel(name):
    global model
    try:
        # Load the model
        model = whisper.load_model(name)
        return True
    
    # If the model has not been loaded, we will return false here
    except Exception as e:
        return False
#

def callWhisperModel(audio_file):
    global model
    # This call will only run if the model has been loaded, if it has not been loaded, we will return an error
    try:
        # Call the model
        # TODO : Debugging statementd, will have to be removed at the runtime
        print("The audio file is : " + audio_file)
        print(os.listdir())
        result = model.transcribe(audio = audio_file)
    
    # If the model has not been loaded, we will return an none object
    except Exception as e:
        # TODO : Will have to be removed at the time of production
        print(e)
        return None
    
    return result["text"]

# This file is not meant to be run directly, if anyone tries to run it directly we will raise an error
if __name__ == "__main__":
    raise Exception("This file is not meant to be run directly")