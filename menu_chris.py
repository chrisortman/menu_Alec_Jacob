import stats


DISPLAY_STAT_SELECT = 0
DISPLAY_CAR_SELECT = 1
DISPLAY_STAT = 2
QUIT = 99

def main():

    # State can be one of
    # () -> empty tuple, no menu selection
    # (x) -> single element tuple, we've selected the stat
    # (x,y) -> two element tuple, we've selected stat and car
    # stat is a string, car is a function in the stats module
    # QUIT -> quit signal
    next_state = ()

    should_quit = False
    while next_state != QUIT:

        # Important that all the other states are tuples
        # since we can't get in the while if next_state is QUIT
        # this is safe
        mode = len(next_state)

        if mode == DISPLAY_STAT_SELECT:
            print_stat_menu()
            choice = prompt_for_choice("Enter number of the stat:")
            next_state = handle_stat_select(choice)
        elif mode == DISPLAY_CAR_SELECT:
            print_car_menu()
            choice = prompt_for_choice("Enter number of the car:")
            next_state = handle_car_select(choice,next_state)
        elif mode == DISPLAY_STAT:
            print_stat_selection(*next_state)
            go_again = input("Do you want to go again? (Y/N):   ")
            if go_again.lower == "n":
                next_state = QUIT
            else:
                next_state = ()

def prompt_for_choice(prompt_text):
    return int(input(prompt_text))

def print_car_menu():
    print(" MENU")
    print("1) CRX")
    print("2) Eclipse")
    print("3) Silvia")
    print("4) Tucson")
    print("5) quit")

def print_stat_menu():
    print(" MENU")
    print("1) HP")
    print("2) TQ")
    print("3) weight")
    print("4) quit")

def print_stat_selection(stat, car):
    print(stat, " = ", car(stat))

# Gets the menu choice and computes
# the next state
def handle_stat_select(menu_choice):

    if menu_choice == 1:
        return ("HP",)
    elif menu_choice == 2:
        return ("TQ",)
    elif menu_choice == 3:
        return ("weight",)
    elif menu_choice == 4:
        return QUIT

def handle_car_select(menu_choice,current_state):

    if menu_choice == 1:
        return current_state + (stats.crx,)
    elif menu_choice == 2:
        return current_state + (stats.silvia,)
    elif menu_choice == 3:
        return current_state + (stats.eclipse,)
    elif menu_choice == 4:
        return current_state + (stats.tucson,)
    elif menu_choice == 5:
        return QUIT


main()

