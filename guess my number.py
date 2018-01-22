end= 100
start= 0
print("Please think of a number between 0 and 100!")
while True:
    med = int((end+start)/2)
    print("Is your secret number %d?"% (med))
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ",end='')
    x = input()
    if x == 'h':
        end = med
    elif x == 'l':
        start = med 
    elif x == 'c':
        print('Game over. Your secret number was: %d' % (med))
        break
    else:
        print("Sorry, I did not understand your input.")
