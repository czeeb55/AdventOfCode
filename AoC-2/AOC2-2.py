# https://adventofcode.com/2019/day/2
# Part 2 challenge: find combination of values in position 1("noun") and 2("verb") that create the desired output of 19690720.
# Nouns and verbs are  0 <= X <= 99
def processCode(intCode):
    index = 0 # start at first digit
    while intCode[index] != 99: # 99 is the stop code
        slice = intCode[index:index+4] # Grab the current set of values we're working with
        if(intCode[index] == 1):
            intCode[slice[3]] = intCode[slice[1]] + intCode[slice[2]]
            index += 4

        elif(slice[0] == 2):
            intCode[slice[3]] =  intCode[slice[1]] * intCode[slice[2]]
            index += 4
    return(intCode[0]) # First digit is the only requested output


# Iterate over all possible combinations, reset input back to correct value, print out noun/verb combination
for noun in range(100):
    for verb in range(100):
        input = [1,noun,verb,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,9,23,27,1,5,27,31,1,5,31,35,1,35,13,39,1,39,9,43,1,5,43,47,1,47,6,51,1,51,13,55,1,55,9,59,1,59,13,63,2,63,13,67,1,67,10,71,1,71,6,75,2,10,75,79,2,10,79,83,1,5,83,87,2,6,87,91,1,91,6,95,1,95,13,99,2,99,13,103,1,103,9,107,1,10,107,111,2,111,13,115,1,10,115,119,1,10,119,123,2,13,123,127,2,6,127,131,1,13,131,135,1,135,2,139,1,139,6,0,99,2,0,14,0]
        result = processCode(input)
        if result == 19690720:
            print('Desired noun: ' + str(noun) + '. Desired verb: ' + str(verb))
            exit() # Stop processing




#input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,19,5,23,2,9,23,27,1,5,27,31,1,5,31,35,1,35,13,39,1,39,9,43,1,5,43,47,1,47,6,51,1,51,13,55,1,55,9,59,1,59,13,63,2,63,13,67,1,67,10,71,1,71,6,75,2,10,75,79,2,10,79,83,1,5,83,87,2,6,87,91,1,91,6,95,1,95,13,99,2,99,13,103,1,103,9,107,1,10,107,111,2,111,13,115,1,10,115,119,1,10,119,123,2,13,123,127,2,6,127,131,1,13,131,135,1,135,2,139,1,139,6,0,99,2,0,14,0]


