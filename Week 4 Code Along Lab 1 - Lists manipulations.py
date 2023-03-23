#Week 4
#Code along 1

my_numbers = "10 20 30 40 50 60"
num_list = my_numbers.split()
print(num_list)
print(my_numbers)
print(num_list[1])

int_list = [int(x) for x in my_numbers.split()]
print(int_list)


my_csv = "Harry Porter, Darth Vader, Garfield, Ron"
str_list = my_csv.split(",")
print(str_list)

my_time = "10:05:45,09:43:32,07:30:25"
time_list = my_time.split(",")
for item in time_list:
    time = item.split(":")
    print(time)


time = "08:49:34"
hrs, mins, secs = time.split(":")
print(hrs, mins ,secs)


from_csv = "John, 1234 Evergreen Terrace, 801-555-1212,,,email"
name, address, phone = from_csv.split(",")
print(name, phone, address) #pretending this saving to a database