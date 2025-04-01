import random

def main():
    sets = int(input("How many lottery numbers do you want to generate? "))

    for _ in range(sets):
        numbers = [random.randint(0, 9) for _ in range(7)]
        print(', '.join(str(num) for num in numbers))

# Run the program
main()

