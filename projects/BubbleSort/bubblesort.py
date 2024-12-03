num_list = []

for c in range(0, 5):
    num = float(input('Type a number: '))
    num_list.append(num)

for c in range(0, len(num_list)):
    for c in range (0, len(num_list) - 1):
        if num_list[c] > num_list[c+1]:
            num_list[c], num_list[c+1] = num_list[c+1], num_list[c]

#Function to remove the post dot part of float numbers only when its just zero like: 1.0
def format_float(num):
    return str(num).rstrip('.0') if num % 1 == 0 else str(num)

for number in num_list:
    print(format_float(number), end=', ' if number != num_list[len(num_list) - 1] else '.')
    