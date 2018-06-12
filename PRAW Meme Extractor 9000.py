from time import sleep
import praw
import pyautogui as pag

# Infinite Loop
while True:
	# Creates a new instance of 'reddit'
	reddit = praw.Reddit(client_id='your client id',
                     client_secret='super secret client code', password='your password',
                     user_agent='anything can be here', username='your username')

	# Defining what subreddit we want to grab fresh memes from
	sub_reddit = reddit.subreddit("ProgrammerHumor")
	new_memes = sub_reddit.new(limit=1)
	
	# Iterates in the array thing created by new_memes
	for submission in new_memes:
		# Some posts are sticked to the top which almost never changes so let's check whether it is stickied or not
		if not submission.stickied:
			# Types the message, title of the post and the post image
			pag.typewrite("Newest /r/ProgrammerHumor Meme comming right up!")
			pag.hotkey('enter')
			pag.typewrite(submission.title)
			pag.hotkey('enter')
			pag.typewrite(submission.url)
			pag.hotkey('enter')
	
	# Wait 20 minutes before our posts count as spam
	sleep(1200)
