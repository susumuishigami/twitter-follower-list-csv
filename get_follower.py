import logging

import pandas as pd
import tweepy

from credential import (
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
    API_KEY,
    BEARAR_TOKEN,
    SECRET_KEY,
)

logger = logging.getLogger(__name__)


def main():
    username = input("input username")
    api = tweepy.Client(
        bearer_token=BEARAR_TOKEN,
        consumer_key=API_KEY,
        consumer_secret=SECRET_KEY,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
        wait_on_rate_limit=True,
    )

    user = api.get_user(
        username=username,
        user_fields="description,protected,location,name,username,public_metrics,profile_image_url,verified",
        tweet_fields="id",
        expansions="pinned_tweet_id",
    )
    user_id = user.data.get("id")

    follower_list = []
    next_token = None
    while True:
        followers = api.get_users_followers(
            user_id,
            max_results=1000,
            user_fields=["public_metrics"],
            pagination_token=next_token,
        )
        for follower in followers.data:
            metrics = follower.public_metrics
            follower_list.append(
                (
                    follower.username,
                    follower.name,
                    metrics.get("followers_count"),
                    metrics.get("following_count"),
                    metrics.get("tweet_count"),
                    metrics.get("listed_count"),
                    f"https://twitter.com/{follower.username}",
                )
            )
        next_token = followers.meta.get("next_token")
        if next_token is None:
            break

    followers_df = pd.DataFrame(
        follower_list,
        columns=[
            "username",
            "name",
            "followers",
            "following",
            "tweet",
            "listed",
            "URL",
        ],
    )

    followers_df.to_csv(f"output.{user_id}.csv")


if __name__ == "__main__":
    main()
