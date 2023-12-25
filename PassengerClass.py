
class Passenger:
    def __init__(self,firstName, lastname, passport):
        self.__firstName = firstName
        self.__lastName = lastname
        self.__passport = passport

    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def setFirstName(self, firstName):
        self.__firstName = firstName

    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def setLastName(self, lastName):
        self.__lastNmae = lastName

    @property
    def passport(self):
        return self.__passport
    @passport.setter
    def setPassport(self, passport):
        self.__passport = passport

    def __str__(self):
        return f"{self.__firstName} {self.__lastName} {self.__passport}"
    def __repr__(self):
        return str(self)