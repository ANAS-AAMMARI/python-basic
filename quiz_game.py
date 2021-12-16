print("Welcome to my math quiz!")

playing = input("Do you want to play? ")

if playing != 'yes':
    quit()

print("Okay! let's play :)")
qts = {
    "1 + 3": "4",
    "5 + 7": "12",
    "(3 +5) - 4": "4",
    "5 * 6": "30",
    "12 / 3": "4"
}
an: int = 0
for item in qts:
    answer = input(f"{item} = ")
    if answer == qts.get(item):
        print("Correct!")
        an += 1
        print(f"{item} = {qts.get(item)}")
    else:
        print("Incorrect!")

if an == len(qts):
    print(f"excellent {an} / {len(qts)}")
else:
    print(f"you need more practice {an} / {len(qts)}")
