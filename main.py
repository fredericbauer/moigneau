from speech_to_text import get_transcription_from_audio
from response import get_response_from_model
from stream_mic import record_audio2
from text_to_speech import text_to_speech_file
from read_audio import play_audio_sync
import threading

input = record_audio2()
question = get_transcription_from_audio(input)
response = get_response_from_model(question)
audio_response = text_to_speech_file(response)

print(question)
print(response)
play_audio_sync(audio_response)
print("terminé")


