from decouple import config
from datetime import datetime
from tweepy import StreamingClient, StreamRule

# Access Keys
bearer_token = config("bearer_token")

# Class of connection with Twitter
class MyListener(StreamingClient):
    def on_data(self, data):
        time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        try:
            with open(f"collected_tweets_{ time }.txt", 'w') as f:
                items = data.decode()
                f.write(items + '\n')
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

if __name__ == "__main__":
    twitter_stream = MyListener(bearer_token)
    twitter_stream.add_rules(add=[
        StreamRule("Disney Plus"), StreamRule("Netflix"),
        StreamRule("HBO"), StreamRule("Prime Video")
    ])
    twitter_stream.filter()