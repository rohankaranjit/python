# Function to print full pyramid pattern
def full_pyramid(n):
    for i in range(1, n + 1):

        for j in range(n - i):
            print(" ", end="")
