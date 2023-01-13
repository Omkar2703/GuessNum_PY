import random #We use "random" python module to generate random number
num = random.randint(1, 10)
# In line 2 num is variable that accepts any random number between 1 to 10 
player = input("Hello buddy!!, What's Your Name?\n")
#Let's Print the players name.
print("Let's Play an Game "+player+", I'll be guessing a number between 1 to 10")
print(player+ " you have to predict the number which I had Guessed")
print("You will get 5 tries")
no_guess = 0
#In while loop no_guess is less than 5 because no_guess is initialized to 0
while(no_guess<5):
    guess = int(input("Predict the guessed number: ")) #Accepting guess
    no_guess += 1
    if guess<num:
        print("Wrong, You predicted number is smaller than guessed number\n")
    if guess>num:
        print("Wrong, You predicted number is greater than guessed number\n")
    if guess==num:
        #If number guess is correct it will come out of the loop
        break
if guess == num:
    print("BINGOO!!, You guessed the number in " + str(no_guess) + " tries!\n")
else:
    print("Shitt!!, You did not guess the number, The number was " + str(num))        