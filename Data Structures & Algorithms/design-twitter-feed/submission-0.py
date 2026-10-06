from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.time = 0
        self.user_tweets = defaultdict(list)    # userId -> list of (time, tweetId)
        self.following = defaultdict(set)       # followerId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1  # Decrement for min-heap (most negative = most recent)
        self.user_tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        # Ensure user follows themselves in the feed
        followees = self.following[userId] | {userId}

        # Initialize the heap with the newest tweet from each followee
        for followee_id in followees:
            tweets = self.user_tweets[followee_id]
            if tweets:
                last_idx = len(tweets) - 1
                t, tweet_id = tweets[last_idx]
                # Store (time, tweet_id, followee_id, next_idx_to_check)
                max_heap.append((t, tweet_id, followee_id, last_idx - 1))

        heapq.heapify(max_heap)
        feed = []

        # Pull up to 10 most recent tweets overall
        while max_heap and len(feed) < 10:
            t, tweet_id, followee_id, next_idx = heapq.heappop(max_heap)
            feed.append(tweet_id)

            if next_idx >= 0:
                next_t, next_tweet_id = self.user_tweets[followee_id][next_idx]
                heapq.heappush(max_heap, (next_t, next_tweet_id, followee_id, next_idx - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)