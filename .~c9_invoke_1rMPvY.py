import stats


main():
    print()

HP = 1
TQ = 2
WEIGHT = 3

def compare_1():
    searched_stat= input("what type of stat are you looking for HP, TQ, weight?   ")

    car = input("enter choice of car\n crx, silvia, eclipse or tucson: ")
    
    if car == "crx":
        print(searched_stat," = ",str(stats.crx(searched_stat)))
    if car == "silvia":
        print(searched_stat," = ",str(stats.silvia(searched_stat)))
    if car == "ecripse":
        print(searched_stat," = ",str(stats.ecripse(searched_stat)))    
    if car == "tucson":
        print(searched_stat," = ",str(stats.silvia(searched_stat)))

def compare_2():
    car_1 = input("What is the first car you would like to compare?   ")
    car_2 = input("What is the second car you would like to compare?   ")
    
    
    if car_1 == "crx":
        column_1 = "crx"
    if car_1 == "silvia":
        column_1 = "crx"
    if car_1 == "ecripse":
        column_1 = "ecripse" 
    if car_1 == "tucson":
        column_1 = "tucson"
    if car_2 == "crx":
        column_2 = "crx"
    if car_2 == "silvia":
        column_2 = "silvia"
    if car_2 == "ecripse":
        column_2 = "ecripse" 
    if car_2 == "tucson":
        column_2 = "tucson"

    print(column_1, "    ", column_2)
    print(stats.silvia"-------------------",stats.crx)

    
main()