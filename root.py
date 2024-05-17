import random
import aa, bas, eb, JC, mc, rs, kh, ka

EVERYONES_CODE = [aa, bas, eb, JC, mc, rs, kh, ka]
random.shuffle(EVERYONES_CODE)

starting_string = "Let's program in Python!"

print("Starting string:")
print(starting_string)
print()

string = starting_string

for module in EVERYONES_CODE:
    print("After running " + module.MY_NAME + "'s code:")
    string = module.mutate(string)
    print(string)
    print()