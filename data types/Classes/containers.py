# here we are creating dictionary class  as  container
# and taking care of case sensitivity


class dictionary:
    def __init__(self):
        self.tags = {}

    def add(self, keys):
        self.tags[keys.lower()] = self.tags.get(keys.lower(), 0) + 1

    def __getitem__(self, keys):
        return self.tags[keys.lower()]

    def __len__(self, keys):
        return len(self.tags)

    def __setitem__(self, keys, value):
        self.tags[keys.lower()] = value

    def __iter__(self):
        return iter(self.tags)


cloud = dictionary()

cloud.add("python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)

# if key is wrong the program crashes hence __getitem__is required
print(cloud["Python"])

# 'dictionary' object does not support item assignment
# to change or set a value
cloud['python'] = 10
print(cloud["Python"])

# to iterate values in object
for i in cloud:
    print(i)
