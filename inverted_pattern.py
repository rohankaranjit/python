




def inverted_full_pyramid(n):
    for i in range(n, 0, -1):

        for j in range(n - i):
            print(" ", end="")
            for k in range(2*i - 1):
            print("*", end="")
        print("")
        n = 5

# Call the function to print the inverted full pyramid
inverted_full_pyramid(n)

