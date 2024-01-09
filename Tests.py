from PlaneClass import Plane
from PassengerClass import Passenger
from Airpot import Airport
from colorama import Fore, Style
from os import system
from time import sleep

def test_addPassenger():
    plane = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p1 = Passenger("John", "Doe", 123)
    p2 = Passenger("Jane", "Doe", 124)
    p3 = Passenger("John", "Smith", 125)
    p4 = Passenger("Jane", "Smith", 126)
    list =[p3, p4]
    plane.addPassenger = p1
    assert plane.passengers == [p1], "Should pe Jhon Doe 123, but it is " + str(plane.passengers) + "(test_addPassenger)"
    plane.addPassenger = p2
    assert plane.passengers == [p1, p2], "Should pe Jhon Doe 123, Jane Doe 124, but it is " + str(plane.passengers) + "(test_addPassenger)" 
    plane.addPassenger = list
    assert plane.passengers == [p1, p2, p3, p4], "Should pe Jhon Doe 123, Jane Doe 124, John Smith 125, Jane Smith 126, but it is " + str(plane.passengers) + "(test_addPassenger)"

def test_removePassenger():
    plane = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p1 = Passenger("John", "Doe", 123)
    p2 = Passenger("Jane", "Doe", 124)
    p3 = Passenger("John", "Smith", 125)
    list = [p1, p2, p3]
    plane.addPassenger = list
    plane.removePassenger(123)
    assert plane.passengers == [p2, p3], "Should be Jane Doe 124, John Smith 125, but it is " + str(plane.passengers) + "(test_removePassenger)"
    plane.removePassenger(125)
    assert plane.passengers == [p2], "Should be Jane Doe 124, but it is " + str(plane.passengers) + "(test_removePassenger)"
    plane.removePassenger(124)
    assert plane.passengers == [], "Should be empty, but it is " + str(plane.passengers) + "(test_removePassenger)"

def test_updatePassenger():
    plane = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p1 = Passenger("John", "Doe", 123)
    p2 = Passenger("Jane", "Doe", 124)
    p3 = Passenger("John", "Smith", 125)
    list = [p1, p2, p3]
    plane.addPassenger = list
    plane.updatePassenger(123, Passenger("Monica", "Smith", 234))
    assert plane.passengers[0] == Passenger("Monica", "Smith", 234), "Should be Monica Smith 234, Jane Doe 124, John Smith 125, but it is " + str(plane.passengers) + "(test_updatePassenger)"
    plane.updatePassenger(234, Passenger("Caroline", "Forbes", 235))
    assert plane.passengers[0] == Passenger("Caroline", "Forbes", 235), "Should be Caroline Forbes 235, Jane Doe 124, John Smith 125, but it is " + str(plane.passengers) + "(test_updatePassenger)"
    plane.updatePassenger(235, Passenger("Monica", "Smith", 234))
    assert plane.passengers[0] == Passenger("Monica", "Smith", 234), "Should be Monica Smith 234, Jane Doe 124, John Smith 125, but it is " + str(plane.passengers) + "(test_updatePassenger)"

def test_concatenation():
    p1 = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p2 = Plane(2, "Airbus", "BlueAir", 200, "Paris")
    p3 = Plane(3, "Boeing", "WizzAir", 150, "London")
    assert p1.concatenation() == "100 Bucharest", "Should be 100 Bucharest, but it is " + p1.concatenation() + "(test_concatenation)"
    assert p2.concatenation() == "200 Paris", "Should be 200 Paris, but it is " + p2.concatenation() + "(test_concatenation)"
    assert p3.concatenation() == "150 London", "Should be 150 London, but it is " + p3.concatenation() + "(test_concatenation)"

def test_addPlane():
    p1 = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p2 = Plane(2, "Airbus", "BlueAir", 200, "Paris")
    p3 = Plane(3, "Boeing", "WizzAir", 150, "London")
    airport = Airport()
    airport.addPlane = p1
    assert airport.planes == [p1], "Should be " + str(p1) + ", but it is " + str(airport.planes) + "(test_addPlane)"
    airport.addPlane = p2
    assert airport.planes == [p1, p2], "Should be " + str(p1) + ", " + str(p2) + ", but it is " + str(airport.planes) + "(test_addPlane)"
    airport.addPlane = p3
    assert airport.planes == [p1, p2, p3], "Should be " + str(p1) + ", " + str(p2) + ", " + str(p3) + ", but it is " + str(airport.planes) + "(test_addPlane)"

