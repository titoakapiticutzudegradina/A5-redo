
class Passenger:
    def __init__(self,firstName, lastname, passport):
        self.__firstName = firstName
        self.__lastName = lastname
        self.__passport = passport

    @property
    def firstName(self):
        return self.__firstName
    @firstName.setter
    def firstName(self, firstName):
        self.__firstName = firstName

    @property
    def lastName(self):
        return self.__lastName
    @lastName.setter
    def lastName(self, lastName):
        self.__lastName = lastName

    @property
    def passport(self):
        return self.__passport
    @passport.setter
    def passport(self, passport):
        self.__passport = passport

    def __str__(self):
        return f"{self.__firstName} {self.__lastName} {self.__passport}\n"
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return self.__firstName == other.__firstName and self.__lastName == other.__lastName and self.__passport == other.__passport