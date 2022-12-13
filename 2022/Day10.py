inputData = '''noop
addx 25
addx -5
addx -14
addx 4
noop
addx 2
addx 3
noop
noop
noop
noop
addx 3
addx 5
addx 2
noop
noop
addx 5
noop
noop
noop
addx 1
addx 2
addx 5
addx -40
addx 5
noop
addx 26
addx -20
addx -3
addx 2
noop
addx -4
addx 9
addx 5
addx 2
addx 11
addx -10
addx 2
addx 5
addx 2
addx 5
noop
noop
noop
addx -31
addx 32
addx -37
addx 1
addx 8
addx 13
addx -15
addx 4
noop
addx 5
noop
addx 3
addx -2
addx 4
addx 1
addx 4
addx -14
addx 15
addx 4
noop
noop
noop
addx 3
addx 5
addx -40
noop
addx 5
addx 8
addx -3
noop
addx 2
addx 9
addx -4
noop
noop
noop
noop
addx 5
addx -9
addx 10
addx 4
noop
noop
addx 5
addx -19
addx 24
addx -2
addx 5
addx -40
addx 22
addx -19
addx 2
addx 5
addx 2
addx 5
noop
noop
addx -2
addx 2
addx 5
addx 3
noop
addx 2
addx 2
addx 3
addx -2
addx 10
addx -3
addx 3
noop
addx -40
addx 2
addx 11
addx -5
addx -1
noop
addx 3
addx 7
noop
addx -2
addx 5
addx 2
addx 3
noop
addx 2
addx 6
addx -5
addx 2
addx -18
addx 26
addx -1
noop
noop
noop
noop'''

newLines = inputData.split("\n")

x = 1
currentCycle = 0
cycleHistory = {}

for line in newLines:
    currentCycle += 1
    
    if line == "noop":
        pass
    else:
        cycleHistory[str(currentCycle)] = x
        currentCycle += 1
        cycleHistory[str(currentCycle)] = x
        
        addition = int(line.split(" ")[1])
        x += addition
        #currentCycle += 2
    
    isIn = False
    for key in cycleHistory:
        if key == str(currentCycle):
            isIn = True
    if isIn == False:
        cycleHistory[str(currentCycle)] = x

cycleAddition = [20, 60, 100, 140, 180, 220]
total = 0
for key in cycleHistory:
    if int(key) in cycleAddition:
        total += cycleHistory[key] * int(key)
        print(cycleHistory[key], "*", int(key), "=", cycleHistory[key] * int(key))

#print(cycleHistory)
print(total)