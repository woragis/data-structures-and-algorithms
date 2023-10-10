class Hashmap:
    def __init__(self) -> None:
        self.hashmap = {}

    def __str__(self) -> str:
        return f'Hashmap: {self.hashmap}'

    def hashFunction(self, data):
        # implement a count function to get each character value
        # and multiply first, second and last value to create a hash
        key = len(str(data))**2
        return key

    def insert(self, data):
        key = self.hashFunction(data)
        self.hashmap[key] = data

    def remove(self, data):
        key = self.hashFunction(data)
        self.hashmap[key].pop()

    def getItem(self, data):
        key = self.hashFunction(data)
        return self.hashmap[key]


newHashmap = Hashmap()
newHashmap.insert('jezreel')
newHashmap.insert('Jefferson')
newHashmap.insert('sara rebeca')
newHashmap.insert('israel')
print(newHashmap)
