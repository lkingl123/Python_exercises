#1.1. Color List (2.5 points)

colors = ["red","green","blue","orange","yellow","white"]
print(colors)
print(len(colors))
print(colors[4])
print(colors[1:5])
print(colors[-3:])
print(colors * 2)


#1.2. Color List Mutation (2.5 points)

colors = ["red","green","blue","orange","yellow","white"]

colors[5] = "indigo"
print(colors)
colors[2] = colors[4]
print(colors)

colors2 = ["black","gray","cyan"]
colors = colors + colors2
colors[5] = colors
print(colors)

