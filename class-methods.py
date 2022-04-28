class Animal:
    def __init__(self, **kwargs):
        # default values to be printed if no parameters are passed
        self._type = kwargs['type'] if 'type' in kwargs else 'Kitten'
        self._name = kwargs['type'] if 'name' in kwargs else 'Fluffy'
        self._sound = kwargs['type'] if 'sound' in kwargs else 'Meow'

    def type(self, t = None):
        if t: self._type = t
        return self._type
    
    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The "{self.type()}" is named "{self.name()}" and says "{self.sound()}"'

def main():
    # functions can be assigned to variables
    dog = Animal(type = 'Dog', name = 'Bingo', sound = 'bark')
    print(dog)
    # to change a parameter, e.g sound, name or type
    dog.sound('Meow')
    print(dog)

main()