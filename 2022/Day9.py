import math

inputData = '''R 2
U 2
L 2
U 1
L 1
U 1
R 1
L 2
U 2
R 1
D 2
U 2
R 1
D 1
L 1
R 1
L 2
U 2
L 2
D 1
R 1
U 2
L 2
U 2
R 1
D 1
L 2
U 2
R 2
L 2
U 2
R 2
L 1
U 2
R 2
D 1
L 1
R 2
U 1
R 2
D 2
L 1
R 1
U 1
R 2
L 1
U 1
R 1
L 2
D 2
R 2
D 1
L 2
R 2
L 1
R 2
D 1
R 2
D 2
L 1
R 1
U 2
L 2
R 2
D 1
R 2
U 2
L 1
D 2
R 2
L 2
D 2
U 1
R 2
U 2
R 2
D 2
R 1
U 2
D 2
R 1
L 1
R 1
U 2
D 2
R 1
U 1
R 1
L 1
U 2
L 2
D 2
U 2
D 2
R 2
D 2
L 1
U 2
L 1
R 1
D 2
L 1
U 1
D 2
U 2
D 2
R 2
U 1
R 1
U 2
D 1
R 2
D 2
L 3
U 1
D 2
U 3
R 3
L 1
D 2
R 1
D 3
L 3
R 1
D 3
L 3
D 1
R 3
D 1
L 1
D 2
R 3
D 1
U 2
R 2
L 1
D 1
R 3
U 2
L 3
U 2
D 2
R 2
D 3
U 1
D 3
L 3
R 2
L 2
D 3
L 2
U 3
R 2
D 1
R 2
U 3
R 3
U 3
L 1
R 3
D 2
R 1
L 3
R 1
D 3
L 3
D 1
U 2
R 3
U 3
D 1
L 2
R 3
L 1
D 2
L 3
D 1
L 3
D 1
U 2
D 3
R 2
U 1
L 3
R 3
L 2
R 1
L 2
D 2
R 3
U 3
R 3
D 2
U 3
D 2
R 3
D 3
R 2
U 1
L 3
U 2
R 2
L 2
U 1
L 3
D 2
U 2
R 1
L 2
D 2
U 3
R 2
D 2
L 3
U 1
L 1
U 2
R 2
U 1
D 2
U 2
R 3
L 1
U 1
D 3
U 4
L 3
D 2
L 3
U 4
D 2
R 4
L 4
U 2
D 3
U 2
D 3
L 3
U 2
D 3
L 1
U 1
R 1
L 4
R 3
D 3
L 2
U 3
R 2
L 1
U 4
D 3
U 1
L 2
D 4
L 1
R 3
D 4
R 1
L 1
U 3
L 3
D 3
R 3
U 1
L 4
U 3
R 3
L 3
U 2
R 3
L 3
R 1
D 3
R 3
L 4
R 3
D 4
L 3
U 2
R 4
L 1
U 1
R 4
D 3
U 1
R 1
D 1
U 3
R 2
L 1
D 1
L 3
D 4
R 4
U 4
D 1
R 3
D 3
R 3
L 4
R 4
L 2
R 2
D 3
R 4
D 2
U 4
L 3
D 1
R 2
U 2
R 3
D 1
R 3
D 1
L 1
U 4
L 2
U 4
L 4
U 3
R 4
L 3
R 3
L 4
U 4
R 4
D 2
R 2
D 3
U 4
D 1
U 1
D 5
U 3
D 5
U 5
D 3
L 3
U 3
D 3
R 1
D 3
R 4
U 4
D 1
R 5
D 5
R 2
U 5
L 2
U 2
D 2
U 4
R 1
D 1
L 2
R 2
D 1
L 5
R 5
D 4
R 5
L 1
D 2
L 3
U 2
D 3
L 1
R 5
U 3
R 1
D 3
R 1
U 1
R 3
U 2
D 5
L 5
R 1
U 3
L 4
D 2
R 1
D 3
U 4
R 3
L 4
U 2
D 3
U 1
R 5
D 3
L 2
U 3
L 5
U 3
L 3
D 5
L 5
U 3
R 2
D 5
U 4
L 5
U 1
D 5
R 3
D 1
L 5
R 2
D 2
U 5
R 1
D 2
L 3
D 2
L 5
D 2
U 5
L 2
R 3
L 3
D 3
U 2
R 5
L 1
U 5
R 5
L 2
D 5
R 3
L 2
U 2
D 3
R 4
L 1
R 3
D 5
R 3
D 4
R 2
D 5
R 3
L 3
R 2
U 2
L 1
R 6
U 6
L 6
U 2
R 6
D 4
U 1
L 1
R 1
D 1
L 6
D 6
U 4
L 6
D 3
R 1
U 1
D 3
R 3
D 5
U 1
L 2
R 6
U 5
D 6
L 6
R 2
U 1
D 1
L 4
D 5
L 6
U 1
L 6
R 5
U 5
D 3
L 5
R 2
U 3
D 1
L 2
U 2
D 1
L 5
D 1
U 5
R 4
L 2
R 5
D 3
U 3
R 2
U 3
D 6
L 5
R 1
U 5
L 1
R 6
D 6
R 6
L 1
D 2
R 5
L 4
D 3
L 5
R 4
L 6
U 1
L 2
U 3
R 4
D 3
R 3
L 1
D 4
L 2
R 5
D 2
R 2
D 5
U 2
L 4
R 4
U 4
R 1
D 3
L 6
U 5
L 5
D 6
U 3
D 6
R 6
D 3
U 6
L 6
D 3
L 6
R 3
D 2
L 4
D 5
L 5
D 2
L 6
R 1
D 1
L 4
U 6
R 1
L 5
D 7
U 2
R 6
D 7
L 2
R 3
U 1
L 3
R 2
U 7
D 7
U 7
D 4
R 2
L 7
R 7
L 5
R 4
U 5
L 5
U 6
R 2
D 3
L 2
U 6
D 5
R 2
D 2
R 5
U 7
R 3
D 1
L 5
R 1
U 3
D 6
U 6
L 7
U 4
L 6
D 1
L 7
U 4
D 7
L 1
D 6
L 2
R 5
L 7
U 3
D 2
R 7
L 2
U 6
L 3
U 6
L 5
R 2
L 7
D 3
L 7
R 1
L 1
R 5
D 6
L 2
D 5
L 4
D 3
U 5
D 1
R 4
U 1
L 2
R 3
U 7
D 6
U 2
D 4
U 5
D 5
U 7
R 2
D 1
U 2
L 2
U 3
D 1
R 4
D 1
R 3
U 1
R 7
D 4
R 3
D 2
L 2
U 4
L 2
U 6
L 4
D 6
U 3
L 1
U 4
R 7
D 6
L 2
D 7
R 4
U 5
R 4
D 5
R 6
D 4
R 4
U 2
R 3
L 7
R 8
D 8
R 5
U 2
D 6
L 2
R 4
U 3
L 1
R 2
D 5
L 1
D 5
L 5
U 1
R 8
D 1
U 1
L 1
R 8
L 3
R 6
L 1
U 3
R 6
L 5
U 2
L 8
R 4
U 4
R 6
U 5
R 1
L 2
R 5
D 1
U 4
L 3
U 3
R 1
U 3
R 8
L 1
U 2
L 7
D 6
L 6
R 4
D 2
R 2
L 8
D 4
R 4
U 4
L 6
D 3
R 7
D 8
U 4
R 4
U 2
L 8
D 5
L 4
U 7
D 8
U 6
R 6
L 5
D 5
L 2
D 1
R 1
D 4
R 5
L 7
D 8
U 2
D 3
L 5
R 4
L 7
R 3
L 1
D 8
R 5
L 8
R 8
D 1
R 4
D 1
L 2
D 5
L 7
U 1
L 4
R 5
L 3
R 9
D 9
L 4
R 6
L 6
R 1
L 3
R 5
D 8
L 1
U 2
R 8
U 7
D 6
L 8
D 1
L 9
D 5
L 1
D 6
L 8
R 2
L 6
R 4
U 1
R 6
L 5
R 5
L 6
R 8
D 5
L 4
R 2
L 7
R 2
U 9
L 6
R 2
U 7
D 4
U 2
L 2
U 8
R 8
U 3
R 6
D 6
L 2
D 4
L 4
R 2
L 1
U 8
D 2
R 2
L 1
R 7
L 8
D 8
L 4
U 4
R 5
U 1
D 8
L 8
R 9
D 6
L 1
D 5
L 9
U 6
D 6
U 3
D 5
R 5
U 9
L 2
R 5
U 9
L 1
D 4
U 4
L 5
D 6
R 3
L 6
U 3
R 4
U 5
L 5
D 8
L 6
U 4
D 1
U 7
D 2
L 3
R 7
U 1
R 4
U 4
R 9
U 3
D 2
L 6
R 9
U 3
L 8
R 10
U 3
R 8
D 8
L 1
U 4
R 5
U 8
D 10
U 10
L 7
D 5
L 2
R 7
L 1
U 10
R 1
D 1
L 5
R 7
U 6
L 3
R 7
U 4
R 3
U 3
R 4
U 8
L 8
D 6
L 5
U 10
L 9
R 3
U 10
D 9
U 5
D 10
U 7
D 6
U 9
L 8
U 3
D 6
R 9
U 9
D 4
R 8
U 7
R 6
U 5
R 5
U 3
D 4
R 9
L 7
D 7
U 1
L 3
R 4
D 8
L 4
D 6
U 1
R 7
D 4
L 9
D 2
R 4
U 10
D 5
U 6
D 6
R 5
U 6
D 6
L 7
U 4
D 1
L 6
R 8
L 7
U 8
L 2
R 6
L 9
D 2
U 9
D 5
U 10
D 1
R 9
L 6
D 7
U 1
D 4
L 3
R 7
U 1
R 6
D 4
R 1
D 4
L 8
R 1
U 10
D 1
U 5
R 6
U 5
D 2
U 10
R 8
L 7
U 6
L 4
R 6
L 7
U 3
R 4
D 1
L 4
R 7
D 2
L 4
U 3
D 6
U 10
D 5
R 8
U 5
L 9
D 4
L 4
D 8
U 9
R 2
U 4
R 4
U 9
D 1
R 7
U 5
L 2
U 10
R 4
D 1
L 3
R 11
D 7
U 7
D 7
L 11
U 2
D 1
U 1
R 1
U 3
L 6
U 10
L 4
U 5
L 10
D 1
U 8
R 7
L 4
U 7
L 9
U 6
L 11
U 3
R 8
L 6
D 9
L 9
D 1
R 7
L 11
D 9
R 7
U 2
D 11
L 4
D 4
R 11
D 7
U 2
D 7
R 2
D 1
L 6
D 11
R 3
U 7
L 10
U 7
D 2
R 2
U 1
L 9
R 11
L 3
R 7
L 2
D 11
R 1
D 4
R 3
L 10
U 5
D 3
R 10
D 8
U 1
D 2
R 10
L 8
R 1
D 8
U 6
R 8
D 8
L 2
D 7
U 4
L 5
R 4
D 4
U 7
D 11
U 11
R 4
L 6
U 3
L 10
U 1
L 11
U 3
D 6
L 11
R 4
L 3
D 12
L 7
R 9
L 9
U 10
L 1
D 6
L 10
U 3
R 6
D 5
L 6
R 8
D 4
R 6
L 6
D 9
L 1
D 11
U 6
L 3
R 10
U 12
R 11
D 10
U 5
R 6
D 12
U 12
R 8
U 5
D 1
R 12
D 1
R 7
U 8
D 5
U 7
D 3
R 7
D 8
U 11
R 2
U 4
L 2
R 1
L 3
U 9
L 5
D 11
R 10
L 3
U 3
D 3
R 1
L 8
D 6
R 7
U 11
L 6
D 1
R 12
D 8
U 7
R 2
U 5
R 4
U 10
L 8
D 5
U 10
D 3
L 6
R 4
L 9
D 6
R 7
D 4
U 10
D 1
L 6
R 1
L 7
U 5
L 9
U 12
L 7
U 6
D 6
U 9
L 7
U 4
D 5
L 1
U 5
D 1
L 10
D 2
R 3
D 13
U 11
L 1
U 1
D 1
R 12
U 13
L 5
D 11
L 9
U 11
L 2
R 6
D 7
L 2
U 5
R 2
U 10
L 9
D 7
R 12
D 10
L 12
D 8
L 8
R 12
D 11
U 12
L 1
U 2
D 6
R 3
D 2
U 9
L 10
R 4
U 2
D 10
U 7
R 6
U 9
R 4
L 3
U 13
R 9
U 6
D 8
L 5
R 11
L 6
R 12
D 5
U 7
R 11
D 1
L 9
R 12
U 2
R 5
U 1
R 9
U 6
D 4
R 2
U 2
D 5
L 9
R 6
U 4
L 6
R 9
L 4
U 3
L 9
R 6
L 5
D 6
L 3
R 6
L 3
D 9
U 5
D 1
R 5
L 3
U 9
R 7
L 8
R 6
L 7
U 4
D 13
U 2
L 1
U 11
R 8
L 13
D 1
U 4
L 13
D 1
L 8
D 13
L 2
R 2
D 1
L 14
U 7
R 11
L 1
R 4
L 5
R 11
U 7
D 8
L 3
U 1
L 12
U 13
D 9
R 1
L 11
U 12
D 5
U 10
D 10
R 9
L 1
D 5
R 7
L 1
D 13
R 10
U 2
R 3
L 14
D 7
R 12
U 13
L 2
U 13
L 3
U 5
L 11
R 8
D 11
R 6
L 11
R 5
L 3
U 1
L 5
R 13
L 12
D 10
R 8
D 6
L 1
R 10
U 5
R 3
D 11
L 8
R 4
D 2
L 1
R 7
U 3
L 14
R 3
L 4
R 13
L 10
U 3
D 1
L 11
U 1
D 6
R 10
U 1
R 2
L 7
U 3
L 5
U 4
D 7
R 8
U 12
R 6
L 2
D 5
L 11
R 4
L 4
R 6
L 3
R 10
U 4
D 9
U 1
D 4
L 12
D 13
L 1
D 6
R 8
L 1
D 9
L 8
U 3
D 3
U 2
R 11
U 10
L 5
D 11
U 12
D 3
R 15
L 1
R 5
D 9
U 15
D 2
L 9
U 9
D 15
R 4
L 9
R 8
L 12
D 5
R 12
U 9
L 9
U 7
L 12
R 11
U 9
L 15
D 9
L 4
R 4
U 13
D 7
R 7
D 8
U 5
D 5
L 15
D 2
R 8
D 10
R 5
U 13
R 1
L 8
D 12
R 2
L 4
D 9
L 9
D 7
R 5
U 15
R 9
L 2
R 8
U 11
D 15
U 13
D 5
U 5
R 11
U 7
R 11
D 12
U 6
D 6
L 8
D 8
R 14
U 13
R 11
D 1
R 4
U 14
R 11
L 8
D 2
U 13
R 15
L 10
D 2
L 3
R 9
U 2
R 8
U 15
R 3
D 4
L 7
D 7
R 1
D 13
R 1
L 13
U 9
L 13
U 10
L 15
D 5
R 11
D 3
U 3
R 4
L 7
R 1
U 13
R 9
U 7
R 10
D 5
U 7
R 6
L 14
U 2
R 8
D 2
U 16
D 12
R 11
D 4
L 8
U 8
L 13
D 5
R 4
U 8
D 15
R 8
D 13
R 16
U 4
D 3
U 5
D 8
R 16
L 13
U 3
D 6
L 9
R 10
D 6
R 16
D 15
R 11
L 8
D 8
U 4
R 16
D 1
U 11
L 15
R 7
D 2
R 1
D 4
L 1
U 15
D 16
R 3
U 10
D 9
U 6
D 15
R 11
L 6
R 2
U 14
R 4
L 15
R 15
D 16
U 9
D 2
L 8
D 15
R 5
U 13
L 15
D 1
R 4
U 14
D 15
L 15
U 13
R 16
L 7
R 4
D 13
L 15
D 3
L 7
D 4
R 12
D 10
U 8
D 6
L 13
R 15
U 12
L 4
R 16
D 1
R 14
L 9
D 13
U 2
D 9
U 16
L 15
R 12
L 14
R 6
D 1
R 2
L 15
U 7
L 16
U 15
D 11
R 11
L 3
R 11
L 15
U 17
L 14
R 4
U 15
D 6
L 2
R 7
L 16
U 4
L 14
U 9
L 7
D 16
R 4
D 2
R 15
L 6
R 6
D 1
U 5
D 14
U 4
D 11
R 5
U 16
L 3
D 7
R 10
L 3
D 8
L 10
U 1
D 16
L 6
R 6
L 14
R 6
U 11
L 17
D 7
R 2
L 12
D 15
U 16
R 2
U 3
R 16
U 12
L 3
U 5
D 1
R 12
U 17
D 11
L 16
U 13
L 5
D 1
R 2
L 10
U 12
D 7
U 6
R 4
U 5
L 3
R 16
D 1
U 14
R 15
D 6
U 14
R 4
L 6
D 11
R 16
L 15
U 7
L 10
R 5
L 15
R 12
L 17
U 5
D 14
L 6
R 2
U 5
R 10
L 8
D 2
U 17
L 13
D 17
L 5
R 11
L 3
U 11
R 1
L 3
D 1
L 7
D 14
R 13
U 9
D 7
L 15
U 5
D 4
R 7
L 10
D 6
R 18
U 5
R 18
U 6
D 17
U 8
R 16
D 12
R 12
D 9
R 9
U 4
R 16
L 1
D 12
L 12
R 11
D 15
U 13
L 8
R 4
L 1
R 1
D 11
R 15
D 3
L 17
D 17
R 11
U 13
D 11
R 4
D 17
U 8
L 1
D 2
L 16
D 6
L 15
D 17
L 8
U 5
D 15
L 15
U 11
D 9
L 18
U 18
R 14
L 4
U 17
R 11
D 18
U 2
R 9
D 15
R 5
L 13
R 2
L 18
D 5
U 14
L 17
R 3
U 4
R 15
U 1
D 15
U 12
D 17
U 11
L 3
R 10
U 13
R 12
L 10
R 1
D 4
U 2
D 14
R 14
U 5
R 16
U 17
R 16
U 18
R 6
U 5
R 18
U 12
D 7
R 9
L 1
U 15
D 10
L 4
U 9
L 3
U 1
R 12
D 14
U 13
L 10
R 8
U 5
D 7
U 1
L 13
U 14
D 18
L 13
D 12
R 2
L 6
D 17
L 18
R 6
U 4
L 7
R 8
U 5
D 1
L 3
U 10
R 5
D 7
U 16
R 12
U 8
L 18
R 1
L 11
D 14
L 19
R 15
U 14
L 8
R 14
U 13
D 18
U 14
L 14
U 11
L 10
D 11
L 11
R 15
L 12
R 10
L 9
R 9
L 9
D 3
R 9
L 6
R 8
D 7
L 18
D 12
R 3
U 7
R 18
U 9
L 14
D 12
L 10
U 15
L 11
R 17
D 7
R 5
L 3
U 13
D 7
U 13
R 16
D 2
L 7
R 15
L 14
U 19
D 3
L 19
D 11
R 8
D 6
U 12
R 5
U 6
L 7
R 4
L 3
D 6
L 17
U 16
D 11
U 12
D 4
R 6
D 10
L 3
D 15
R 5
L 6
D 11
U 17
L 14
D 15
L 1
D 6
R 16
D 11
U 2
D 2
U 7
D 10
L 11
D 19
L 12
D 3
L 18
U 3'''

