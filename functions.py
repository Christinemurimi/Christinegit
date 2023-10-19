# Inbuilt functions
# Customs/user defined functions
greeting = "Hello there"
print (greeting)
print(greeting.upper())
print (greeting.lower())



# custom/user defined functions
def motto():
    print("Hello there this is our motto")
motto()

def add():
    x =10
    y = 20
    z = x + y
    print ("Your answer is", z)


add()



def addition (x, y, z):
    answer = x + y + z
    print ("your answer is", answer)


addition(300,480,900)
addition(534,756,7556)


def avg(name, first_number, second_number, third_number):
    answer = (first_number + second_number + third_number) / 3
    print ("Hello", name, "your average is", answer)

avg("Tine", 200, 400, 600)


def simple_interest(p, r, t):
    interest = (p * r * t) / 100
    return interest

print( simple_interest(1000, 7, 5))
print(simple_interest(454, 89,625))

