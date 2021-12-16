import random
import math

chaine = "1234567890azertyuiopmlkjhgfdsqwxcvbn=)@\^|{[#&(-+*AZERTYUIOPMLKJHGFDSQWXCVBN"

length = 16
rslt = ""
for i in range(16):
    # rdm = math.floor(random.random() * len(chaine))
    rdm = math.floor(random.randint(0, len(chaine) - 1))
    rslt += chaine[rdm]
print(rslt)
