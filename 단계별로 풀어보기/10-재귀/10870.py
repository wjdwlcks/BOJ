
def Fibonacci(num):
    if num <= 1:
        return num
    else:
        return Fibonacci(num-2) + Fibonacci(num-1)

print(Fibonacci(int(input())))