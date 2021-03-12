import os
from fuzzywuzzy import fuzz

itunes = os.listdir("F:\\Generic Folders\\Music - HDD\\iTunes\\iTunes Media\\Music")
playlists = []

def play_music(text):
	text = text.replace('play', '', 1)
	if 'tunes' in text:
		print('Playing music...')
	else:
		for pl in playlists:
			if pl in text:
				print('Playing playlist...')
				break

		for artist in itunes:
			if fuzz.partial_ratio(text,str(artist).lower()) > 90:
				text = text.replace(str(artist).lower(), '', 1)
				albums = os.listdir("F:\\Generic Folders\\Music - HDD\\iTunes\\iTunes Media\\Music\\" + artist)

				for alb in albums:
					album = str(alb).lower()
					if fuzz.partial_ratio(text, album) > 70:
						album = os.listdir("F:\\Generic Folders\\Music - HDD\\iTunes\\iTunes Media\\Music\\" + artist + '\\' + alb)
						os.startfile("F:\\Generic Folders\\Music - HDD\\iTunes\\iTunes Media\\Music\\" + artist + '\\' + alb + '\\' + alb[0])
						print('Playing ' + alb + ' by ' + artist + '...')
						break

def change_volume(text):
	if ('lower' or 'down' or 'reduce') in text:
		print('Reducing the volume...')
	elif ('raise' or 'up' or 'increase') in text:
		print('Increasing the volume...')