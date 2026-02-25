def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here
    X = np.array(X, dtype=float)
    n = len(X)
    m = np.mean(X, axis=0)
    for i,x in enumerate(X):
        X[i] -= m

    C = X.T@X/(n-1)

    eigenvalues, eigenvectors = np.linalg.eigh(C)

    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]
    # sorted(eigenvectors, key:lambda = eigenvalues,  reverse=True)

    W = eigenvectors[:, :k]
    X_projected = X @ W

    return X_projected.tolist()