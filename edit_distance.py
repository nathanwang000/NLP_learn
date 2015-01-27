import numpy as np

def min_edit_distance(X, Y, print_table=True):
    ''' 
    Given input X, Y as strings,
    output the levenshtein edit distance between X and Y

    Background:
    levenshtein edit distance is the minimum operation
    (insertion (1), deletion (1), subsitution (2))required
    to change one word into the other
    
    Intuition:
    dynamic programming, taking advantage of the fact that
    the transformation from X to Y can be seen as an operation
    on the last character of the sequence, which can only be
    insertion, deletion, or subsitution
    '''
    N = len(X); M = len(Y)
    D = np.zeros((N+1, M+1))
    # initialization
    D[:,0] = np.arange(N+1)
    D[0,:] = np.arange(M+1)
    # recurrence relation
    for i in range(1,N+1):
        for j in range(1,M+1):
            D[i,j] = min(D[i-1,j]+1, # deletion of one char in X
                         D[i,j-1]+1, # insertion of one char in X
                         D[i-1,j-1] + (2 if X[i-1]!=Y[j-1] else 0))
        
    # for output purpose only
    if print_table:
        out = "%5s%5s" % ('NULL','#')
        for i in range(1,M+1):
            out += "%5s" % Y[i-1]
        print out
        for i in range(N+1):
            out = "%5s" % (X[i-1] if i-1>=0 else '#')
            for j in range(M+1):
                out += "%5d" % D[i,j]
            print out
    
    return D[N,M]

if __name__ == '__main__':
    min_edit_distance('intention','execution', 'True')