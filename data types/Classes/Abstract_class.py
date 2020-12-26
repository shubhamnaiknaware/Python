from abc import ABC, abstractmethod
# stream class is made abstract so no object of stream class cannot be created
# read method is made abstract so the subclasses have common method


class InvalidInputError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidInputError("Stream is Running")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidInputError("Stream is already closed")
        self.opened = True

    @abstractmethod
    def read(self):
        pass


class NetworkStream(Stream):
    def read(self):
        print("Reading data from Network")


class FileStream(Stream):
    def read(self):
        print("Reading data from File")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from Memory")


m = NetworkStream()
m.read()

t = MemoryStream()
t.read()
