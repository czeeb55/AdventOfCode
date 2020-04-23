# https://adventofcode.com/2019/day/1
def calculateFuel(mass):
    fuel = mass // 3 # Divide by 3 and round down
    fuel = fuel - 2 
    return fuel

def calculateFuelAdvanced(mass):
    total = 0 # Total fuel for the component
    fuel =  calculateFuel(mass) # Get initial fuel requirements
    while fuel > 0: # Calculate fuel needed for the fuel
        total += fuel # Sum up. If the calculated fuel in the next line is 0 or negative, it won't reach this point and get added.
        subfuel = calculateFuel(fuel)
        fuel = subfuel
    return total



# Each person given unique list of 100 values
ship = [76542,
97993,
79222,
55538,
126710,
77603,
67546,
129345,
60846,
52191,
126281,
85662,
79245,
78514,
91236,
126982,
94593,
63104,
96955,
122919,
92047,
63529,
75949,
65479,
116132,
55851,
100051,
120419,
79243,
109752,
57719,
131000,
99825,
92855,
111945,
58349,
104867,
53638,
110072,
111190,
126422,
72304,
62865,
113793,
98395,
86596,
89219,
135417,
113665,
87273,
144161,
97285,
136308,
79486,
140622,
138221,
115714,
142175,
114524,
50519,
112963,
109686,
113104,
50622,
102019,
96717,
148433,
70861,
133918,
89471,
112281,
109168,
68965,
109233,
101051,
52587,
65339,
97698,
126416,
61012,
120883,
81018,
60398,
112250,
64253,
98120,
74640,
134790,
80984,
61221,
119815,
96125,
96105,
87124,
60042,
141705,
57290,
57881,
131585,
51360]

sum =0
for component in ship:
    fuel = calculateFuelAdvanced(component)
    sum += fuel
print(sum)