def get_matrix(n=' '):
    """Function to get matrix"""
    dim = [int(x) for x in input("Enter size of{}matrix: ".format(n)).split()]
    mat = []
    print("Enter{}matrix: ".format(n))
    for i in range(dim[0]):
        row = [int(x) if x.isdigit() else float(x) for x in input().split()]
        mat.append(row)
    return dim, mat


def print_matrix(mat):
    """Function to print matrix"""
    print("The result is:")
    for i in mat:
        print(*i, sep=' ')


def mat_add():
    """Function to add two matrices"""
    dim_a, mat_a = get_matrix(' first ')
    dim_b, mat_b = get_matrix(' second ')
    if dim_a[0] == dim_b[0] and dim_a[1] == dim_b[1]:
        mat_c = []
        for i in range(dim_a[0]):
            mat_c.append([])
            for j in range(dim_a[1]):
                mat_c[i].append(mat_a[i][j] + mat_b[i][j])
        print_matrix(mat_c)

    else:
        print("The operation cannot be performed.")


def mat_scalar_mul():
    """Function to multiply matrix by a constant"""
    dim_a, mat_a = get_matrix()
    x = input("Enter constant: ")
    if x.isdigit():
        scalar = int(x)
    else:
        scalar = float(x)

    for i in range(dim_a[0]):
        for j in range(dim_a[1]):
            mat_a[i][j] *= scalar

    print_matrix(mat_a)


def mat_mul():
    """Function to multiply two matrices"""
    dim_a, mat_a = get_matrix(' first ')
    dim_b, mat_b = get_matrix(' second ')
    if dim_a[1] == dim_b[0]:
        mat_c = []
        for i in range(dim_a[0]):
            mat_c.append([])
            for j in range(dim_b[1]):
                c = 0
                for k in range(dim_a[1]):
                    c = c + mat_a[i][k] * mat_b[k][j]
                mat_c[i].append(c)

        print_matrix(mat_c)

    else:
        print("The operation cannot be performed.")


def mat_transpose():
    """Function to call matrix transpose funtions based on selected
    option"""
    print("""1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
    option = int(input("Your choice: "))
    if option == 1:
        main_diagonal()
    elif option == 2:
        side_diagonal()
    elif option == 3:
        vertical_line()
    elif option == 4:
        horizontal_line()


def main_diagonal():
    """Funtion to Transpose matrix on main diagonal"""
    dim_a, mat_a = get_matrix()
    mat_c = []
    for i in range(dim_a[1]):
        mat_c.append([])
        for j in range(dim_a[0]):
            mat_c[i].append(mat_a[j][i])
    print_matrix(mat_c)


def side_diagonal():
    """Function to Transpose matrix on Side Diagonal"""
    dim_a, mat_a = get_matrix()
    mat_c = []
    for i in range(dim_a[1] - 1, -1, -1):
        mat_c.append([])
        for j in range(dim_a[0] - 1, -1, -1):
            mat_c[dim_a[1] - i - 1].append(mat_a[j][i])
    print_matrix(mat_c)


def vertical_line():
    """Function to transpose matrix on vertical line"""
    dim_a, mat_a = get_matrix()
    mat_c = []
    for i in range(dim_a[0]):
        mat_c.append([])
        for j in range(dim_a[1] - 1, -1, -1):
            mat_c[i].append(mat_a[i][j])
    print_matrix(mat_c)


def horizontal_line():
    """Function to transpose matrix on horizontal line"""
    dim_a, mat_a = get_matrix()
    mat_c = []
    for i in range(dim_a[0] - 1, -1, -1):
        mat_c.append([])
        for j in range(dim_a[1]):
            mat_c[dim_a[1] - 1 - i].append(mat_a[i][j])
    print_matrix(mat_c)


def find_minor(m, i, j):
    """Function to find minors"""
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def find_determinant(m):
    """Recursive function to find determinant"""
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    det = 0
    for fc in range(len(m)):
        det += ((-1) ** fc) * m[0][fc] * find_determinant(find_minor(m, 0, fc))
    return det


def mat_determinant():
    """Determinant function"""
    dim_a, mat_a = get_matrix()
    if dim_a[0] == dim_a[1]:
        print("The result is:")
        if dim_a[0] > 1:
            print(find_determinant(mat_a))
        else:
            print(*mat_a[0])
    else:
        print("The operation cannot be performed.")


def mat_inverse():
    """Function to inverse the matrix"""
    dim_a, mat_a = get_matrix()

    if dim_a[0] == 1:
        if mat_a[0][0] == 0:
            print("As determinant is zero,the operation cannot be performed.")
            return
        else:
            print(1)
            return

    determinant = find_determinant(mat_a)

    if determinant == 0:
        print("As determinant is zero,the operation cannot be performed.")
        return

    # special case for 2x2 matrix:
    if dim_a[0] == 2:
        return [[mat_a[1][1]/determinant, -1*mat_a[0][1]/determinant],
                [-1*mat_a[1][0]/determinant, mat_a[0][0]/determinant]]

    # find matrix of cofactors
    mat_adj = []
    for fr in range(dim_a[0]):
        mat_adj.append([])
        for fc in range(dim_a[1]):
            minor = find_minor(mat_a, fr, fc)
            val = find_determinant(minor)
            cof = ((-1) ** (fr + fc)) * val
            mat_adj[fr].append(cof)

    mat_c = []
    for i in range(dim_a[0]):
        mat_c.append([])
        for j in range(dim_a[1]):
            mat_c[i].append(mat_adj[j][i])

    for r in range(dim_a[0]):
        for c in range(dim_a[1]):
            mat_c[r][c] = mat_c[r][c]/determinant

    print_matrix(mat_c)


while True:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    choice = int(input("Your choice: "))
    if choice == 1:
        mat_add()
    elif choice == 2:
        mat_scalar_mul()
    elif choice == 3:
        mat_mul()
    elif choice == 4:
        print()
        mat_transpose()
    elif choice == 5:
        mat_determinant()
    elif choice == 6:
        mat_inverse()
    elif choice == 0:
        break
    print()
