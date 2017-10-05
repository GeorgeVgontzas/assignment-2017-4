import sys
import csv

def katwOrioLog(ari8mos):
    if ari8mos < 2:
        return 0  
    return 1 + katwOrioLog(ari8mos / 2)

def power(m,n):
    product = 1
    for i in range(n):
        product = product * m
    return product
  
def RowFromBottom(pinakas, grammi):
    return pinakas[-grammi-1]

def CreateAndInitToZero(grammes, sthles):
    return [[0 for j in range(sthles)] for i in range(grammes)]

def Bi(B, i, m):
    pinakas = B[(i - 1) * m : m * i]
    if m * i > len(B):
        for p in range(m * i - len(B)):
            pinakas.append([0 for x in range(len(B))])
    return pinakas

def Ai(A, i, m):
    return Bi(list(zip(*A)), i, m)

def Num(lista):
    ari8mos = 0
    for i in range(len(lista) - 1, -1, -1):
        ari8mos = ari8mos + power(2, i) * lista[len(lista) - i - 1]
    return ari8mos

def h(A, B):
    C = [0 for i in range(len(A))]
    for i in range (len(A)):
        if A[i] == 1 and B[i] == 1:
            C[i] = 1
        else:
            C[i] = A[i] + B[i]
    return C

def FourRussians(A,B,n):
    m = katwOrioLog(n)
    C = CreateAndInitToZero(n, n)
    for i in range(1, n // m + 2):
        dynamh = power(2,m)
        rs = CreateAndInitToZero(dynamh, n)
        bp = 1
        k = 0
        for j in range(1, dynamh):
            rs[j] = h(rs[j - power(2, k)],RowFromBottom(Bi(B, i, m), k))
            if bp == 1:
                bp = j + 1
                k = k + 1
            else:
                bp = bp - 1
        Ci = CreateAndInitToZero(n, n)
        for j in range(0, n):
            Aij = Num(list( zip(*Ai(A, i, m)) )[j])
            Ci[j] = rs[Aij]
        C = [h(C[i],Ci[i]) for i in range(len(C))]
    return C

def print_array(Array):
    for row in Array:
        print(row)

if len(sys.argv) == 3:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    with open(file1, newline='') as csvfile:
        A = [[int(x) for x in rec] for rec in csv.reader(csvfile, delimiter=',')]        
    with open(file2, newline='') as csvfile:
        B = [[int(x) for x in rec] for rec in csv.reader(csvfile, delimiter=',')]
    print_array((FourRussians(A, B, len(A))))
elif len(sys.argv) == 2:
    file1 = sys.argv[1]
    file = open(file1)
    komboi = set()
    for row in file:
        row = row.split()
        komboi.add(int(row[0]))
        komboi.add(int(row[1]))
    file.close()
    n = len(komboi)
    file = open(file1)
    A = CreateAndInitToZero(n, n)
    for i in range(n):
        A[i][i] = 1
    for row in file:
        row = row.split()
        A[int(row[0])][int(row[1])] = 1
        A[int(row[1])][int(row[0])] = 1
    PinakasGeitniashs = A
    for i in range(n - 1):
        PinakasGeitniashs = FourRussians(PinakasGeitniashs, A, n)
    for i in range(n):
        for j in range(i, n):
            if PinakasGeitniashs[i][j] == 1:
                print(i, j)
    
