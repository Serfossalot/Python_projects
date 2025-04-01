def main():
    while True:
        # Step 1 & 2
        length = int(input("How many items do you want to be in the list? "))
        items = []

        # Step 3
        for _ in range(length):
            item = input("Input an item: ")
            items.append(item)

        # Step 4
        print(items)

        # Step 5 & 6
        to_remove = input("What item do you want to delete? ")

        # Step 7
        items = [x for x in items if x != to_remove]

        # Step 8
        print(items)

        # Step 9
        again = input("\nDo you want to continue? ").strip().lower()
        if again == 'n':
            break

# Run the program
main()

