# to hide a attribute of a class we use __ to prefix the attributes
class dictionary:
    def __init__(self):
        self.__tags = {}

    def add(self, keys):
        self.__tags[keys.lower()] = self.__tags.get(keys.lower(), 0) + 1


cloud = dictionary()

cloud.add("python")
cloud.add("python")
cloud.add("python")
# __dict__ shows all attributes and their values
print(cloud.__dict__)

print(cloud._dictionary__tags)
