def smallest_factor(n):
    if n < 2:
        print("Invalid input. Enter a number greater than 2.")
        return None

    i = 2
    while i <= n:
        if n % i == 0:
            return i
        i += 1

    return n

def find_prime_numbers(start, end):
    if start < 0:
        print("Invalid input. Enter a non-negative number for start.")
        return
    if end < start:
        print("Invalid input. Enter an end number greater than or equal to start.")
        return

    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

choice = int(input("Choose an option: \n1. Find the smallest factor of a number \n2. Find prime numbers within a range \nEnter your choice (1 or 2): "))

if choice == 1:
    n = int(input("Enter an integer greater than or equal to 2: "))
    smallest_factor = smallest_factor(n)
    if smallest_factor != n:
        print(f"The smallest factor other than 1 for {n} is {smallest_factor}.")
    else:
        print(f"{n} is a prime number.")
elif choice == 2:
    start = int(input("Enter starting number (non-negative): "))
    end = int(input("Enter ending number (greater than or equal to start): "))
    find_prime_numbers(start, end)
else:
    print("Invalid choice. Please enter 1 or 2.")
