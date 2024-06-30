def halfDiamondStar(N): 

    for i in range(N): 
  
        for j in range(0, i + 1): 
            print("*", end = "") 
        print() 
  
    # Loop to print the lower  
    # diamond pattern 
    for i in range(1, N): 
  
        for j in range(i, N): 
            print("*", end = "") 
        print() 
  
# Driver Code 
N = 5; 
  
# Function Call 
