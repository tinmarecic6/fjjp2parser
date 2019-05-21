import requests
from pyparsing import *



url = "https://www.imdb.com/title/tt4508902/?ref_=fn_al_tt_1"
r = requests.get(url)
source = r.text



title = OneOrMore(Word(alphanums+":"))('title')
title_parse = '"name": "' + title + '",'

match = title_parse.scanString(source)
titles = []
for m in match:
    titles.append(m[0].title)
movie_title = ' '.join(titles[0])



genre = Word(alphanums+"-")
genres = OneOrMore(Suppress('"')+genre+Suppress('"'+Optional(',')))('genres')
genres_parse = '"genre": [' + genres + ']'

match = genres_parse.scanString(source)
genres = []
for m in match:
	genres = m[0].genres

	
	
actor_name = Group(Suppress('"name": ' + '"') + OneOrMore(Word(alphas)) + Suppress('"'))
actor_data = Suppress('"@type": ' + '"' + Word(alphanums) + '"' + ',' + '"url":' + '"' + Word(alphanums+'/') + '"' + ',') + actor_name
actors = OneOrMore(Suppress("{") + actor_data + Suppress("}" + Optional(","))) ('names')
actors_parse = '"actor": [' + actors + ']'

match = actors_parse.scanString(source)
names0 = []
for m in match:
	names0 = m[0].names
actor_names = []
for n in names0:
	actor_names.append(' '.join(n))

	
	
date = Word(nums+"-")('date')
date_parse = '"datePublished": "' + date + '",'

match = date_parse.scanString(source)
date_published = ""
for m in match:
    date_published = m[0].date
	
	

value = Word(nums+'.')('rating')
rating = '"ratingValue": ' + '"' + value + '"'
#rows = '"ratingCount": ' + '"' + Word(nums) + '"' + ',' + '"bestRating": ' + '"' + Word(nums+'.') + '"' + ',' + '"worstRating": ' + '"' + Word(nums+'.') + '"' + ','
rows = ZeroOrMore(alphanums+'@":,.\n\s\t')
rating_parse = rating

match = rating_parse.scanString(source)
movie_rating0 = []
for m in match:
	movie_rating0.append( m[0].rating )
movie_rating = movie_rating0[0]




print('"' + movie_title + '" was published ' + date_published + '. Average user rating is ' + movie_rating + '. Genres: ' + ', '.join(genres) + '. Actors: ' + ', '.join(actor_names) + '.')