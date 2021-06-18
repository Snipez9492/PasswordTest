import webbrowser

run = True

name = input("State your name: ")
password = "Waleibk92"
attempt = 3

while run:
    if not name:
        retry = input("Please enter a name: ")
        name = retry
        continue
    else:
        print("Next to meet you", name)

    access = input("What is the password: ")

    if access == password:
        print("Access is granted, welcome", name)
        webbrowser.open('https://www.nba.com/')
        run = False
    else:
        print("Please try again.")
        attempt = attempt - 1

        if attempt == 0:
            print("You have exceeded the number of attempt. Goodbye!")
            break