def test_removePlane():
    airport = Airport()
    p1 = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p2 = Plane(2, "Airbus", "BlueAir", 200, "Paris")
    p3 = Plane(3, "Boeing", "WizzAir", 150, "London")
    airport.addPlane = p1
    airport.addPlane = p2
    airport.addPlane = p3
    airport.removePlane(1)
    assert airport.planes == [p2, p3], "Should be " + str(p2) + ", " + str(p3) + ", but it is " + str(airport.planes) + "(test_removePlane)"
    airport.removePlane(2)
    assert airport.planes == [p3], "Should be " + str(p3) + ", but it is " + str(airport.planes) + "(test_removePlane)"
    airport.removePlane(3)
    assert airport.planes == [], "Should be empty, but it is " + str(airport.planes) + "(test_removePlane)"

def test_updatePlane():
    airport = Airport()
    p1 = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    airport.addPlane = p1
    airport.updatePlane(1, Plane(1, "Airbus", "BlueAir", 200, "Paris"))
    assert airport.planes == [Plane(1, "Airbus", "BlueAir", 200, "Paris")], "Should be " + str(Plane(1, "Airbus", "BlueAir", 200, "Paris")) + ", but it is " + str(airport.planes) + "(test_updatePlane)"
    airport.updatePlane(1, Plane(1, "Boeing", "WizzAir", 150, "London"))
    assert airport.planes == [Plane(1, "Boeing", "WizzAir", 150, "London")], "Should be " + str(Plane(1, "Boeing", "WizzAir", 150, "London")) + ", but it is " + str(airport.planes) + "(test_updatePlane)"
    airport.updatePlane(1, Plane(1, "Airbus", "BlueAir", 200, "Paris"))
    assert airport.planes == [Plane(1, "Airbus", "BlueAir", 200, "Paris")], "Should be " + str(Plane(1, "Airbus", "BlueAir", 200, "Paris")) + ", but it is " + str(airport.planes) + "(test_updatePlane)"

def test_sortByLastName():
    airport = Airport() 
    p1 = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p2 = Plane(2, "Airbus", "BlueAir", 200, "Paris")
    p3 = Plane(3, "Boeing", "WizzAir", 150, "London")
    airport.addPlane = p1
    airport.addPlane = p2
    airport.addPlane = p3
    p1.addPassenger = [Passenger("John", "Doe", 123), Passenger("Jane", "Smith", 124), Passenger("John", "Smith", 125), Passenger("Jane", "Doe", 126) ]
    p2.addPassenger = [Passenger("Raluca", "Cret", 127), Passenger("Alexia", "Bora", 378), Passenger("Carla", "Lupu", 456), Passenger("Ioana", "Giurgea", 546)]
    p3.addPassenger = [Passenger("Gabi", "Hanu", 144), Passenger("Mihai", "Ghilencea", 468), Passenger("Teodora", "Catanas",189), Passenger("Diana", "Grigore", 654)]
    airport.sortByLastName(1)
    assert p1.passengers == [Passenger("John", "Doe", 123), Passenger("Jane", "Doe", 126), Passenger("John", "Smith", 125), Passenger("Jane", "Smith", 124)], "Should be " + str([Passenger("John", "Doe", 126), Passenger("Jane", "Doe", 123), Passenger("John", "Smith", 125), Passenger("Jane", "Smith", 124)]) + ", but it is " + str(p1.passengers) + "(test_sortByLastName)"
    airport.sortByLastName(2)
    assert p2.passengers == [Passenger("Alexia", "Bora", 378), Passenger("Raluca", "Cret", 127), Passenger("Ioana", "Giurgea", 546), Passenger("Carla", "Lupu", 456)], "Should be " + str([Passenger("Alexia", "Bora", 378), Passenger("Raluca", "Cret", 127), Passenger("Ioana","Giurgea",546), Passenger("Carla", "Lupu", 456)]) + ", but it is " + str(p2.passengers) + "(test_sortByLastName)"
    airport.sortByLastName(3)
    assert p3.passengers == [Passenger("Teodora", "Catanas",189), Passenger("Mihai", "Ghilencea", 468), Passenger("Diana", "Grigore", 654), Passenger("Gabi", "Hanu", 144)], "Should be " + str([Passenger("Teodora", "Catanas",189), Passenger("Mihai", "Ghilencea", 468), Passenger("Diana", "Grigore", 654), Passenger("Gabi", "Hanu", 144)]) + ", but it is " + str(p3.passengers) + "(test_sortByLastName)"

