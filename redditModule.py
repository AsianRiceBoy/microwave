#!/usr/bin/env python3

import praw, prawcore, dotenv, os

dotenv.load_dotenv()

#create read only reddit instance
reddit = praw.Reddit(client_id = os.getenv("CLIENT_ID"), client_secret = os.getenv("CLIENT_SECRET"), user_agent = "None")

def getTopPosts(sourceSubreddit = "all", timescale = "day", amount = 10):
	"""Return a list of the specified amount of top posts over a given timescale from the subreddit."""
	#TODO error handling for unspecified timescales (hour,day,week,month,year,all = valid)
	#TODO set upper limit for amount of posts retrieved
	source = None
	if subredditExists(sourceSubreddit):
		source = reddit.subreddit(sourceSubreddit)
	else:
		return ("Subreddit invalid")

	topPosts = []
	for post in source.top(timescale, limit = amount):
		topPosts.append(post.permalink)
	
	return topPosts

def subredditExists(sourceSubreddit):
	"""Checks if a given subreddit exists"""
	exists = True
	try:
		reddit.subreddits.search_by_name(sourceSubreddit, exact = True)
	except prawcore.exceptions.NotFound:
		exists = False

	return exists





