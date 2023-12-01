N = int(input()) 

for i in range(1, N*2) : 
    if (N-i > 0) : {
        print(" " * (N-i) + "*" * (2*i-1))
    }
    else : {
        print(" " * (i-N) + "*" * ((N-(i-N)) * 2-1))
    }
    
    