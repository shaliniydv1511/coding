def transpose(m):
    a = []
    for i in range(len(m[0])):
        b = []
        for j in range(len(m)):
            t = m[j][i]
            b.append(t)
        a.append(b)
    return(a)

print(transpose([[1,2],[3,4],[5,6]]))