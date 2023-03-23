#2.1. Shapes (5 points)

shapes = ["square", "circle"]
print(shapes)

shapes.append('triangle')
print(shapes)

shapes.insert(1,'rectangle')
print(shapes)

shapes.remove('rectangle')
print(shapes)

del shapes[2]
print(shapes)


#2.2. Sorting (5 points)

ages = [27, 60, 14, 35, 3, 76]
print(ages)

ages.sort()
print(ages)

names = ['Quinn', 'John', 'Amber', 'Kim']
print(names)

names.sort()
print(names)

stats = [[3, 2], [1, 2], [1, 1], [3, 1]]
print(stats)

stats.sort()
print(stats)


#2.3. Min-Max (5 points)

numbers = [6, 10, 3, 24, 79, 24]
print(numbers)

print(min(numbers))
print(max(numbers))