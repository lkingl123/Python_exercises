# Exercise #1: (10 points)

stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12,
    'map fragments': 3
}

total = 0
print(f"Inventory:")
for keys, values in stuff.items():
    total += values
    print(f"{values} {keys} ")

print(f"Total number of items : {total}")



#Exercise #2: (10 points)


characters = ["Thor", "Thanos", "Black Panther", "Iron Man", "Hulk", "Batman", "Captain America"]

string = ', '.join(characters[:-1]) + ' and ' + characters[-1] + '.'

print(string)



#Exercise #3: (10 points)

definitions = {'dict': 'stores a key/value pair',
               'list': 'stores a value at each index',
               'map': 'see dict',
               'set': 'stores unordered unique elements',
               'exit': 'exit the program'}

while True:
    term = input("Enter a term, 'dict','list','map','set'('exit' to exit): ")
    found = False
    for key, value in definitions.items():
        if term == key:
            print(f"{key}: {value}")
            found = True
            break
    if not found:
        print(f"{term} not found.")
    if term == 'exit':
        break




#Exercise #4: (2 points)

print(set("Mississippi"))



#Exercise #5: (2 points)


list1 = [1, 2, [3, 4, "hello"]]

list1[2][2] = "goodbye"

print(list1)


#Exercise #6: (3 points)

#6a.

d = {'simple_key':"hello"}
value = d["simple_key"]
print(value)


#6b.

d = {"k1":{"k2":"hello"}}
value = d["k1"]["k2"]
print(value)
