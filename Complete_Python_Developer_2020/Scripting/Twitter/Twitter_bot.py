
import tweepy, time

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

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
    if follower.name == "Sven":
        follower.follow()
        break


print("\nGet all Tweets with given argument\n")

search_iten = "Python"
number_of_tweets = 2

for tweet in tweepy.Cursor(api.search, search_iten).items(number_of_tweets):
    try:
        tweet.favorite()
        print("I liked that tweet!")
    except tweet.TweepyError as e:
        print(e.reason)
    except StopIteration:
        break
