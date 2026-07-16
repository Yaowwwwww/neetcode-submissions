class TimeMap:

    def __init__(self):
        self.M = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.M[(key, timestamp)] = value


    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.M:
            return self.M[(key, timestamp)]
        while timestamp > 0:
            timestamp = timestamp - 1
            if (key, timestamp) in self.M:
                return self.M[(key, timestamp)]
        return ""

