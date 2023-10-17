x = 1

def echo(string):
    print(string)

while x == 1:
    print("Enter input: ")
    userInput = input()
    echo(userInput)
    if userInput == "quit":
        x = 0
