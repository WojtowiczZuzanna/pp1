N = int(input("Enter the number of prime numbers you want to find: "))

prime_numbers = []
num = 2

while len(prime_numbers) < N:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)
    num += 1

print("The first", N, "prime numbers are:", prime_numbers)
