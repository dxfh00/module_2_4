numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    is_prime = True
    a = 2
    while a < numbers[i]:
        if numbers[i] % a == 0:
            is_prime = False
            break
        a +=1
    if numbers[i] < 2:
        continue
    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print('Primes:', (primes))
print('Not Primes:', (not_primes))