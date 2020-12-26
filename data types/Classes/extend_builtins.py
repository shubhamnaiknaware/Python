class Text(str):
    def duplicate(self):
        return self + self


# we can use string methods on text as it inherits string class
text = Text("Python")
text.lower()
print(text.duplicate())


class Rlist(list):
    def append(self, object):
        print("Append called")
        super().append(object)


lis = Rlist()
lis.append(10)
print(lis)
