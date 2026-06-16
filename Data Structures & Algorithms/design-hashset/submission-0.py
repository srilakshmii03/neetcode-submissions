class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:

        index = key % self.size

        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:

        index = key % self.size

        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:

        index = key % self.size

        return key in self.buckets[index]