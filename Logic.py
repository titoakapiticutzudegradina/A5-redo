#Sorts a list of elements by a given key
def sortf(self ,key = None, reverse = False):
    if key == None:
        key = lambda x: x
    if type(self) != list:
        raise ValueError("Argument must be a list")
    if type(reverse) != bool:
        raise ValueError("Argument must be a boolean")
    if reverse:
        for i in range(len(self)-1):
            for j in range(i+1, len(self)):
                if key(self[i]) < key(self[j]):
                    self[i], self[j] = self[j], self[i]
    else:
        for i in range(len(self)-1):
            for j in range(i+1, len(self)):
                if key(self[i]) > key(self[j]):
                    self[i], self[j] = self[j], self[i]
    return self

#Filter a list of elements by a given key
def filterf(self, key = None):
    if key == None:
        key = lambda x: x
    if type(self) != list:
        raise ValueError("Argument must be a list")
    return [x for x in self if key(x)]

if __name__ == "__main__":
    print(sortf([1,2,3,4,5], reverse = True))
    print(filterf([1,2,3,4,5], key = lambda x: x < 3))