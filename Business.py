class Applying():
    def __init__(self, name, age, role, years_of_experience):
        self.name = name
        self.age = age 
        self.role = role
        self.years_of_experience = years_of_experience
        

class Business(Applying):
    max_number_of_employess = 24
    number_of_employess = 18
    max_number_of_software_engineers = 7
    software_engineers = 5
    accountants = 3
    max_number_of_accountants = 5

    def __init__(self, name, age, role, years_of_experience, hired):
        super().__init__(name, age, role, years_of_experience)
        self.role = role
        self.years_of_experience = years_of_experience
        self.hired = hired

    def hire(self):
        if self.role == "Software Engineer" or self.role == "SOFTWARE ENGINEER" or self.role == "software engineer":
            if self.years_of_experience >= 2:
                if self.number_of_employess < self.max_number_of_employess:
                        if self.software_engineers < self.max_number_of_software_engineers:
                            print(F"{self.name} You are hired")
                            Business.number_of_employess += 1 
                            Business.software_engineers += 1 
                        else:
                            print(f"{self.name} due to the amount of engineers we have we could not offer you a role, sorry :(")
                else:
                    print(F"{self.name} You were not hired due to a limit on the amount of employees we can have, sorry :(")
            else:
                print(F"{self.name} You do not meet the minimum years of experience for this role")
        elif self.role == "Accountant" or self.role == "ACCOUNTANT" or self.role == "accountant":
            if self.years_of_experience >= 2:
                if self.number_of_employess < self.max_number_of_employess:
                    if self.accountants <= self.max_number_of_accountants:
                        print(F"{self.name} You are hired")
                        Business.number_of_employess += 1 
                        Business.accountants += 1 
                    else:
                        print(f"{self.name} due to the amount of accountants we have we could not offer you a role, sorry :(")
                else:
                    print(F"{self.name} You were not hired due to a limit on the amount of employees we can have, sorry :(")
            else:
                print(F"{self.name} You do not meet the minimum years of experience for this role")

p1 = Business("Alex", 23, "software engineer", 2, False)
p1.hire()
print(Business.number_of_employess)
p2 = Business("James", 26, "software engineer", 5, False)
p2.hire()
print(Business.number_of_employess)
p3 = Business("Maddy", 19, "SOFTWARE ENGINEER", 0, False)
p3.hire()
print(Business.number_of_employess)
p4 = Business("Jamie", 19, "Software Engineer", 4, False)
p4.hire()
print(Business.number_of_employess)
p5 =  Business("Nick", 31, "accountant", 4, False)
p5.hire()
print(Business.number_of_employess)
p6 =  Business("Adam", 26, "Accountant", 2, False)
p6.hire()
print(Business.number_of_employess)
p7 =  Business("Pepe", 42, "ACCOUNTANT", 10, False)
p7.hire()
print(Business.number_of_employess)
p8 =  Business("Luis", 19, "ACCOUNTANT", 4, False)
p8.hire()
print(Business.number_of_employess)
p9 = Business("Lexi", 28, "software engineer", 5, False)
p9.hire()
print(Business.number_of_employess)

    
