class Twitter:

    def __init__(self):
        self.follows = dict()
        self.data = dict()
        self.time_stamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.data:
            self.data[userId] = []
        self.data[userId].append((self.time_stamp, tweetId))
        self.time_stamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        result = []

        users = {userId}
        
        if userId in self.follows:
            users.update(self.follows[userId])
        
        for user in users:
            if user in self.data and self.data[user]:
                index = len(self.data[user]) - 1
                time_stamp, tweetId = self.data[user][index]
                heapq.heappush(heap, (-time_stamp, tweetId, user, index))
        
        while heap and len(result) < 10:
            time_stamp, tweetId, user, index = heapq.heappop(heap)
            result.append(tweetId)
            
            index -= 1
            if index >= 0:
                time_stamp, tweetId = self.data[user][index]
                heapq.heappush(heap, (-time_stamp, tweetId, user, index))

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)