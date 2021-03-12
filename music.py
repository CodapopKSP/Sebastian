import os
from fuzzywuzzy import fuzz

itunes = os.listdir("F:\\Generic Folders\\Music - HDD\\iTunes\\iTunes Media\\Music")
playlists = []

def play_music(text):
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

def change_volume(text):
	if ('lower' or 'down' or 'reduce') in text:
		print('Reducing the volume...')
	elif ('raise' or 'up' or 'increase') in text:
		print('Increasing the volume...')