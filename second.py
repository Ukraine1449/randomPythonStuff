from collections import Counter
import testimport

# this is called a dictionary
# to add stuff do emails[key here] = value here
emails = {'Roman': 'roma.bystriakov@gmail.com', 'Boogaloo': 'boogaloo@electric.com'}
emails['Testkey'] = 'Value@gmail.com'
emailstoadd = {'element1': 'element1data', 'element2': "element2data"}
emails.update(emailstoadd)
# left is key right is value (like ID and name) id as key name as value
hashedemails = []
for i in emails:
    hashedemails.append(i.__hash__())

print(str(hashedemails))
if 'Roman' in emails:
    print(emails['Roman'])
# or
print(emails.get('Boogaloo'))

for k in emails:
    print(k)

thingy = 'Roman is my name'
dataaa = thingy.split()
for word in dataaa:
    if word in emails:
        print(emails[word])

names = {'Roman', 'Mike', 'Electric boogaloo'}
stuffff = 'Roman is a dumbass'
seeeen = set()
for word in stuffff:
    if str.lower(word) in names:
        if str.lower(word) in seeeen:
            pass
        else:
            seeeen.add(word)
print(seeeen)

foods = ['pizza', 'Custard']
backpack = ['pizza', 'Custard', 'broccoli', 'Chips', 'Cookies', 'Custard']
foods.append('Cookies')
if 'Cookies ' in foods:
    print('Cookies are there')
else:
    foods.append('Cookie')

for i in backpack:
    print(i)
    if i in foods:
        print(f'kept {i}')
        continue
    else:
        backpack.remove(i)
        print(f'removed {i}')
        continue
print(backpack)
print(backpack.count('Cookies'))

if backpack.count('Cookies') < 3:
    backpack.append('Cookies')
else:
    pass

counts = [backpack.count(item) for item in set(backpack)]
print(counts)
print(Counter(backpack))

workdays = ['Monday', 'Tuesday', 'thursday', 'friday']
workdays.insert(2, 'Wednesday')
print(workdays)
workdays.remove('friday')
print(workdays)

del workdays[0]
print(workdays)

popped = workdays.pop(1)
print(f'Just removed {popped}')

for item in backpack[:]:
    print(item)
    if item == 'Custard':
        backpack.remove(item)

workdayss = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
workdayss.sort(key=str.lower)
print(workdayss)

games = []
print('Tell me your favorite games')
while True:
    data = input()
    if str.lower(data) == 'q':
        break
    elif data == '':
        pass
    else:
        games.append(data)

print(games)

stack = []
stack.append('Plate A')
print(stack.pop())
print(stack)

que = []

que.append('data 1')
que.append('data 2')

dataaaa = 'Boogaloo, test123 yessss, NEIN NEIN NEIN'
print(dataaaa.split(','))

# Could do this:
import random

print(random.randint(1, 10))

# or this but can cause var conflicts:
from random import *

print(randint(0, 100))
print(testimport.testthingy)