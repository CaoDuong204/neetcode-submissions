class MyHashMap:
    def __init__(self):
        self.storage = []

    def put(self, key, value):
        for pair in self.storage:
            if pair[0] == key:
                pair[1] = value
                return
        self.storage.append([key, value])

    def get(self, key):
        for pair in self.storage:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        for pair in self.storage:
            if pair[0] == key:
                self.storage.remove(pair)
                return