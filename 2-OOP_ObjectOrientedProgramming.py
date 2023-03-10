#class

class İsim:
    pass


class Kisi:
    # class attributes
    adres= "bilgi yok"

    # costructor(yapıcı)
    def __init__(self, name="none", year="none"): # class tan türetmiş olduğumuz p1 p2 objesini temsil ediyor. 
        # obje üzerine veri aktarmaya 
        #object attributes
        self.name = name
        self.year = year

    # instance methods
    def selam(self):
        print("Merhaba" +" "+self.name)

    def yashesap(self):
        return 2023-self.year

    

#object (instance)
p1 = Kisi("taha",2000)
p2 = Kisi("ahmet",2005)
p3 = Kisi()

p1.name = "mehmet"
# print(p1.name)
# print(p2.year)
# print(p3.adres)

# p1.selam()
# print(p1.yashesap())


class Daire:
    #class object attribute
    pi = 3.14

    def __init__(self, yaricap=1):
        self.yaricap = yaricap

    # Methods
    def cevre(self):
        return 2*self.pi*self.yaricap    # classın içinden veri çekiyoruz self
    
    def alan(self):
        return self.pi*(self.yaricap**2)
    

c1 = Daire()

c1.yaricap = 5

# print(f"alan= {c1.alan()}")
# print(f"cevre= {c1.cevre()}")

"""inheritance"""

# Person => name, surname, age, eat(), Run(), Read()
# Student(Person), Teacher(Person)

class Person():
    def __init__(self):
        print("person olustu")

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        print("student olustu")
    

p2 = Student()

