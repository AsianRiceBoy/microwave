#!/usr/bin/env python3

import praw, dotenv, os

dotenv.load_dotenv()

#create read only reddit instance
reddit = praw.Reddit(client_id = os.getenv("CLIENT_ID"), client_secret = os.getenv("CLIENT_SECRET"), user_agent = "None")

def getTopPosts(sourceSubreddit = "all", timescale = "day", amount = 10):
	"""Return a list of the specified amount of top posts over a given timescale from the subreddit."""
	#TODO implement error handling for invalid subreddits
	#TODO error handling for unspecified timescales (hour,day,week,month,year,all = valid)
	#TODO set upper limit for amount of posts retrieved
	source = reddit.subreddit(sourceSubreddit)
	topPosts = []
	for post in source.top(timescale, limit = amount):
		topPosts.append(post.permalink)
	
	return topPosts
	


