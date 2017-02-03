from random import*

def liste_alea(n, maxi):
    L=[]
    for i in range(n):
        x=randint(0,maxi) 
        L.append(x)
    return(L)

def tri_selection(L,n):
    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if L[j]<L[mini]:
                mini = j
        L[i],L[mini]=L[mini],L[i]
    return(L)

def tri_selection_inverse(L,n):
    for i in range(n-1):
        mini = i
        for j in range(i,n):
            if L[j]>L[mini]:
                mini = j
        L[i],L[mini]=L[mini],L[i]
    return(L)

L=liste_alea(100,100)
print(L)
print(tri_selection(L,len(L)))
