import numpy as np


def calculatePCA():
    # Taking the number of rows and columns
    num_rows = int(input("Enter the number of rows : "))
    num_cols = int(input("Enter the number of columns : "))

    # Defining the matrix and taking input element by element
    matrix = np.zeros((num_rows, num_cols))
    for i in range(num_rows):
        for j in range(num_cols):
            matrix[i, j] = int(
                input(f"Enter element at position ({i+1}, {j+1}) : "))
    print()
    print("Matrix :")
    print(matrix)

    # Calculate the mean of each column
    column_means = np.mean(matrix, axis=0)

    # Center columns by subtracting column means
    centered_matrix = matrix - column_means

    # Calculate the covariance matrix of centered matrix
    covariance_matrix = np.cov(centered_matrix.T)

    # Eigendecomposition of covariance matrix
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

    # Create the projection matrix using the top two eigenvectors
    projection_matrix = eigenvectors[:, :2]

    # Project the data
    transformed_matrix = np.dot(projection_matrix.T, 
                                centered_matrix.T).T

    print()
    print("Transformed Matrix: ")
    print(transformed_matrix)
    print()


calculatePCA()
