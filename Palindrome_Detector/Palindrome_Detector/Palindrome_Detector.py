#Palindrome Solution
def is_palindrome(s):
    s = s.lower()# Normalize the string by converting it to lowercase
    return s == s[::-1]#s[::-1] computes the reverse string using the slicing
#Return True if the Strings are equal. Return False Otherwise
def main():
    while True:
        user_input = input("Enter a string: ")
        if is_palindrome(user_input):
            print("You entered a palindrome")
        else:
            print("You did not enter a palindrome")
        continue_input = input("Do you want to continue (Y/y)? ")
        if continue_input.lower() != 'y':
            break
        print("****************************************")                                                       
if __name__ == "__main__":
    main()

