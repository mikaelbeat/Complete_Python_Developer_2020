
import tweepy, time

auth = tweepy.OAuthHandler("OIrdiIGNB3eIvHum8o2jqeT3y", "t3fPEUaCzxBRCd8dh0ixyOttZwKYdSxX3COEWVxmQwHkTvhjgE")
auth.set_access_token("988679202609291264-KAwY4tRDP2qwO3dpgrCuKjDvrzN1Iln", "QSH5onkJJhzGnpYbdDuBU7sS4wPIa2fNirvRfrqrR7U40")

api = tweepy.API(auth)
user = api.me()

print(user.name, user.screen_name)
print(user.followers_count)

""" public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text) """

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    print(follower.name)
    if follower.name === "name":
        follower.follow()

