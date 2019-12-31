#!/usr/bin/env python3

import praw, prawcore, dotenv, os

dotenv.load_dotenv()

#create read only reddit instance
reddit = praw.Reddit(client_id = os.getenv("CLIENT_ID"), client_secret = os.getenv("CLIENT_SECRET"), user_agent = "None")

def getTopPosts(sourceSubreddit = "all", timescale = "day", amount = 10):
	"""Return a list of the specified amount of top posts over a given timescale from the subreddit."""
	if not(subredditExists(sourceSubreddit)): return "Subreddit invalid" 
	if not(timescale in ["hour", "day", "week", "month", "year", "all"]): return "Timescale invalid" 
	if (type(amount) != int or amount > 50 or amount < 0): return "Amount invalid (limit 50)" 

	source = reddit.subreddit(sourceSubreddit)
	
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

