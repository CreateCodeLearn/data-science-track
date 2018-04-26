## the long way
print("The long way: ", (y_test==y_pred).sum()/len(y_test))

## the short way
from sklearn.metrics import accuracy_score
print("The short way: ", accuracy_score(y_true=y_test, y_pred=y_pred))