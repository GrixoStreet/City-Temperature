city_temperature = {} #Dict for storing the cities and the temps.
temperatures = {} #Dict for storing 3 temps for one city


#Function to display menu
def menu_display():
    print("Operation list:-")
    print("1-Record temperature \n2-Get average temperature \n3-Get highest temperature \n4-Get lowest temperature \n5-Exit")

#Function to take user input
def get_user_choice():
    return input("Choose an operation: ")

#Function for recording city temp
def record_temperature (city , temperature):
    city_temperature[city] = temperature
    print("===================================================")
    print(f"{city} got added")

    #Getting highest temp
    counter = 1
    counter_str = ""
    global highest_temp
    highest_temp = temperatures["temp1"]
    for i in temperatures.values():
        counter_str = str(counter)
        counter += 1
        if i > highest_temp:
            highest_temp = i

    #Getting lowest temp
    counter = 1
    counter_str = ""
    global lowest_temp
    lowest_temp = temperatures["temp1"]
    for i in temperatures.values():
        counter_str = str(counter)
        counter += 1
        if i < lowest_temp:
            lowest_temp = i

#Function for getting city average temp
def get_average_temp (city):
    average_temp = (highest_temp + lowest_temp) / 2
    print("===================================================")
    print(f"The average temperature of {city} is: {average_temp}")
    

#Function to get the highest temp
def get_highest_temp(city):
    print("===================================================")
    print(f"The highest temperature of {city} is: {highest_temp}")

#Function to get the lowest
def get_lowest_temp(city):
    print("===================================================")
    print(f"The lowest temperature of {city} is: {lowest_temp}")

while True:
    print("===================================================")
    menu_display()
    userchoice = get_user_choice()
    userchoice = userchoice.lower()
    #First Choice
    if userchoice == "1" or userchoice == "record temperature":
        city_name = input("Enter a city name: ")
        for i in range(3):
            i_str = str(i)
            temp = int(input("Enter a temperature: "))
            temperatures["temp" + i_str] = temp
        record_temperature(city_name , temperatures)
    
    #Second Choice
    if userchoice == "2" or userchoice == "get average temperatrue":
        city_name = input("Enter a city name: ")
        get_average_temp(city_name)

    #Third Choice   
    if userchoice == "3" or userchoice == "get highest temperatrue":
        city_name = input("Enter a city name: ")
        get_highest_temp(city_name)

    #Fourth Choice
    if userchoice == "4" or userchoice == "get lowest temperatrue":
        city_name = input("Enter a city name: ")
        get_lowest_temp(city_name)
    
    #Fifth Choice 
    if userchoice == "5" or userchoice == "exit":
        break