# Missionaries and Cannibals
bankA = ['c', 'c', 'c', 'm', 'm', 'm']
bankB = []
count = 0
boat='a'
print('Missionaries and Cannibals problem \nInitially bankA has all three missionaries and cannibals.bankB is empty. ')
print('bankA: ' + str(bankA))
print('bankB: ' + str(bankB))
print('Goal state that must be obtained:\nAll three missionaries and cannibals must be brought to bankB \nAt a time'
      'atleast 1 and atmost 2 memebers can be moved from one bank to another.')
print('Game stops when there are more number of cannibals than the missionaries at the given time. ')

def status():
    print('bankA: ' + str(bankA), end=' ')
    print('bankB: ' + str(bankB))

while (True):
    print("Choose any one of the following options")
    print("1.Move 2 missionaries from bankA to bankB")
    print("2.Move 2 missionaries from bankB to bankA")
    print("3.Move 2 cannibals from bankA to bankB")
    print("4.Move 2 cannibals from bankB to bankA")
    print("5.Move 1 missionary and 1 cannibal from bankA to bankB")
    print("6.Move 1 missionary and 1 cannibal from bankB to bankA")
    print("7.Move 1 missionary from bankA to bankB")
    print("8.Move 1 missionary from bankB to bankA")
    print("9.Move 1 cannibal from bankA to bankB")
    print("10.Move 1 cannibal from bankB to bankA")
    print("11.Reset/Start again")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if (bankA.count('m') < 2 ):
            print('Please select another option. Less than 2 missionaries on bankA')
        elif  boat=='a':
            boat='b'
            for i in range(2):
                bankB.append('m')
            for j in range(2):
                bankA.remove('m')
            count = count + 1
            status()
        else:
            print("Boat not present on bank")

    elif choice == 2:
        if (bankB.count('m') < 2  ):
            print('Please select another option. Less than 2 missionaries on bankB')
        elif boat=='b':
            boat = 'a'
            for i in range(2):
                bankA.append('m')
            for j in range(2):
                bankB.remove('m')
            count = count + 1
            status()
        else:
            print("Boat not present on bank")


    elif choice == 3:
        if (bankA.count('c') < 2 ):
            print('Please select another option. Less than 2 cannibals on bankA')
        elif boat=='a':
            boat = 'b'
            for i in range(2):
                bankB.append('c')
            for j in range(2):
                bankA.remove('c')
            count = count + 1
            status()
        else:
            print("Boat not present on bank")


    elif choice == 4:
        if (bankB.count('c') < 2):
            print('Please select another option. Less than 2 cannibals on bankB')
        elif  boat=='b':
            boat = 'a'
            for i in range(2):
                bankA.append('c')
            for j in range(2):
                bankB.remove('c')
            count = count + 1
            status()
        else:
             print("Boat not present on bank")

    elif choice == 5:
        if (bankA.count('c') < 1 ):
            print('Please select another option. No cannibal on bankA')
        elif (bankA.count('m') < 1 ):
            print('Please select another option. No missionary on bankA')
        elif boat=='a':
            boat = 'b'
            bankB.append('m')
            bankA.remove('m')
            bankB.append('c')
            bankA.remove('c')
            count = count + 1
            status()
        else:
            print("Boat not present on bank")

    elif choice == 6:
        if (bankB.count('c') < 1 ):
            print('Please select another option. No cannibal on bankB')
        elif (bankB.count('m') < 1 and boat=='b'):
            print('Please select another option. No missionary on bankB')
        elif boat=='b':
            boat = 'a'
            bankA.append('m')
            bankB.remove('m')
            bankA.append('c')
            bankB.remove('c')
            count = count + 1
            status()
        else:
            print("Boat not present on bank")

    elif choice == 7:
        if (bankA.count('m') < 1  ):
            print('Please select another option. No missionary on bankA')
        elif boat=='a':
            boat = 'b'
            bankB.append('m')
            bankA.remove('m')
            count = count + 1
            status()
        else:
            print("Boat not present on bank")

    elif choice == 8:
        if (bankB.count('m') < 1 ):
            print('Please select another option. No missionary on bankB')
        elif  boat=='b':
            boat = 'a'
            bankA.append('m')
            bankB.remove('m')
            count = count + 1
            status()
        else:
            print("Boat not present on bank")

    elif choice == 9:
        if (bankA.count('c') < 1 ):
            print('Please select another option. No cannibal on bankA')
        elif  boat=='a':
            boat = 'b'
            bankB.append('c')
            bankA.remove('c')
            count = count + 1
            status()
        else:
            print("Boat not present on bank")

    elif choice == 10:
        if (bankB.count('c') < 1 ):
            print('Please select another option. No cannibal on bankB')
        elif  boat=='b':
            boat = 'a'
            bankA.append('c')
            bankB.remove('c')
            count = count + 1
            status()
        else:
            print("Boat not present on bank")

    elif choice == 11:
        bankA = ['c', 'c', 'c', 'm', 'm', 'm']
        bankB = []
        count = 0
        status()
    else:
        print('Please select correct option:')

    # Game over
    if (((bankA.count('c') > bankA.count('m')) and bankA.count('m') > 0) or (
            (bankB.count('c') > bankB.count('m')) and bankB.count('m') > 0)):
        print('Game over! The missionary was eaten by the cannibal.')
        ans = input('Try again?(y/n) ')
        if (ans == ('y' or 'Y')):
            bankA = ['c', 'c', 'c', 'm', 'm', 'm']
            bankB = []
            count = 0
            boat='a'
            status()
        else:
            break

    # stopping condition
    if (bankB.count('m') == 3 and bankB.count('c') == 3 and bankA.count('m') == 0 and bankA.count('c') == 0):
        print('Solution obtained in ' + str(count) + ' steps')
        print('bankB: ' + str(bankB))
        print('bankA: ' + str(bankA))
        break
