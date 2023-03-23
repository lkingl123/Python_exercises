# Using a breakpoint and the debugger, find the problem and fix the following code:

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]

def calculate_bmi(weight, height):
    return weight / (height ** 2)

for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(weight, height)
    print("Patient's BMI is: %f" % bmi)

# The correct BMIs are 21.604938, 22.160665 and 51.903114.