# TODO data for device have to be read from DataBase
users_list_models = []


class Device:
    def __init__(self, name ="", ip ="", userList=[], address=""):
        self.name = name
        self.ip = ip
        self.userList = userList
        self.address = address


class User:
    def __init__(self, firstName="", secondName="", imageList=[]):
        self.firstName = firstName
        self.secondName = secondName
        self.imageList = imageList