#!/usr/bin/env python

__author__ = "Rag Sagar.V"
__email__ = '@'.join(['ragsagar','.'.join([_ for _ in ['gmail','com']])])


from mechanize import Browser
import re,imdb

actors_rating = {} #actors_rating['actor name'] = rank
rank = 0
current_rank = 0
count = 1
url = "http://www.imdb.com/chart/top"
br = Browser()
br.open(url)
imdb_access = imdb.IMDb()

links = br.links(url_regex=re.compile(r"/title/tt*"))
for counter,link in enumerate(links):
    if counter == 20:
        break
    mid = int(link.url.split('/')[2][2:])
    movie = imdb_access.get_movie(mid)
    #print counter+1,movie
    for i in (0,1):
        actor_name =  movie['cast'][i]['name']
        if actors_rating.has_key(actor_name):
            actors_rating[actor_name] = actors_rating[actor_name] + 1
        else:
            actors_rating[actor_name] = 1

   
for actor in sorted(actors_rating, key=actors_rating.get, reverse=True):
	previous_rank = current_rank
	current_rank = actors_rating[actor]
	if previous_rank !=  current_rank :
		rank += count
		count = 1
	else:
		count += 1	
	print rank,actor       
    

