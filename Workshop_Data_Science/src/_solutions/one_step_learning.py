def one_step_learning(X, y):
    return np.dot( np.dot ( np.linalg.inv ( np.dot(X.T, X) ), X.T), y )