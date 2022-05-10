from tweepy.auth import OAuthHandler
import tweepy 
import collections
collections.Callable = collections.abc.Callable

def send_to_twitter(msg):
    CONSUMER_KEY = '0xMeLsokcb7IRR30X2xfJmiIs'
    CONSUMER_SECRET = 'bWVnKTzoXZKL5Fo3uFEyUvB3u9mpqwD1Lgg5kLEJFg0T0qKl9z'
    ACESS_KEY = '1506501938141351938-vY8WcDmrCjMvUWEUd62x425WF4ULcr'
    ACESS_SECRET = '1P22xpBvdpBwLn0y6XtV0u1i8Fm6sQ0eQXiJTmjTUJL9z'
    auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(ACESS_KEY,ACESS_SECRET)
    
    api = tweepy.API(auth)
    api.update_status(msg)