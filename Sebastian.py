import speech_recognition as sr
import os
from fuzzywuzzy import fuzz
from music import play_music, change_volume
from conversation import introduction

r = sr.Recognizer()

def main():
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=2)
		print('Speak Now...')
		audio = r.listen(source, phrase_time_limit=10)

		try:
			text = r.recognize_google(audio)
			print(text)

			if 'Sebastian' in text:

				text = text.replace('Sebastian', '')
				text = text.lower()

				if 'introduce' in text:
					introduction(text, source)

				if 'play' in text:
					play_music(text)

				if 'volume' in text:
					change_volume(text)

		except Exception as e:
			print(e)
			main()
	main()
main()

def command(key, text, command):
	if key in text:
		text = text.replace(key, '')
		command.execute(text)
