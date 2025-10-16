class Animal:
    def __init__(self, newName, newColour):
        self.__name = newName
        self.__colour = newColour

    def getName(self):
        return self.__name

    def getColour(self):
        return self.__colour

    def setName(self, newName):
        self.__name = newName

    def setColour(self, newColour):
        self.__colour = newColour


class Dog(Animal):
    def __init__(self, newName, newColour, newRescued):
        super().__init__(newName, newColour)
        self.__rescued = newRescued

    def getRescued(self):
        return self.__rescued

    def rescue(self):
        self.__rescued += 1



dog1 = Dog("Bob", "Brown", 2)


print(dog1.getName())
print(dog1.getColour())
print(dog1.getRescued())
dog1.rescue()
print(dog1.getRescued())  
