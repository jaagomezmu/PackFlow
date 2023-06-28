# Fibinacci challenge

def fibonacci(n):
    if n <= 0:
        return "Invalid input. n should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    result = fibonacci(n)
    print(f"The {n}-th value of the Fibonacci sequence is: {result}")
