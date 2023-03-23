#Week 4
#Code Along lab 2

my_dict = {
    "name":"Thor",
    "age":25,
}

print(my_dict)

example_dict = {
    "animals": ["Dog","Cat","Fish"],
    "number": 1,
    "a_boolean": True,
    "another_dict": {
        "you could":"keep going",
        "like this":"forever"
    }
}

for key in example_dict:
    print(key)

for item in example_dict.items():
    print(item)

for values in example_dict.values():
    print(values)


states_dict = {
    "UT":"Utah",
    "TX":"Texas",
    "MS":"Mississippi",
    "AK":"Alaska",
    "HI":"Hawaii"
}

for item in states_dict.items():
    print(item)


for k,v in states_dict.items():
    print(k,v)

seasons = {
    "Fall": ["September","October","November"],
    "Spring": ["March, April, May"],
    "Summer": ["June, July, August"]
}

print(seasons)
winter_season = {"Winter": ["December, January, February"]}
seasons.update(winter_season)
print(seasons)

# Sets data structure
# Set uses ()
small_primes = set()
small_primes.add(2)
small_primes.add(3)
small_primes.add(5)
print(small_primes)
small_primes.add(1)
print(small_primes)
small_primes.remove(1)
print(small_primes)
print(3 in small_primes)
print(4 in small_primes)
print(4 not in small_primes)
small_primes.add(3)
print(small_primes)

#tuples
#t = ()

t = ("a","b","c","e","a")
print(t)
print(type(t))


list_a = [1,2,3]
list_b = [2,3,4]
print(set(list_a + list_b))

#t[1] = "xyz"
print(t.count("a"))


