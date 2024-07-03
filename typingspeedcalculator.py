from time import time
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

while True:
    ck = input("Ready to test: yes / no: ").strip().lower()
    if ck == "yes":
        test = ("HI I Am Techpixel", "welcome to my site")
        test1 = r.choice(test)
        print("***** Typing Speed *****")
        print(test1)
        print()
        time_1 = time()
        testinput = input("Enter: ")
        time_2 = time()
        print('Speed:', speed_time(time_1, time_2, testinput), "w/sec")
        print("Error:", mistake(test1, testinput))
        print("Thank you")
    elif ck == "no":
        print(" thank you. ")
        break
    else:
        print("Wrong input. Please enter 'yes' or 'no'.")
