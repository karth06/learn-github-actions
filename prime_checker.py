def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, int(n ** 0.5) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def main():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


if __name__ == "__main__":
    main()
