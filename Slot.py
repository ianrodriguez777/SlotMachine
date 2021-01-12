# Created by : Ian M. Rodriguez
# Slot Machine Project
# **Add Exceptions**

import random
import time

# Result list contains possible
slot_result = ["CHERRY", "ORANGE", "PLUM", "BELL", "MELON", "BAR"]

# Slot machine greets user and prompts user to enter a dollar amount
# I created an extra element to the project that keeps the slot machine running until the user runs out of money
bank = 100
print('Welcome to the slot machine! You start off with $', bank)
print('If you get to $ 0 you lose! Good luck!')
num_amount = int(input('How much money would you like to enter?: '))

# While loop allows slot machine to run until the user runs out of money
while bank > 0:
    # Random generator picks one of the six options from the slot_result list
    slotspin1 = random.choice(slot_result)
    slotspin2 = random.choice(slot_result)
    slotspin3 = random.choice(slot_result)
    # bank decrements by the amount that the user entered
    bank -= num_amount
    # Print out the results of the 3 slotspins
    print(slotspin1, slotspin2, slotspin3)
    # If all three slotspins match, the user hits the Jackpot and the amount won is added to bank
    if slotspin1 == slotspin2 and slotspin2 == slotspin3:
        num_amount *= 10
        bank += num_amount
        print('You won the Jackpot!: $', num_amount)
        print('You now have $', bank, ' in the bank')
        num_amount = int(input('\nEnter an amount: '))
    # If two slotspins match, the amount is quadrupled and added to the bank
    elif slotspin1 == slotspin2 or slotspin1 == slotspin3 or slotspin2 == slotspin3:
        num_amount *= 4
        bank += num_amount
        print('You win $', num_amount)
        print('You now have $', bank, ' in the bank')
        num_amount = int(input('\nEnter an amount: '))
    # If nothing matches, the slot machine returns the current amount in bank
    # and prompts user to enter an amount again
    else:
        # Slot machine tells the user when bank hits $0 or less, waits 3 seconds, and exits the program
        if bank <= 0:
            print('You now have $', bank, ' in the bank')
            print('Uh Oh! You lost all your money')
            time.sleep(4)
            quit()
        else:
            print('You did not win :(')
            print('You now have $', bank, ' in the bank')
            num_amount = int(input('\nEnter an amount: '))
