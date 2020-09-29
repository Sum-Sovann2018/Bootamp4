def matrix_multiplication(mat1, mat2):

    mat3 = [[0,0,0],[0,0,0],[0,0,0]]
    print("Matrix 1:")

    for i in range(len(mat1)):

        for j in range(len(mat1)):

            print(mat1[i][j], end = "\t")
        print()

    print("\nMatrix 2:")

    for i in range(len(mat2)):

        for j in range(len(mat2)):
            print(mat2[i][j], end = "\t")
        print()

    print("\nThe result is:")
    for i in range(len(mat1)):

        for j in range(len(mat2[0])):

            for k in range(len(mat2)):
                mat3[i][j] += mat1[i][k] * mat2[k][j]
            print(mat3[i][j], end = "\t")

        print()

matrix1 = [[3,7,5],[2,6,7],[4,3,2]]
matrix2 = [[6,5,4],[3,2,1],[1,2,3]]

matrix_multiplication(matrix1,matrix2)