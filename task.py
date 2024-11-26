import random
people = dict()

name = ('Egor', 'Artem', 'Dima')
second_name = ('Galimov', 'Remen', 'Vinarov')
ages = (17,17,19)
group = ('ip-312k', 'ip-313k')

for i in range(0,3):
    people[i] = random.choice(name),random.choice(second_name),random.choice(ages),random.choice(group)

print(people)

#1
print('-'*10,'Name','-'*10)
for k,v in people.items():
    print(v[0])

#2
print('-'*10,'Second Name','-'*10)
for k,v in people.items():
    print(v[1])

#3
arr = []
print('-'*10,'By second name','-'*10)
for item in people.values():
    arr.append(item[1])
print(arr)
print(sorted(arr))

#4
print('-'*10,'By number group','-'*10)
print(sorted(group))
