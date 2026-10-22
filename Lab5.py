def input_matrix(rows, cols, name):
    print(f"\nEnter elements of Matrix {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print(f"Invalid row length. Please enter exactly {cols} values.")
            return None
        matrix.append(row)
    return matrix

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            product = sum(A[i][k] * B[k][j] for k in range(len(B)))
            row.append(product)
        result.append(row)
    return result

def main():
    try:
        r1 = int(input("Enter number of rows for Matrix A: "))
        c1 = int(input("Enter number of columns for Matrix A: "))
        r2 = int(input("Enter number of rows for Matrix B: "))
        c2 = int(input("Enter number of columns for Matrix B: "))
        
        A = input_matrix(r1, c1, 'A')
        B = input_matrix(r2, c2, 'B')
        
        if A is None or B is None:
            return
            
        # Matrix addition only if dimensions are same
        if r1 == r2 and c1 == c2:
            print("\nMatrix Addition (A + B):")
            sum_result = add_matrices(A, B)
            for row in sum_result:
                print(row)
        else:
            print("\nMatrix addition not possible (incompatible dimensions).")
            
        # Matrix multiplication only if c1 == r2
        if c1 == r2:
            print("\nMatrix Multiplication (A x B):")
            product_result = multiply_matrices(A, B)
            for row in product_result:
                print(row)
        else:
            print("\nMatrix multiplication not possible (columns of A != rows of B).")
            
    except ValueError:
        print("Invalid input. Please enter only integers.")

if __name__ == '__main__':
    main()
