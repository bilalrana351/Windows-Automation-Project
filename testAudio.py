import Audio
import WhisperModel

WhisperModel.loadWhisperModel("base.en")

Audio.getTranscribedAudio()

a = input("Press Enter to continue...")

Audio.getTranscribedAudio()