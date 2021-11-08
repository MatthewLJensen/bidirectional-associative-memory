import numpy as np

class BAM:
    def __init__(self, A_size, B_size):
        self.correlation_matrix = np.zeros((A_size, B_size), dtype=int)
        self.remaining = min(A_size, B_size)
    
    def print_correlation_matrix(self):
        print(self.correlation_matrix)
    
    def learn_association(self, A, B):
        x = (2*(np.array(A))) - 1
        y = (2*(np.array(B))) - 1
        xty = np.outer(x,y)
        self.correlation_matrix += xty
        self.remaining -= 1
        return self.remaining

    def recall(self, A, B):
        x = np.array(A)
        y = np.array(B)
        
        x2 = np.zeros(len(A), dtype=int)
        y2 = np.zeros(len(B), dtype=int)

        while ((not ((x == x2).all())) or (not ((y == y2).all()))):
            np.copyto(x2, x)
            np.copyto(y2, y)
           
            # do the dot product
            pre_y = np.dot(x, self.correlation_matrix)

            for i in range(len(y)):
                if pre_y[i] > 0:
                    y[i] = 1
                elif pre_y[i] < 0:
                    y[i] = 0

            # repeat for B -> A
            pre_x = np.dot(y, self.correlation_matrix.transpose())

            for i in range(len(x)):
                if pre_x[i] > 0:
                    x[i] = 1
                elif pre_x[i] < 0:
                    x[i] = 0

        return x, y

    def remaining_associations(self):
        return self.remaining


