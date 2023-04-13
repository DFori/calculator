print("pythin for beginners")
temperature = int(input("temperature :"))
if temperature > 30:
    print("it's a hot day")
elif temperature < 30: # (20, 30]
    print("it's a cool day have fun")
    print("be safe")

name = input("what's your name?")
print("Hello Mr/Mrs " + name)
birth_year = int(input("enter your birth year"))
age = 2023 - int(birth_year)
print(age)

print("X + Y = sum")
first = int(input("X "))
second = int(input("Y "))
sum = first + second
print("sum = " + str(sum))
