secrt_word1 = "donkey"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secrt_word1 and not(out_of_guesses):
    if guess_count < guess_limit:
      guess = input("enter the correct animal name start with 'D' : ")
      guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guesses, YOU LOSSE THE GAME! ")
else:
    print("WAOOO YOU WIN THE GAME!")
