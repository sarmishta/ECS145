from copy import deepcopy
import math


class Matrix(object):
    """
    Represent a matrix and allow for basic matrix operations to be done.
    """
    def __init__(self, X):
        """
        X - a list of lists, ie [[1],[1]]
        """
        self.X = X

    
    @property
    def rows(self):
        return len(self.X)
    
    @property
    def cols(self):
        return len(self.X[0])
    

    def __getitem__(self, key):
        return self.X[key]

    def __setitem__(self, key, value):
        assert self.cols == len(value)
        self.X[key] = value

    def __delitem__(self, key):
        """
        Delete a row of the matrix
        """
        del self.X[key]

    def del_column(self, key):
        """
        Delete a specified column
        """
        for i in range(0,self.rows):
            del self.X[i][key]

    @property
    def determinant(self):
        return recursive_determinant(self)

def recursive_determinant(X):
    """
    Find the determinant recursively.  
    """
    #Must be a square matrix
    assert X.rows == X.cols
    #Must be at least 2x2
    assert X.rows > 1

    term_list = []
    if X.cols>2:
        for j in range(0,X.cols):
            #Remove i and j columns
            new_x = deepcopy(X)
            del new_x[0]
            new_x.del_column(j)
            #multiplier
            multiplier = X[0][j] * math.pow(-1,(2+j))
            #Recurse to find the determinant
            det = recursive_determinant(new_x)
            term_list.append(multiplier*det)
        return sum(term_list)
    else:
        return(X[0][0]*X[1][1] - X[0][1]*X[1][0])


# X = Matrix([[1,2,2],[2,1,4],[2,4,5]])
# print(recursive_determinant(X))   