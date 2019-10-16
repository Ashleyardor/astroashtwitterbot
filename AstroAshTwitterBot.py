import tweepy, time, sys
from time import sleep
from twitter_creds import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#create API object
api = tweepy.API(auth)

#read from helloworld.txt print to status
f = open('helloworld.txt', 'r')
content = f.readline()

#print conetnt from helloworld.txt every 10 minutes
def tweet():
    for content in f:
        try:
            if content !='\n':
                api.update_status(content)
                sleep(600)
            else:
                pass
        except tweepy.TweepError as err:
            print(err.reason)
            sleep(2)
tweet()

f.close()
print("I am a twitterbot")


#Print Creator information
def creator():
    user = api.get_user('ashleyardor')
    print("Name: " , user.name)
    print("Location: " , user.location)
    print("Following: " , user.friends_count)
    print("Follwers: " , user.followers_count)
creator()


#reply to mentions
def mentions():
    mention = api.mentions_timeline()
    for m in reversed(mention):
        print(str(m.id) + ' - ' + mention.full_text)
        if '#helloworld' in m .full_text.lower():
            print('found #helloworld')
            print('Responding back')
            api.update_status('@' + m.user.screen_name +
                              'Hello. I am hungry for more.' , m.id)

while True:
    mentions()
    sleep(30)
    
mentions()

