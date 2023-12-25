from PassengerClass import Passenger

#Plane class has the information about a plane(id, name, company, seats, destination, passengers)
class Plane:
    def __init__(self, id, name, company, seats, destination):
        self.__id = id
        self.__name = name
        self.__company = company
        self.__seats = seats
        self.__destination = destination
        self.__passengers = []

    @property
    def id (self):
        return self.__id
    @id.setter
    def setId(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def setName(self, name):
        self.__name = name

    @property
    def company(self):
        return self.__company
    @company.setter
    def setCompany(self, company):
        self.__company = company

    @property
    def seats(self):
        return self.__seats
    @seats.setter
    def setSeats(self, seats):
        self.__seats = seats

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def setDestination(self, destination):
        self.__destination = destination

    @property
    def passengers(self):
        return self.__passengers
    @passengers.setter
    #Adds a passenger/multiple passengers to the plane
    def addPassenger(self, passenger):
        if type(passenger) == Passenger:
            if len(self.__passengers) < self.__seats:
                self.__passengers.append(passenger)
            else:
                raise Exception("Plane is full")
        if type(passenger) == list:
            for p in passenger:
                if len(self.__passengers) + len(passenger) < self.__seats:
                    self.__passengers.append(p)
                else:
                    raise Exception("Plane is full")

    def printPlane(self):
        return f"Id: {self.__id} Name: {self.__name} Company: {self.__company} Seats: {self.__seats} Destination: {self.__destination}"

    def __str__(self):
        whatever = ' '.join([str(passenger) for passenger in self.__passengers])
        return f"Id: {self.__id} Name: {self.__name} Company: {self.__company} Seats: {self.__seats} Destination: {self.__destination}\nPassenger:\n {whatever}"
    def __repr__(self):
        return str(self)
    
    #Removes a passenger from the plane(by passport)
    def removePassenger(self, passport):
        if type(passport) != int:
            raise ValueError("Argument must be an integer")
        for passenger in self.__passengers:
            if passenger.passport == passport:
                self.__passengers.remove(passenger)
                return
        raise Exception("Passenger not found")

    #Updates a passenger in the plane(by passport)
    def updatePassenger(self, passport, newPassenger):
        if type(passport) != int:
            raise ValueError("Argument must be an integer")
        if type(newPassenger) != Passenger:
            raise ValueError("Argument must be a Passenger")
        for passenger in self.__passengers:
            if passenger.passport == passport:
                passenger.fisrtName = newPassenger.firstName
                passenger.lastName = newPassenger.lastName
                passenger.passport = newPassenger.passport
                return
        raise Exception("Passenger not found")
    

    
    

    