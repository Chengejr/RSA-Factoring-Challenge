#!/usr/bin/python3
import sys

def factorize(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    input_file = sys.argv[1]

    with open(input_file, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    for num in numbers:
        factor1, factor2 = factorize(num)
        print(f"{num}={factor1}*{factor2}")

if __name__ == "__main__":
    main()
