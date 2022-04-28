class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound
        pass

    def type(self):
        return self._type
        pass

    def name(self):
        return self._name
        pass

    def sound(self):
        return self._sound
        pass
    pass

def printAnimal(o):
    if not isinstance(o, Animal):
        raise TypeError('printAnimal(): requires an animal')
        pass
    print(f'The {o.type()} is named {o.name()} and says {o.sound()}.')
    pass

def main():
    printAnimal(Animal("Human", "Junaid", "Talks"))
    pass

main()