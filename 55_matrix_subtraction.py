def matrix_substraction(mat1, mat2):

    mat3 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
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
    for i in range(len(mat3)):
        for j in range(len(mat3)):
            mat3[i][j] = mat1[i][j] - mat2[i][j]
            print(mat3[i][j], end = "\t")

        print()

matrix1 = [[10,5,4,2],[5,10,9,55],[9,19,69,8],[7,8,4,75]]
matrix2 = [[12,65,34,2],[1,5,8,45],[7,21,63,8],[0,78,4,75]]

matrix_substraction(matrix1,matrix2)