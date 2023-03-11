"""
def fonksiyon1(name):
    print("hi "+name)

fonksiyon2 = fonksiyon1

print(fonksiyon1("taha1"))
print(fonksiyon2("taha2"))

del fonksiyon2

print(fonksiyon1("taha3"))
"""

""" fonksiyon içinde fonksiyon
def fun1(num1):
    print("fun1 calisti")
    def fun2(num1):
        print("fun2 calisti")
        print(num1+1)    
    fun2(num1)

fun1(3)
"""


""" decorator 
def my_func(func1):
    def func2(name):
        print("fonksiyondan önce calisacak")
        func1(name)
        print("fonksiyondan sonra calisacak")
    return func2

@my_func
def merhaba(name):
    print("Merhaba "+name)

merhaba("taha")
"""


