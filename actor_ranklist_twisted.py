#!/usr/bin/env python

__author__ = "Rag Sagar.V"
__email__ = '@'.join(['ragsagar','.'.join([_ for _ in ['gmail','com']])])


from twisted.internet import reactor, threads
import re,imdb,itertools


actors_rating = {} #actors_rating['actor name'] = rank
rank = 0
count = 1
current_rank = 0
concurrent = 5
finished = itertools.count(1)
reactor.suggestThreadPoolSize(concurrent)


try:
	imdb_access = imdb.IMDb()
except imdb.IMDbError, err:
	print err
		
top_100 = imdb_access.get_top250_movies()[:100]


def populate_actors(mid):
	movie = imdb_access.get_movie(int(mid))
	#print movie
	for i in (0,1):
		actor_name =  movie['cast'][i]['name']
		if actors_rating.has_key(actor_name):
			actors_rating[actor_name] = actors_rating[actor_name] + 1
		else:
			actors_rating[actor_name] = 1
	if finished.next()==added:
		reactor.stop()
	
added = 0
for movie in top_100:
	added += 1	
	req = threads.deferToThread(populate_actors, movie.getID())

try:
	reactor.run()
except KeyboardInterrupt:
	reactor.stop()	

   
for actor in sorted(actors_rating, key=actors_rating.get, reverse=True):
	previous_rank = current_rank
	current_rank = actors_rating[actor]
	if previous_rank !=  current_rank :
		rank += count
		count = 1
	else:
		count += 1	
	print rank,actor   
    
    


