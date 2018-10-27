#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time


#Variables that contains the user credentials to access Twitter API 
access_token = "2942900654-jXXkKOlsOwDQiNAu9ihWaeuL2QDty9dRVORZUM2"
access_token_secret = "eTzQ5ymemNNKS3mZsJnbjuS87yK29GJAR5CGw7c5rnfI7"
consumer_key = "8TxyBccN42dzfTglBl19Xidtl"
consumer_secret = "AfGxBHh1MxOmmyJUuZl64hPXGiwXTpa45tIJWgijzlGVivOo4w"

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
		
		
		
		


	