def test_sortBySeats():
    airport = Airport() 
    p1 = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p2 = Plane(2, "Airbus", "BlueAir", 200, "Paris")
    p3 = Plane(3, "Boeing", "WizzAir", 150, "London")
    airport.addPlane = p1
    airport.addPlane = p2
    airport.addPlane = p3
    airport.sortBySeats()
    assert airport.planes == [p1, p3, p2], "Should be " + str([p1, p3, p2]) + ", but it is " + str(airport.planes) + "(test_sortBySeats)"
    p4 = Plane(4, "Boeing", "WizzAir", 125, "Bucharest")
    airport.addPlane = p4
    airport.sortBySeats()
    assert airport.planes == [p1, p4, p3, p2], "Should be " + str([p1, p4, p3, p2]) + ", but it is " + str(airport.planes) + "(test_sortBySeats)"
    p5 = Plane(5, "Boeing", "WizzAir", 175, "Bucharest")
    airport.addPlane = p5
    airport.sortBySeats()
    assert airport.planes == [p1, p4, p3, p5, p2], "Should be " + str([p1, p4, p3, p5, p2]) + ", but it is " + str(airport.planes) + "(test_sortBySeats)"

def test_sortBySubString():
    airport = Airport() 
    p1 = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p2 = Plane(2, "Airbus", "BlueAir", 200, "Paris")
    p3 = Plane(3, "Boeing", "WizzAir", 150, "London")
    airport.addPlane = p1
    airport.addPlane = p2
    airport.addPlane = p3
    p1.addPassenger = [Passenger("John", "Doe", 123), Passenger("Jane", "Smith", 124), Passenger("John", "Smith", 125), Passenger("Jane", "Doe", 126) ]
    p3.addPassenger = [Passenger("Gabi", "Hanu", 144), Passenger("Mihai", "Ghilencea", 468), Passenger("Teodora", "Catanas",189), Passenger("Diana", "Grigore", 654)]
    p2.addPassenger = [Passenger("Raluca", "Cret", 127), Passenger("Alexia", "Bora", 378), Passenger("Carla", "Lupu", 456), Passenger("Ioana", "Giurgea", 546)]
    airport.sortBySubString("Jo")
    assert airport.planes == [p1,p2,p3], "Should be " + str([p1,p2,p3]) + ", but it is " + str(airport.planes) + "(test_sortBySubString)"
    airport.sortBySubString("Ra")
    assert airport.planes == [p2,p1,p3], "Should be " + str([p2,p1,p3]) + ", but it is " + str(airport.planes) + "(test_sortBySubString)"
    airport.sortBySubString("c")
    assert airport.planes == [p2, p1, p3], "Should be " + str([p2, p1, p3]) + ", but it is " + str(airport.planes) + "(test_sortBySubString)"

def test_sortByConcatenation():
    airpot = Airport()
    p1 = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p2 = Plane(2, "Airbus", "BlueAir", 200, "Paris")
    airpot.addPlane = p1
    airpot.addPlane = p2
    airpot.sortByConcatenation()
    assert airpot.planes == [p1, p2], "Should be " + str([p1, p2]) + ", but it is " + str(airpot.planes) + "(test_sortByConcatenation)"
    p3 = Plane(3, "Boeing", "WizzAir", 150, "London")
    airpot.addPlane = p3
    airpot.sortByConcatenation()
    assert airpot.planes == [p1, p3, p2], "Should be " + str([p1, p3, p2]) + ", but it is " + str(airpot.planes) + "(test_sortByConcatenation)"
    p4 = Plane(4, "Boeing", "WizzAir", 125, "Bucharest")
    airpot.addPlane = p4
    airpot.sortByConcatenation()
    assert airpot.planes == [p1, p4, p3, p2], "Should be " + str([p1, p4, p3, p2]) + ", but it is " + str(airpot.planes) + "(test_sortByConcatenation)"

