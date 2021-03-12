import speech_recognition as sr

r = sr.Recognizer()


def introduction (text, source):
	text = text.replace('introduce', '', 1)
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