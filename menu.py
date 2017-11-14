import stats





searched_stat = 0
car = 0
def main():
    global searched_stat
    global car
    
    valid_search = False
    while not valid_search:
        while searched_stat != "quit":
            
            print_stat_menu()
            try:
                searched_stat = handle_stat_select()
                if searched_stat == "quit":
                    quit()
                valid_search = True
                while car != "quit":
                    print_car_menu()
                    car = handle_car_select()
                    print("Do you want to continue?")
                searched_stat = input("If You are done type\"quit\".\nIf you are not done press enter.")
                go_again = input("Do you want to go again? (Y/N):   ")
                if go_again == "N":
                    searched_stat = "quit" 
                
                
            except NameError:
                print("your input was inviable")




    
    
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


def handle_stat_select():
        
    valid_number_1 = False
    while not valid_number_1:
        try:
            searched_stat= int(input("Enter number of stat:   "))
            if searched_stat == 1:
                searched_stat = "HP"
            elif searched_stat == 2:
                searched_stat = "TQ"
            elif searched_stat == 3:
                searched_stat = "weight" 
            elif searched_stat == 4:
                searched_stat = "quit"
            print("You chose, ",searched_stat)
            valid_number_1 = True
            return searched_stat
        except NameError:
            print("searched_stat wasnt allowed as a value")
        except ValueError:
            print("You fool thats not even a number")
            
        
        
    

def handle_car_select():
    
    
    valid_number_2 = False
    while not valid_number_2:
        try:  
            car = int(input("enter number of car:   "))        
            
            if car == 1:
                print(searched_stat," = ",str(stats.crx(searched_stat)))
            if car == 2:
                print(searched_stat," = ",str(stats.silvia(searched_stat)))
            if car == 3:
                print(searched_stat," = ",str(stats.eclipse(searched_stat)))    
            if car == 4:
                print(searched_stat," = ",str(stats.silvia(searched_stat)))
            if car == 5:
                car = "quit"
                return car
            print("You pressed, ",car)
            valid_number_2 = True
            return car
        except NameError:
            print("Your car choice was not allowed")
        except ValueError:
            print("You fool that was not even a number.")




main()


