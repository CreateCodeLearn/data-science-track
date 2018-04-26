def rmse(y_hat, y):
    return np.sqrt(np.sum((y_hat-y)**2)/len(y))