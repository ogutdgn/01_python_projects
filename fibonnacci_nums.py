num1 = 1
num2 = 1
list_of_fibonacci = [1,1]
while True:
    list_of_fibonacci.append(list_of_fibonacci[-1] + list_of_fibonacci[-2])

    if list_of_fibonacci[-1] == 55:
        print(list_of_fibonacci)
        break

    