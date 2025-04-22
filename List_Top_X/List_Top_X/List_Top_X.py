import random

def main():
    try:
        size = int(input("How many numbers? "))
        x = int(input("How many top values? "))

        if not (0 < x <= size):
            raise ValueError("x must be between 1 and size.")

        nums = [random.randint(0, 100) for _ in range(size)]
        print("\nGenerated:", nums)
        print(f"Top {x}:", sorted(nums, reverse=True)[:x])

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
