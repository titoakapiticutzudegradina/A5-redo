from PlaneClass import Plane
from PassengerClass import Passenger
from Logic import *
from colorama import Fore, Style

class Airport:
    def __init__(self):
        self.__planes = []

    @property
    def planes(self):
        return self.__planes
    @planes.setter
    #Adds a plane to the airport
    #Input: plane - Plane  
    #Output: -
    def addPlane(self, plane):
        for p in self.planes:
            if p.id == plane.id:
                raise Exception(Fore.RED + "Plane already exists" + Style.RESET_ALL)
        if type(plane) == Plane:
            self.planes.append(plane)
        else:
            raise ValueError(Fore.RED + "Argument must be a Plane" + Style.RESET_ALL)

    #Print all the planes in the airport
    #Input: -
    #Output: a list of planes   
    def printPlanes(self):
        for plane in self.__planes:
            print(plane.printPlane())

    #Remove a plane from the airport
    #Input: id - int
    #Output: -
    def removePlane(self, id):
        if type(id) != int:
            raise ValueError(Fore.RED + "Argument must be an integer" + Style.RESET_ALL)
        for plane in self.planes:
            if plane.id == id:
                self.planes.remove(plane)
                return
        raise Exception(Fore.RED + "Plane not found" + Style.RESET_ALL)
    
    #Update a plane from the airport
    #Input: id - int, newplane - Plane
    #Output: -
    def updatePlane(self, id, newplane):
        if type(id) != int:
            raise ValueError(Fore.RED + "Argument must be an integer" + Style.RESET_ALL)
        if type(newplane) != Plane:
            raise ValueError(Fore.RED + "Argument must be a Plane" + Style.RESET_ALL)
        for plane in self.planes:
            if plane.id == id:
                plane.name = newplane.name
                plane.company = newplane.company
                plane.seats = newplane.seats
                plane.destination = newplane.destination
                return
        raise Exception(Fore.RED + "Plane not found" + Style.RESET_ALL)
    
    def __str__(self):
        return f" {' '.join(str(plane) for plane in self.planes)}"

    #Sort the passengers in a plane by lastName
    #Input: id - int
    #Output: -
    def sortByLastName(self, id):
        if type(id) != int:
            raise ValueError(Fore.RED + "Argument must be an integer" + Style.RESET_ALL)
        for plane in self.planes:
            if plane.id == id:
                sortf(plane.passengers, key = lambda x: x.lastName)
                return
        raise Exception("Plane not found")
    
    #Sort the planes by the number of passengers
    #Input: -
    #Output: -
    def sortBySeats(self):
        sortf(self.planes, key = lambda x : x.seats)

    #Sort the planes according to the number of passengers with the first name starting with a given substring
    #Input: substring - string
    #Output: -
    def sortBySubString(self, substring):
        if type(substring) != str:
            raise ValueError(Fore.RED + "Argument must be a string" + Style.RESET_ALL)
        sortf(self.planes, key = lambda x : len(filterf(x.passengers, key = lambda y : y.firstName.startswith(substring))), reverse = True)

    #Sort the planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
    #Input: -
    #Output: -
    def sortByConcatenation(self):
        sortf(self.planes, key = lambda x : x.concatenation())

    #filter the planes that have passengers with the passport starting with thw same 3 characters
    #Input: chr - int
    #Output: a list of planes
    def filterByPassport(self, chr):
        results = self.planes
        if type(chr) != int:
            raise ValueError(Fore.RED + "Argument must be an integer" + Style.RESET_ALL)
        return filterf(results, key = lambda x : len(filterf(x.passengers, key = lambda y : str(y.passport).startswith(str(chr)))) != 0)
    
    #Filtter passengers from a given plane for which the first or last name contains a string
    #Input: id - int, string - string
    #Output: a list of passengers
    def filterByName(self, id, string):
        if type(id) != int:
            raise ValueError(Fore.RED + "Argument must be an integer" + Style.RESET_ALL)
        if type(string) != str:
            raise ValueError(Fore.RED + "Argument must be a string" + Style.RESET_ALL)
        for plane in self.planes:
            if plane.id == id:
                results = plane.passengers
        return filterf(results, key = lambda x : string in x.firstName or string in x.lastName)
    
    #Filter plane/planes where there  is a passenger with a given name
    #Input; firstName - string, lastName - string
    #Output: a list of planes
    def filterPlanes(self, firstName, lastName):
        results = self.planes
        if type(firstName) != str or type(lastName) != str:
            raise ValueError(Fore.RED + "Argument must be a string" + Style.RESET_ALL)
        return filterf(results, key = lambda x : len(filterf(x.passengers, key = lambda y : y.firstName == firstName and y.lastName == lastName)) != 0)

