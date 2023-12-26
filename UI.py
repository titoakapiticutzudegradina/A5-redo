from PlaneClass import Plane
from PassengerClass import Passenger
from Airpot import Airport
from colorama import Fore, Style
from os import system
from time import sleep

airport = Airport()
airport.addPlane = Plane(1, "Plane 911", "MAG", 28, "Turnurile Gemene")
airport.planes[0].addPassenger = [Passenger( "Anisia", "Bantu", 1234), Passenger("Gabriel", "Hanu", 8454 ), Passenger("Diana", "Grigore", 6969), Passenger("Stefan", "Baldean", 6660)]
airport.addPlane = Plane(2, "Plane 356", "HGMG", 15, "New York")
airport.planes[1].addPassenger = [Passenger("Jhon", "Doe", 3876), Passenger("Jane", "Smith", 3875), Passenger("Jhon", "Smith", 7864), Passenger("Coco", "Cioco", 1234)]
airport.addPlane = Plane(3, "Private Jet", "CM", 7, "Virginia")
airport.planes[2].addPassenger = [Passenger("Aron", "Hotchner", 1234), Passenger("Derek", "Morgan", 1234),Passenger("Spancer", "Ried", 1780), Passenger("Penelope", "Garcia", 1234), Passenger("Emily", "Prentiss", 1234)]
airport.addPlane = Plane(4, "Plane 854", "ASD", 10, "Amsterdam")
airport.planes[3].addPassenger = [Passenger("Carla", "Lupu", 4444), Passenger("Raluca", "Cret", 4446), Passenger("Alexia", "Bora", 4445), Passenger("Andreea", "Bora", 4447)]
airport.addPlane = Plane(5, "Plane 123", "MAG", 10, "Amsterdam")
airport.planes[4].addPassenger = [Passenger("Tito", "Catanas", 1809), Passenger("Mihai", "Ghilencea", 1810), Passenger("Andrei", "Bora", 1811), Passenger("Andreea", "Bora", 1812)]

def menu():
    print(Fore.BLUE)
    print("0. Exit")
    print("1. Add plane")
    print("2. Remove plane")
    print("3. Update plane")
    print("4. Print pasengers from a plane")
    print("5. Add a passenger to a plane")
    print("6. Remove a passenger from a plane")
    print("7. Update a passenger from a plane")
    print("8. Sort the passengers from a plane by last name")
    print("9. Sort the planes by number of passengers")
    print("10. Sort the planes by the number of passengers with the first name starting with substring")
    print("11. Sort the planes by the number of seats and the destination")
    print("12. Search for planes with passengers that have the same 3 characters in their passport")
    print("13. Search for a passengers in a plane ")
    print("14. Search for the plane/planes of a passenger")
    print(Style.RESET_ALL)

