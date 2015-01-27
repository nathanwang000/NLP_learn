import numpy as np

def min_edit_distance(X, Y, print_table=True):
    ''' 
    Given input X, Y as strings,
    output the levenshtein edit distance between X and Y

    Background:
    Levenshtein edit distance is the minimum operation
    (insertion (1), deletion (1), subsitution (2))required
    to change one word into the other
    
    Intuition:
    Dynamic programming, taking advantage of the fact that
    the transformation from X to Y can be seen as an operation
    on the last character of the sequence, which can only be
    insertion, deletion, or subsitution.
    Consider a string X of length n and a string Y of length m,
    partition them into X[-1] and X[:-1], Y[-1] and Y[:-1].
    The possibilities are
    1) X[-1] and Y[-1] are not the same
    possible operations: deletion, subsitution, insertion
    a) deletion: one operation used
    so the problem reduced to D[i-1,j] + 1
    b) subsitution: 2 operations used
    so the problem reduced to D[i-1,j] + 2
    c) insertion
    insert after X[-1] to match Y
    the question remains: how long a string to insert?
    the answer is one is sufficient as proved below
    base case: insert 1 character
    the problem reduced to D[i,j-1] + 1
    assert: the total step for k charactor inserted is at most the same
    as that of 1 character inserted
    proof:
    k character inserted uses k steps. If it can be more efficient than 
    1 character insertion, then it has to reduce the problem to k-1 steps
    more efficient, it that's true, then 1 step algorithm can as well use
    k-1 insertion to achieve the same bound.
    2) X[-1] and Y[-1] are the same
    a) do nothing
    so the problem reduced to D[i-1,j-1]
    b) insertion, deletion, subsitution similar to case 1)
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
