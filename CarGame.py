import sys


# -------------------------------------------------------------
def display_progress(miles):
    progress = 'x' * miles
    print(f"Progress: [{progress}]")


def check_command(command, started):
    if command == "Help":
        print("> Start - Starts the car")
        print("> Stop - Stops the car")
        print("> Quit - Ends the game")
    elif command == "Start":
        if started:
            print("The engine is already running!")
        else:
            print("Engine starting....get ready!")
            started = True
    elif command == "Stop":
        if not started:
            print("The engine is already stopped!")
        else:
            print("Engine stopping...")
            started = False
    elif command == "Quit":
        print("Exiting game. Thanks for playing!")
        sys.exit()
    else:
        print("Please enter a valid command.")
    return started


def drive_forward(c_started, mi_driven):
    while c_started:
        while True:
            try:
                additional_miles = int(input("How far would you like to drive? Distance: "))
                break
            except:
                print("That is not a valid distance.")
        if additional_miles == 0:
            break
        mi_driven += additional_miles
        display_progress(mi_driven)
    return mi_driven


# ----------------------------------------------------
print("Welcome to Car Game!")
print("To see a list of commands, enter 'Help'")
car_started = False
miles_driven = 0

while True:
    display_progress(miles_driven)
    user_command = input("> ").capitalize()
    car_started = check_command(user_command, car_started)
    miles_driven = drive_forward(car_started, miles_driven)
