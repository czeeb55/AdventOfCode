

def evaluateNumber(number):
    adjacent = False
    obj = [int(x) for x in str(number)]
    for idx, digit in enumerate(obj):
        if idx == 5:
            if (int(obj[4]) <= int(obj[5]) and adjacent):
                return True
        else:
            if digit > int(obj[idx + 1]): # Decreases, automatically doesnt match
                return False
            elif digit == int(obj[idx + 1]):
                adjacent = True


# Puzzle input: range 134-564
start = 134564
end = 585159
matches = []
for i in range(start,end):
    check = evaluateNumber(i)
    if(check):
        matches.append(i)

print(len(matches))
'''
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
'''