
class HashTable:
    def __init__(self, size=5):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash(self, key):
        return sum(
            [int(ch)for ch in key if ch.isdigit()]) % len(self.buckets)

    def get_bucket(self, key):
        bucket = self.buckets[self.hash(key)]
        return bucket

    def get_entry(self, key):
        bucket = self.get_bucket(key)
        if bucket is not None:
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    return bucket[i]

        return None

    def put(self, key, value):
        bucket = self.get_bucket(key)
        if bucket is not None:
            for i, (k, v) in enumerate(bucket):
                if k == key:
                    bucket[i] = [key, value]
                    return
        bucket.append((key, value))

    def get(self, key):
        bucket = self.get_bucket(key)
        return [value for k, value in bucket if k == key and bucket is not None]

    def remove(self, key):
        entry = self.get_entry(key)
        if entry is None:
            print('Key Not Found!')
        else:
            self.get_bucket(key).remove(entry)

    def contains(self, key, ll):
        index = self.hash(key)
        return ll[index] == key

    def print(self):
        for index, bucket in enumerate(self.buckets):
            print(f"Bucket {index}: {bucket}")

