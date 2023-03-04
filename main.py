import time

def mainLoop():
    print("Enter the number you want to count to:")
    count = input("> ")

    # check if the input is a number and if it is, convert it to an integer
    if count.isdigit():
        x = int(count)

        for i in range(1, x+1):
            print(i)
            time.sleep(1)

        # define the after() function outside of the for loop
        def after():
            print("Do You Want To Count Again? (y/n)")
            yn = input("> ")

            if yn == "y":
                mainLoop()
            elif yn == "n":
                exit()
            else:
                print(f'"{yn}" isn\'t a valid answer to y/n')
                after()

        # call the after() function outside of the for loop
        after()
    else:
        print("The input isn't a number.")
        mainLoop()

# start the program by calling the mainLoop() function
mainLoop()
