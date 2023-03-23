print(18 % 4)

x = 15
y = x
x = 22

print(x)
print(y)


alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[5])



qu = "wow, welcome week!"
ty = qu.index("we")

print(ty)


if (4 + 5 == 10):
    print("TRUE")
else:
    print("FALSE")
print("TRUE")


def cyu3(x, y, z):
   if x - y > 0:
      return y -2
   else:
      z.append(y)
      return x + 3

print(cyu3(5,5,5))



if int(my_var) >= 20:
    print('too high')

elif int(my_var) >= 18 and my_var < 20:
    print('too low')
else:
    print('undefined parameter')

x = 12
x = x - 3
x = x + 5
x = x + 1
print(x)


toothpaste_list = ['Colgate','Parodontax','Sozodont']


print(toothpaste_list[-2:])


print(18 / 4)



ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)


s = "python rocks"
print(s[2] + s[-4])



print(16 - 2 * 5 // 3 + 1)




alist = [1,3,5]
blist = [2,4,6]
clist = alist + blist
print(clist.sort())


mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
yourdict = mydict
yourdict["elephant"] = 999
print(mydict["elephant"])


mydict = {"cat":12, "dog":6, "elephant":23}
print(mydict["dog"])



p = [3, 4, "Me", 3, [], "Why", 0, "Tell", 9.3]
for ch in p:
   print(ch)



tup = (7,14,21)
tup.append(28)
print(tup)



s = "python rocks"
for ch in s[3:8]:
   print("HELLO")



L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-1]))



let = "z"
let_two = "p"
c = let_two + let
m = c*5
print(m)
print("pzpzpzpzpz")



s = "python rocks"
for ch in s:
   print("HELLO")



s = "python rocks"
print(s[3:8])



qu = "wow, welcome week! Were you wanting to go?"
ty = qu.count("we")
print(ty)