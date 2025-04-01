def main():
    try:
        with open("words.txt", "r") as file:
            content = file.read()
            words = content.split()
                        
            for word in words:
                print(word, end=' ')
                        
            print(f"\n{len(words)}")
    
    except FileNotFoundError:
        print("The file 'words.txt' was not found.")

main()

