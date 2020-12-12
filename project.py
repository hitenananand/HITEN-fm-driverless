#PROGRAM TO MULTIPLY TWO MATRICES USING PYTHON
#3x3 MATRICES
A = [[5,2,6],
[4,4,3],
[8,3,9]]
#3x3 MATRICES
B = [[7,4,8],
[1,3,7],
[8,5,7]]
#result is 3x3
AB= [[0,0,0],
[0,0,0],
[0,0,0]]
#iteration through rows of A
for i in range(len(A)):
    #ITERATION THROUGH COLUMNS OF B
    for j in range(len(B[0])):
        #ITERATION THROUGH ROWS OF B
        for k in range(len(B)):
            AB[i][j] +=A[i][k]*B[k][j]
for r in AB:
    print(r)

#TRANSPOSE OF MATRIX(A)
AT=[[0,0,0],
[0,0,0],
[0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        AT[j][i]= A[i][j]
for x in AT:
    print(x)

#TRANSPOSE OF MATRIX B
BT=[[0,0,0],
[0,0,0],
[0,0,0]]
for i in range(len(B)):
    for j in range(len(B[0])):
        BT[j][i]=B[i][j]
for y in BT:
    print(y)

#VERIFY : (AB)T = (B)T (A)T
    #multiplE AT BT
BTAT=[[0,0,0],
[0,0,0],
[0,0,0]]
for i in range(len(BT)):
    #ITERATION THROUGH COLUMNS OF B
    for j in range(len(AT[0])):
        #ITERATION THROUGH ROWS OF B
        for k in range(len(AT)):
            BTAT[i][j] +=BT[i][k]*AT[k][j]

    #tRanspose of AB
ABT=[[0,0,0],
     [0,0,0],
     [0,0,0]]
for i in range(len(AB)):
    for j in range(len(AB[0])):
        ABT[j][i]=AB[i][j]

if ABT==BTAT:
    print("VERIFIED: (ABT)=(BT)(AT)")
else:
    print("NOT VERIFIED")
