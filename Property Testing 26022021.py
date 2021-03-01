class Dog():
    def __init__(self, name, breed, size, length):
        self._name = name
        self._breed = breed
        self._size = size
        self._length = length
    def getSize(self):
        return self._size
    
    def setName(self, string):
        self._name = string

    def getName(self):
        return self._name

    def getBreed(self):
        return self._breed

    def getLength(self):
        return self._length

dog = Dog(4, 5, 'Shiba Inu', 'Joe')

print(Dog.getSize(Dog))
print(Dog.getName(Dog))
print(Dog.getBreed(Dog))
print(Dog.getLength(Dog))
Dog.setName(Dog, 'Joe Mama')
print(Dog.getName(Dog))
    
