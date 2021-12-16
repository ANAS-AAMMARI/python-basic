import random

print("""object of game is guess the number
generate by Pc start from 0 to 99
""")

if input("You want to play? ") == "yes":
    num_random = random.randint(0, 99)
    less = 0
    bigger = 99
    guesses = 0
    while True:
        # rdm: int = int(input("num = "))
        guesses += 1
        rdm = random.randint(less, bigger)
        if rdm == num_random:
            print(f"you got it the number {str(rdm)} good job :)")
            break
        elif num_random > rdm:
            # print("{0} less than number need".format(str(rdm)))
            less = rdm
        elif num_random < rdm:
            # print(f'{rdm} bigger than number need')
            bigger = rdm
        else:
            print("Incorrect")
else:
    quit()

print("you got it in ", guesses, "guesses")