def UI():
    print(Fore.BLUE + "Welcome to the airport manager!" + Style.RESET_ALL)
    print()
    while True:
        sleep(0.5)
        system("cls || clear")
        menu()
        print()
        airport.printPlanes()
        print()
        cmd = int(input(Fore.BLUE + "Choose an option: " + Style.RESET_ALL))
        if cmd == 0:
            system("cls || clear")
            print(Fore.CYAN + "Hope I'll never see you again!" + Style.RESET_ALL)
            break
        elif cmd ==1:
            system("cls || clear")
            print(Fore.CYAN + "You chose to add a plane" + Style.RESET_ALL)
            print()
            id = int(input("Give the id of the plane: "))
            name = input("Give the name of the plane: ")
            company = input("Give the company of the plane: ")
            seats = int(input("Give the number of seats of the plane: "))
            destination = input("Give the destination of the plane: ")
            plane = Plane(id, name, company, seats, destination)
            airport.addPlane = plane
            system("cls || clear")
            option = input(Fore.CYAN + "Do you want to add a passenger to the plane? (yes/no) " + Style.RESET_ALL)
            if option == "yes":
                print()
                firstName = input("Give the first name of the passenger: ")
                lastName = input("Give the last name of the passenger: ")
                passport = input("Give the passport of the passenger: ")
                plane.addPassenger = Passenger(firstName, lastName, passport)
                print()
                sleep(0.01)
                print(Fore.LIGHTGREEN_EX + "Passenger added successfully!" + Style.RESET_ALL)
            elif option == "no":
                print(Fore.CYAN + "Ok, no passenger added" + Style.RESET_ALL)
                continue
            print()
            sleep(0.01)
            print(Fore.LIGHTGREEN_EX + "Plane added successfully!" + Style.RESET_ALL)
        elif cmd == 2:
            system("cls || clear")
            print(Fore.CYAN + "You chose to remove a plane" + Style.RESET_ALL)
            print()
            id = int(input("Give the id of the plane you want to remove: "))
            airport.removePlane(id)
            print()
            sleep(0.01)
            print(Fore.LIGHTGREEN_EX + "Plane removed successfully!" + Style.RESET_ALL)
        elif cmd == 3:
            system("cls || clear")
            print(Fore.CYAN + "You chose to update a plane" + Style.RESET_ALL)
            print()
            id = int(input("Give the id of the plane you want to update: "))
            name = input("Give the new name of the plane: ")
            company = input("Give the new company of the plane: ")
            seats = int(input("Give the new number of seats of the plane: "))
            destination = input("Give the new destination of the plane: ")
            newplane = Plane(id, name, company, seats, destination)
            airport.updatePlane(id, newplane)
            print()
            sleep(0.01)
            print(Fore.LIGHTGREEN_EX + "Plane updated successfully!" + Style.RESET_ALL)
        elif cmd == 4:
            system("cls || clear")
            print(Fore.CYAN + "You chose to print the passengers from a plane" + Style.RESET_ALL)
            print()
            id = int(input("Give the id of the plane you want to print the passengers from: "))
            print()
            for plane in airport.planes:
                if plane.id == id:
                    print(plane)
                    break
        elif cmd == 5:
            system("cls || clear")
            print(Fore.CYAN + "You chose to add a passenger to a plane" + Style.RESET_ALL)
            print()
            id = int(input("Give the id of the plane you want to add a passenger to: "))
            firstName = input("Give the first name of the passenger: ")
            lastName = input("Give the last name of the passenger: ")
            passport = input("Give the passport of the passenger: ")
            passenger = Passenger(firstName, lastName, passport)
            for plane in airport.planes:
                if plane.id == id:
                    plane.addPassenger = passenger
                    break
            print()
            sleep(0.01)
            print(Fore.LIGHTGREEN_EX + "Passenger added successfully!" + Style.RESET_ALL)
        elif cmd == 6:
            system("cls || clear")
            print(Fore.CYAN + "You chose to remove a passenger from a plane" + Style.RESET_ALL)
            print()
            id = int(input("Give the id of the plane you want to remove a passenger from: "))
            passport = int(input("Give the passport of the passenger you want to remove: "))
            for plane in airport.planes:
                if plane.id == id:
                    plane.removePassenger(passport)
                    break
            print()
            sleep(0.01)
            print(Fore.LIGHTGREEN_EX + "Passenger removed successfully!" + Style.RESET_ALL)
        elif cmd == 7:
            system("cls || clear")
            print(Fore.CYAN + "You chose to update a passenger from a plane" + Style.RESET_ALL)
            print()
            id = int(input("Give the id of the plane you want to update a passenger from: "))
            passport = int(input("Give the passport of the passenger you want to update: "))
            firstName = input("Give the new first name of the passenger: ")
            lastName = input("Give the new last name of the passenger: ")
            newPassenger = Passenger(firstName, lastName, passport)
            for plane in airport.planes:
                if plane.id == id:
                    plane.updatePassenger(passport, newPassenger)
                    break
            print()
            sleep(0.01)
            print(Fore.LIGHTGREEN_EX + "Passenger updated successfully!" + Style.RESET_ALL)
        elif cmd == 8:
            system("cls || clear")
            print(Fore.CYAN + "You chose to sort the passengers from a plane by last name" + Style.RESET_ALL)
            print()
            id = int(input("Give the id of the plane you want to sort the passengers from: "))
            airport.sortByLastName(id)
            print()
            sleep(0.01)
            print(Fore.LIGHTGREEN_EX + "Passengers sorted successfully!" + Style.RESET_ALL)
        elif cmd == 9:
            system("cls || clear")
            print(Fore.CYAN + "You chose to sort the planes by number of passengers" + Style.RESET_ALL)
            airport.sortBySeats()
            print()
            sleep(0.01)
            print(Fore.LIGHTGREEN_EX + "Planes sorted successfully!" + Style.RESET_ALL)
        elif cmd == 10:
            system("cls || clear")
            print(Fore.CYAN + "You chose to sort the planes by the number of passengers with the first name starting with substring" + Style.RESET_ALL)
            substring = input("Give the substring: ")
            airport.sortBySubString(substring)
            print()
            sleep(0.01)
            print(Fore.LIGHTGREEN_EX + "Planes sorted successfully!" + Style.RESET_ALL)
        elif cmd == 11:
            system("cls || clear")
            print(Fore.CYAN + "You chose to sort the planes by the number of seats and the destination" + Style.RESET_ALL)
            airport.sortByConcatenation()
            print()
            sleep(0.01)
            print(Fore.LIGHTGREEN_EX + "Planes sorted successfully!" + Style.RESET_ALL)
        elif cmd == 12:
            system("cls || clear")
            print(Fore.CYAN + "You chose to search for planes with passengers that have the same 3 characters in their passport" + Style.RESET_ALL)
            print()
            chr = int(input("Give the character: "))
            print()
            sleep(0.01)
            print(airport.filterByPassport(chr))
        elif cmd == 13:
            system("cls || clear")
            print(Fore.CYAN + "You chose to search for a passengers in a plane" + Style.RESET_ALL)
            print()
            id = int(input("Give the id of the plane you want to search in: "))
            string = input("Give a string: ")
            print()
            sleep(0.01)
            print(airport.filterByName(id, string))
        elif cmd == 14:
            system("cls || clear")
            print(Fore.CYAN + "You chose to search for the plane/planes of a passenger" + Style.RESET_ALL)
            print()
            firstName = input("Give the first name of the passenger: ")
            lastName = input("Give the last name of the passenger: ")
            print()
            sleep(0.01)
            print(airport.filterPlanes(firstName, lastName))

            

        

