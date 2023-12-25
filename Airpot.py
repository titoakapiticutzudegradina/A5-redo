from PlaneClass import Plane
from PassengerClass import Passenger
from Logic import *

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
        if type(plane) == Plane:
            self.planes.append(plane)
        else:
            raise ValueError("Argument must be a Plane")

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
            raise ValueError("Argument must be an integer")
        for plane in self.planes:
            if plane.id == id:
                self.planes.remove(plane)
                return
        raise Exception("Plane not found")
    
    #Update a plane from the airport
    #Input: id - int, newplane - Plane
    #Output: -
    def updatePlane(self, id, newplane):
        if type(id) != int:
            raise ValueError("Argument must be an integer")
        if type(newplane) != Plane:
            raise ValueError("Argument must be a Plane")
        for plane in self.planes:
            if plane.id == id:
                plane.name = newplane.name
                plane.company = newplane.company
                plane.seats = newplane.seats
                plane.destination = newplane.destination
                return
        raise Exception("Plane not found")
    
    def __str__(self):
        return f" {' '.join(str(plane) for plane in self.planes)}"

    #Sort the passengers in a plane by lastName
    #Input: id - int
    #Output: -
    def sortByLastName(self, id):
        if type(id) != int:
            raise ValueError("Argument must be an integer")
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
            raise ValueError("Argument must be a string")
        sortf(self.planes, key = lambda x : len(filterf(x.passengers, key = lambda y : y.firstName.startswith(substring))), reverse = True)

    #Sort the planes according to the string obtained by concatenation of the number of passengers in the plane and the destination
    #Input: -
    #Output: -
    def sortByConcatenation(self):
        sortf(self.planes, key = lambda x : x.concatenation())
