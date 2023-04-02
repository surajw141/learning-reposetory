def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num-1) + fib(num-2)

number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Invalid input.")
else:
    for i in range(number):
        print(fib(i))