#inputData = "R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2" # pt 1
inputData = "R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20" # pt 2

# 202 too low

newLines = inputData.split("\n")

directionTable = {
    "U": (  0,   1 ),
    "D": (  0,  -1 ),
    "L": ( -1,   0 ),
    "R": (  1,   0 ),
}

headPosition = (0,0)

tail = [
    (0,0), # 1
    (0,0), # 2
    (0,0), # 3
    (0,0), # 4
    (0,0), # 5
    (0,0), # 6
    (0,0), # 7
    (0,0), # 8
    (0,0), # 9
]

tailHistory = {}

def getDistance(pos1, pos2):
    return math.sqrt( math.pow(pos2[0]-pos1[0], 2) + math.pow(pos2[1]-pos1[1], 2) )

for command in newLines:
    spaceSplit = command.split(" ")
    direction = spaceSplit[0]
    distance = int(spaceSplit[1])
    
    dirMap = directionTable[direction]
    for i in range(distance):
        headPosition = ( headPosition[0]+dirMap[0], headPosition[1]+dirMap[1] )
        
        for index in range( len(tail) ):
            tailPart = tail[index]
            #print(tailPart)
            #tailPosition = tail[len(tail)-1]
            
            if index == 0:
                dist = getDistance(headPosition, tailPart)
            else:
                dist = getDistance(tail[index-1], tailPart)
            
            if dist >= 2:
                if index == 0:
                    tail[index] = (headPosition[0] - dirMap[0], headPosition[1] - dirMap[1])
                else:
                    tail[index] = (tail[index-1][0] - dirMap[0], tail[index-1][1] - dirMap[1])
            
            if tailPart in tailHistory:
                tailHistory[tailPart] += 1
            else:
                tailHistory[tailPart] = 1

print(len(tailHistory))
print(tail)
print(headPosition)