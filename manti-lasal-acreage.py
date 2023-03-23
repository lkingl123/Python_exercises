import csv


def sum_acreage(data):
    total_acreage = 0
    for row in data:
        total_acreage += round(float(row['Acreage']),4)
    return total_acreage

def average_acreage(data):
    total_acreage = sum_acreage(data)
    average_acreage = total_acreage / len(data)
    return round(average_acreage,4)

def acreage_vals(data, area_name):
    for row in data:
        if row['Name'] == area_name:
            return round(float(row['Acreage']),4)
    return "Don't exist"

# open the csv file using csv.DictReader

with open("lasal_acreage.csv") as cvs_file:
    data = list(csv.DictReader(cvs_file))

    choice = int(input('Choose an option from 1-average, 2-sum, 3-values: '))

    if choice == 1:
        print(f"Average acreage is {average_acreage(data)}")
    elif choice == 2:
        print(f"Sum of acreage is {sum_acreage(data)}")
    elif choice == 3:
        area_name = input("Enter area name: ")
        acreage = acreage_vals(data,area_name)
        if acreage is not None:
            print(f"Area name acreage is {acreage}")
        else:
            print(f"No data found in {area_name}")

    else:
        print("Only input numbers from 1-3")


