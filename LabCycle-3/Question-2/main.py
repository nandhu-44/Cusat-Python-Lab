import numpy as np

def calculatePCA():
    num_rows = int(input("Enter the number of rows : "))
    num_cols = int(input("Enter the number of columns : "))
    matrix = np.zeros((num_rows, num_cols))
    for i in range(num_rows):
        for j in range(num_cols):
            matrix[i, j] = int(
                input(f"Enter element at position ({i+1}, {j+1}) : "))
    print("\nMatrix :\n", matrix)

    def pca(matrix):
        # Subtract the mean from each column
        centered_matrix = matrix - np.mean(matrix, axis=0)
        # Compute the covariance matrix
        covariance_matrix = np.cov(centered_matrix, rowvar=False)
        # Perform eigen decomposition on the covariance matrix
        eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
        # Sort eigenvalues and eigenvectors in descending order
        sorted_indices = np.argsort(eigenvalues)[::-1]
        sorted_eigenvalues = eigenvalues[sorted_indices]
        sorted_eigenvectors = eigenvectors[:, sorted_indices]
        # Calculate the explained variance ratio
        explained_variance_ratio = (sorted_eigenvalues / 
                                    np.sum(sorted_eigenvalues))
        # Transform the data into the new coordinate system 
        transformed_matrix = np.dot(centered_matrix, sorted_eigenvectors)
        return (transformed_matrix, sorted_eigenvalues, 
                sorted_eigenvectors, explained_variance_ratio)
    # Perform PCA on the matrix
    (transformed_matrix, eigenvalues, eigenvectors, 
     explained_variance_ratio) = pca(matrix)

    print("\nTransformed Matrix :\n", transformed_matrix)
    print("\nEigenvalues:\n", eigenvalues)
    print("\nEigenvectors :\n", eigenvectors)
    print("\nExplained Variance Ratio:\n",explained_variance_ratio)

calculatePCA()