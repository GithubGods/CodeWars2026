def prime(n):
    if n <= 1:
        return False
    else:
        isprime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                isprime = False
                break
        return isprime

if __name__ == "__main__":
    print(prime(17))