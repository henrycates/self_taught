#print 3 different strings
print("String1\n") #string1
name = 'Clark Kent'
print(name)  #string2
print("\nTATATATA")

#combined question 2 and 3
#write a program that prints a message if a variable is less than 10 and different message if >= 10
#write a program that prints a message if a vaiable is <= 10, another for > 10 but <25, another > 25
count = 5
prMax = 0

for i in range(3):
    if (count < 10):
        print("\nThe if statment is true")
        print("\nThe count is ")
        print(count)
        count = 11
    elif (count > 10 & count < 25):
        print("\nCount is Greater than 10 but Less than 25, count is ")
        print( count)
    else:
        print("\nThe condition is false and count is ")
        print(count)

#divide 2 variables and print remainder
a = 10
b = 5

print("\nThe remainder of a / b is ")
print(a % b)

c = 13
d = 7
print("\nThe remainder of c / d is ")
print(c % d)

#create a program that takes 2 variables, divides them, and prints quotient

print("\nQuotient only ")
print( a // b)
print("\nQuotient only ")
print( c // d)

#write a program with a variable age assigned to int that prints different strings depending on what int age is

age = 10
for j in range(3):
    if (age < 18):
        print("You are a minor because your age is less than 18")
        age = 34
    elif (age >= 18 and age < 65):
        print("You are an adult and can work because you cannot retire yet since your age is less than 65")
        age = 68
    elif (age >= 65):
        print("These are your GOLDEN Years, hope you enjoy!")