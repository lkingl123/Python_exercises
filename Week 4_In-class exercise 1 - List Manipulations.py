#4.1. Split Number List (2.5 points)


list = '10 67 123 46 20 18 36 250'
revamp = [int(x) for x in list.split()]
print(revamp)

list = '10,67,123,46,20,18,36,250'
revamp = [int(x) for x in list.split(",")]
print(revamp)

#4.2 Split Data into List

list = '90,67,87,102,77,80'
list_split = [int(x) for x in list.split(",")]
total = 0
for i in list_split:
    total += i
print(total)


#4.3 Slice Lists (2.5 points)

numbers = [1,2,3,4,5,6,7,8,9]
first_four = numbers[:4]
print(first_four)



#4.4 Slice Lists with Increment

list = ['a','b','c','d','e','f','g']
list2 = list[::2]
print(list2)