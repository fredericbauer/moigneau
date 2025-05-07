import pyaudio
import wave
  
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "input.wav"

import pyaudio
import wave
import pvporcupine
import struct


def record_audio(audio, stream):
	RATE = 44100
	CHUNK = 512
	CHANNELS = 1
	FORMAT = pyaudio.paInt16
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "input.wav"
	frames = []
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		print("Recording...")
		data = stream.read(CHUNK)
		frames.append(data)
	print ("finished recording")

	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()



def record_audio2():
	ACCESS_KEY = "tSizWTJu3eeFOtRSL+4bh5yIe/XzX5D/gnFxZR0HMOmi52w5bGFnpg=="
	KEYWORD_FILE_PATH = "C:/Users/Anne-Sophie/Documents/moigneau/bonjour-mouton_fr_windows_v3_0_0.ppn"
	MODEL_FILE_PATH = "C:/Users/Anne-Sophie/Documents/moigneau/porcupine_params_fr.pv"

	porcupine = pvporcupine.create(
		access_key=ACCESS_KEY,
		keyword_paths=[KEYWORD_FILE_PATH],
		model_path=MODEL_FILE_PATH
	)
	RATE = porcupine.sample_rate
	CHUNK = porcupine.frame_length

	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	audio = pyaudio.PyAudio()

	try:
		stream = audio.open(
			format=FORMAT,
			channels=CHANNELS,
			rate=RATE,
			input=True,
			frames_per_buffer=CHUNK
		)
		print("Écoute en cours...")

		while True:
			pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
			pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

			keyword_index = porcupine.process(pcm)
			if keyword_index >= 0:
				print("Mot-clé détecté !")
				audio=pyaudio.PyAudio()
				stream = audio.open(format=FORMAT, channels=CHANNELS,
									rate=44100, input=True,
									frames_per_buffer=512)
				record_audio(audio, stream)
			
				
				print ("Enregistrement terminé !")
				return WAVE_OUTPUT_FILENAME
				break

	except KeyboardInterrupt:
		print("Interruption")
	except Exception as e:
		print(f"Erreur : {e}")
	finally:
		if stream.is_active():
			stream.stop_stream()
	stream.close()
	audio.terminate()
	porcupine.delete()
	# stop Recording