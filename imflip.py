import requests
import urllib
import json

URL = "https://api.imgflip.com/get_memes"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

requests = requests.get(url= URL, headers = headers)

meme_images = requests.json()

# for i in range(len(meme_images['data']['memes'])):
# 	print(meme_images['data']['memes'][i])

memes_list = meme_images['data']['memes']

#print(memes_list)

meme_dictionary = {}

for i in range(len(memes_list)):
	mid = memes_list[i]['id']
	url = memes_list[i]['url']
	name = memes_list[i]['name']
	meme_dictionary[mid] = {'url' : url, 'name' : name}

#print(memes_list)