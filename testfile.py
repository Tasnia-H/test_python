num = int(input("Enter number: "))
count = 0
while (num > 0):
    num = num // 10
    count += 1
div = 10 ** (count - 1)
while (num > 0):
    digit = num // div
    num %= div
    div //= 10
    if (num < 10):
        print(digit, end = " ")
    else:
       print(digit, end = ", ")
