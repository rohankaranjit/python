# Recursive function to find N^P.
def power(N, P):
 

    # only then it will enter it,
    # otherwise not
    if P == 0:
        return 1
 
    # Recurrence relation
    return (N*power(N, P-1))
 # Driver code
if __name__ == '__main__':
    N = 5
    P = 2
     print(power(N, P))
