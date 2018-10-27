#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time


#Variables that contains the user credentials to access Twitter API 
access_token = "xxxx"
access_token_secret = "xxxx"
consumer_key = "xxxx"
consumer_secret = "xxxx"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

	def on_data(self, data):
		print (data)
		return True

	def on_error(self, status):
		print (status)
		
		
if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l, tweet_mode='extended')
	
	
stream.filter(track=['Deep Learning', 'Machine Learning', 'Natural Language Processing', 'School of AI'])
		
		
		
		


	