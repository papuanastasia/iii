def sequence_sum(a,b,c):
    d = 0
    for i in range(a,b+1,c):
        
        d += i
    return d

print(sequence_sum(2,6,2))
