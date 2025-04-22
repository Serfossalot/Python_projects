import random

ROWS = 5
COLS = 5

values = [[random.randint(1, 100) for col in range(COLS)] for row in range(ROWS)]

def main():
    evens = []
    odds = []

    print(values)

    for r in range(ROWS):
        for c in range(COLS):
            if values[r][c] % 2:
                odds.append(values[r][c])
            else:
                evens.append(values[r][c])

    print("The even numbers are: ")
    print(evens)
    print("The odd numbers are: ")
    print(odds)

main()
