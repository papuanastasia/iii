def find_smallest_int(a):
    s = (a[0])
    for i in range(len(a)):
        if s > a[i]:
            s = a[i]
    return(s)
print(find_smallest_int([34,15,88,2]))


