import shelve

class Save:
    def __init__(self):
        self.file = shelve.open('data')

    def add(self, name, value):
        self.file[name] = value

    def get_scores(self, name):
        try:
            return self.file[name]
        except KeyError:
            return 0
    def get_land(self, name):
        try:
            return self.file[name]
        except KeyError:
            return 0

    def get_hero(self, name):
        try:
            return self.file[name]
        except KeyError:
            return 1

    def __del__(self):
        self.file.close()