def test_filterByPassport():
    airport = Airport()
    p1 = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p2 = Plane(2, "Airbus", "BlueAir", 200, "Paris")
    p3 = Plane(3, "Boeing", "WizzAir", 150, "London")
    airport.addPlane = p1
    airport.addPlane = p2
    airport.addPlane = p3
    p1.addPassenger = [Passenger("John", "Doe", 1234), Passenger("Jane", "Smith", 1235), Passenger("John", "Smith", 1236), Passenger("Jane", "Doe", 1237) ]
    p2.addPassenger = [Passenger("Raluca", "Cret", 1238), Passenger("Alexia", "Bora", 1239), Passenger("Carla", "Lupu", 1240), Passenger("Ioana", "Giurgea", 1241)]
    p3.addPassenger = [Passenger("Gabi", "Hanu", 1242), Passenger("Mihai", "Ghilencea", 1243), Passenger("Teodora", "Catanas", 1244), Passenger("Diana", "Grigore", 1245)]
    assert airport.filterByPassport(123) == [p1, p2], "Should be " + str([p1, p2]) + ", but it is " + str(airport.filterByPassport(123)) + "(test_filterByPassport)"
    assert airport.filterByPassport(124) == [p2, p3], "Should be " + str([p2, p3]) + ", but it is " + str(airport.filterByPassport(124)) + "(test_filterByPassport)"
    assert airport.filterByPassport(125) == [], "Should be empty, but it is " + str(airport.filterByPassport(125)) + "(test_filterByPassport)"

def test_filterByName():
    airport = Airport()
    p1 = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    airport.addPlane = p1
    p1.addPassenger = [Passenger("Gabi", "Hanu", 1242), Passenger("Mihai", "Ghilencea", 1243), Passenger("Teodora", "Catanas", 1244), Passenger("Diana", "Grigore", 1245)]
    assert airport.filterByName("G") == [Passenger("Gabi", "Hanu", 1242), Passenger("Diana", "Grigore", 1245)], "Should be " + str([Passenger("Gabi", "Hanu", 1242), Passenger("Diana", "Grigore", 1245)]) + ", but it is " + str(airport.filterByName("G")) + "(test_filterByName)"
    assert airport.filterByName("H") == [Passenger("Gabi", "Hanu", 1242)], "Should be " + str([Passenger("Gabi", "Hanu", 1242)]) + ", but it is " + str(airport.filterByName("H")) + "(test_filterByName)"
    assert airport.filterByName("I") == [], "Should be empty, but it is " + str(airport.filterByName("I")) + "(test_filterByName)"

def test_filterByPlanes():
    airport = Airport()
    p1 = Plane(1, "Boeing", "WizzAir", 100, "Bucharest")
    p2 = Plane(2, "Airbus", "BlueAir", 200, "Paris")
    p3 = Plane(3, "Boeing", "WizzAir", 150, "London")
    airport.addPlane = p1
    airport.addPlane = p2
    airport.addPlane = p3
    p1.addPassenger = [Passenger("John", "Doe", 1234), Passenger("Jane", "Smith", 1235), Passenger("John", "Smith", 1236), Passenger("Jane", "Doe", 1237) ]
    p2.addPassenger = [Passenger("Raluca", "Cret", 1238), Passenger("Alexia", "Bora", 1239), Passenger("Carla", "Lupu", 1240), Passenger("Ioana", "Giurgea", 1241)]
    p3.addPassenger = [Passenger("Gabi", "Hanu", 1242), Passenger("Mihai", "Ghilencea", 1243), Passenger("Teodora", "Catanas", 1244), Passenger("Diana", "Grigore", 1245)]
    assert airport.filterPlanes("John", "Doe") == [p1], "Should be " + str([p1]) + ", but it is " + str(airport.filterPlanes("John", "Doe")) + "(test_filterByPlanes)"
    assert airport.filterPlanes("Mihai", "Ghilencea") == [p3], "Should be " + str([p3]) + ", but it is " + str(airport.filterPlanes("Mihai", "Ghilencea")) + "(test_filterByPlanes)"
    assert airport.filterPlanes("Gabi", "Manu") == [], "Should be empty, but it is " + str(airport.filterPlanes("Gabi", "Manu")) + "(test_filterByPlanes)"

def testAll():
    test_addPassenger()
    test_removePassenger()
    test_updatePassenger()
    test_concatenation()
    test_addPlane()
    test_removePlane()
    test_updatePlane()
    test_sortByLastName()
    test_sortBySeats()
    test_sortBySubString()
    test_sortByConcatenation()
    test_filterByPassport()
    test_filterByName
    test_filterByPlanes()
    print(Fore.LIGHTGREEN_EX + "All tests passed" + Style.RESET_ALL)
    sleep(2)
    system("cls || clear")