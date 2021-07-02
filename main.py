def testmethod(test123):
    if test123 == 'Hi':
        return "Hi there"
    else:
        return 'Goodbye'

returnedfromtest = testmethod('Hi')
print(returnedfromtest)

print("Hello world", end="\n test 123")
a = True

b = "How am I here?"
print("\n", b[5:])
print(b[-5:])
print("\n", b[2], "\n")

print('Message length of b is: ' + str(len(b)) + " \t long")

print(id(a))
print(id(b))
if not a:
    print('False')
else:
    print("\n", a)

ages = [12, 13, 14, 69, 420, 'test123', ["electric", "and", "boogaloo"]]

ages[0] = "electric boogaloo"
print(ages[6][2])
print(ages)
print(len(ages))
print(ages[1:3])
ages2 = ages[:]  # do like this so when ages 2 is changed, it doesnt change the original ages2 = ages when ages2 is
# changed, ages changes with it. also can do ages2 = ages()


print('Hey whats your name?')
name = input('Please enter your name:')
print('Hi', name)

thing1 = '1'
thing2 = int(thing1)
print(type(thing2))

thing3 = 10
print(str(thing3))  # have to put str in front if not string

booltest = True
if booltest:
    print('boolean is true')
if not booltest:
    print('boolean is false')

print('Hi, where do you live?')
location = input('Please input location: ')
if location == 'Texas':
    print('Welcome to texas')
elif location == 'California' or location == 'Grand poggers':
    print('Im so sorry for you')
else:
    print('Where again?')
# elif is else if
for x in ages:
    print(x)
# x is the var that the number is put into
# ages is where the info is located
numbers = [3, 4, 5, 6]
numberlist = 0
i = 0
for x in numbers:
    numberlist = +x
    i = +1
answer = numberlist / i
print(str(answer))

for i in range(10, 100):
    print(str(i))

# 10 is included, 100 is not. Start at 10 end with 99
sum(range(10))
listofnumbers = []
for i in range(0, 10):
    listofnumbers.append(i)
print(listofnumbers)

listofnumbers2 = list(range(11))
print(listofnumbers2)

for i in listofnumbers2:
    print(i)
    if i == 5:
        break
print("What are you looking for?")
number = input()

for i in listofnumbers2:
    print(i)
    if i == number:
        print('Found ' + number)
        continue

print("What are you looking for?")
number = input()

for i in listofnumbers2:
    print(i)
    if i == number:
        print('Found ' + number)
        break
else:
    print("Not found")

while i < 10:
    print(i)
    i += 1

# to multiply it by a power do **. Example below:
nummmer = 10
print(nummmer ** 2)

inputt = input("Please say 1, 2, 3, 4")
if inputt == 1 or 2:
    print("You picked correct")
else:
    print("Ok boomer")

thing4 = "TEST"
if not thing4.islower():
    print(thing4.lower())
else:
    print(thing4)

for gg in range(11):
    print("Iteration number " + str(gg))
    for j in range(gg):
        print(j)


def greet(name="User", benice=True):
    if name == "Ryan":
        print('Ellooooo')
        return "Hey man"
    if not benice:
        return 'Hey asshole. Your name is ' + name
    else:
        return 'Hey ' + name


returned = greet("Roman")
print(greet('Roman', False))