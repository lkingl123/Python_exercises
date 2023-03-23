#functions.py

#Yes -> Y, No -> N, Male -> M,  Female -> F
#Y y N n
# Released - R, Hold - H, Deleted - D, Pending - P


def yesNoBooleanConverter(val):
    val = str(val).upper()
    if val == "Y" or val == "YES":
        return True
    else:
        return False

def booleanYesNoConverter(val):
    if val:
        return "Yes"
    else:
        return "No"


def moveQueueValueConverter(val):
    # R, H, D, P
    val = str(val).upper()
    if val == "R":
        return "Released"
    elif val == "H":
        return "Hold"
    elif val == "D":
        return "Deleted"
    elif val == "P":
        return "Pending"
    else:
        return None


def ConvertFarenheittoCelsius(num):
    celsius = (num - 32) * 5 / 9
    return celsius

def ConvertCelsiustoFarenheit(num):
    fahrenheit = num * 9 / 5 + 32
    return fahrenheit



def NullToBooleanConverter(value):
    if value == None:
        return False
    else:
        return True



def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'