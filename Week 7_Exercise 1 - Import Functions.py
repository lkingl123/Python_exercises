import functions
import functions as func
import random

#1.1. Import functions: (5 points)


num = 32

print(func.ConvertFarenheittoCelsius(num))


num = 32
print(func.ConvertCelsiustoFarenheit(num))


#1.2. NullToBooleanConverter: (5 points)



result = func.NullToBooleanConverter(40)
print(result)


result = func.NullToBooleanConverter(None)
print(result)


result = func.NullToBooleanConverter("None")
print(result)



#1.3. Magic 8-Ball: (5 points)

for i in range(9+1):
    answerNumber = random.randint(1, 9)
    answer = func.getAnswer(answerNumber)

    print(f"Fortune {i+1}: {answer}")




