def main():
    while True:
        start = int(input("What is the starting value? "))
        end = int(input("What is the last value? "))
        multiple = int(input("What multiple do you want to use? "))

        # Generate the list using a list comprehension
        values = [num for num in range(start, end + 1) if num % multiple == 0]

        print(values)
        print(f"There are {len(values)} numbers in this list of numbers.")

        # Ask user if they want to continue
        again = input("\nDo you want to continue? ").strip().upper()
        if again != 'Y':
            break
main()
