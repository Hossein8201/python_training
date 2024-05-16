# https://quera.org/problemset/16396?tab=description
class Foo:
    def __init__(self):
        self.value = 0

    @property
    def x(self):
        return self.value

    @x.setter
    def x(self, new_value):
        self.value = new_value
        self.on_change()

    def on_change(self):
        if(self.value >= 0):
            self.value %= 100
        else:
            self.value = -1

