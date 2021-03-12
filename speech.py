import speech_recognition as sr
import os
from fuzzywuzzy import fuzz

itunes = os.listdir("F:\\Generic Folders\\Music - HDD\\iTunes\\iTunes Media\\Music")

r = sr.Recognizer()
playlists = []

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
					if 'tunes' in text:
						print('Playing music...')
					else:
						for pl in playlists:
							if pl in text:
								print('Playing playlist...')
								break
						for a in itunes:
							if fuzz.partial_ratio(text,str(a).lower()) > 90:
								text = text.replace(str(a).lower(), '')
							#if str(a) in text:
								albums = os.listdir("F:\\Generic Folders\\Music - HDD\\iTunes\\iTunes Media\\Music\\" + a)
								print(albums)
								for al in albums:
									album = str(al).lower()

									if fuzz.partial_ratio(text, album) > 70:
										album = os.listdir("F:\\Generic Folders\\Music - HDD\\iTunes\\iTunes Media\\Music\\" + a + '\\' + al)
										os.startfile("F:\\Generic Folders\\Music - HDD\\iTunes\\iTunes Media\\Music\\" + a + '\\' + al + '\\' + album[0])
										print('Playing ' + al + ' by ' + a + '...')
										break




				if 'volume' in text:
					if ('lower' or 'down' or 'reduce') in text:
						print('Reducing the volume...')
					elif ('raise' or 'up' or 'increase') in text:
						print('Increasing the volume...')

				











		except Exception as e:
			print(e)
			main()
	main()
main()