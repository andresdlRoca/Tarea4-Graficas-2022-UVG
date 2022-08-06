import math 

def matrixMult(A, B):
    result = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0,0,0,0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def convertMatrix(row, col, data):
    mat = []
    for i in range(row):
        rowList = []
        for j in range(col):
            rowList.append(data[row * i + j])
        mat.append(rowList)

    return mat

def identity(num):
    matrix = []
    for row in range(0, num):
        matrix.append([])
        for col in range(0, num):
            if (row == col):
                matrix[row].append(1)
            else:
                matrix[row].append(0)
    return matrix

def dot(A, B):
     return sum([x*y for x,y in zip(A, B)])

def matMultVect(M, v):
    return [dot(r,v) for r in M]

def subtractArrays(A,B):
     dims = isinstance(A,list) + 2 * isinstance(B,list)
     if dims == 3:
         return [ subtractArrays(ra,rb) for ra,rb in zip(A,B) ]
     if dims == 2:
         return [ subtractArrays(A,rb) for rb in B ]
     if dims == 1: 
         return [ subtractArrays(ra,B) for ra in A ]
     return A-B

def crossProduct(A, B):
    Res = [A[1]*B[2] - A[2]*B[1],
         A[2]*B[0] - A[0]*B[2],
         A[0]*B[1] - A[1]*B[0]]

    return Res


def norm(list):
    dist = math.sqrt(((list[0] - list[1]) ** 2)
                    + ((list[1] - list[2]) ** 2)
                    + ((list[2] - list[0]) ** 2))
    
    return dist