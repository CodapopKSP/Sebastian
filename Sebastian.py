import speech_recognition as sr
import os
from fuzzywuzzy import fuzz
from music import play_music, change_volume


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
					if 'yourself' in text:
						print("Hello, I'm Sebastian, a personal AI assistant. What's your name?")
						audio = r.listen(source)
						text = r.recognize_google(audio)
						try:
							text = r.recognize_google(audio)
							if 'my name is ' in text:
								name = text.replace('my name is ', '')
								print('Hello, ' + name + '.')
							elif "I'm " in text:
								name = text.replace("I'm ", '')
								print('Hello, ' + name + '.')
						except Exception as e:
							print(e)

				if 'play' in text:
					play_music(text)

				if 'volume' in text:
					change_volume(text)



		except Exception as e:
			print(e)
			main()
	main()
main()