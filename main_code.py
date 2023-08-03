
def tri(A):
    n=len(A)
    for j in range(n-1,-1,-1):
        for i in range(0,j):
            if A[j]>A[i+1] and A[j]!=0:
                A[i],A[i+1]=A[i+1],A[i]
    return A[:5]
                
def position_list(O,G):
    R=[]
    for i in range(len(O)):
        R.append(trouve_pos(G,O[i]))
    return R
def existence(G,p):
    R=[]
    for i in range(len(p)):
        if p[i] in G:  	
            R.append(p[i])
    return R
def none_existence(ko,KO):
    R=[]
    for i in range(len(ko)):
        if ko[i] not in KO:
            R.append(ko[i])
    return R
def trouve_pos(G,x):
    i=0
    while G[i]!=x and i<len(G):
        i+=1
    return i
    

def file_managing(F):
    a_file=open(F,"r")
    maker=[]
    for line in a_file:
        l=line.strip()
        p=l.split()
        maker.append(p)
    a_file.close()
    for i in range(int(maker[0][0])):
        maker[2*i][0]=int(maker[2*i][0])
        maker[2*i+1][0]=int(maker[2*i+1][0])
    maker[-1][0]=int(maker[-1][0])
    return maker
def liste_transfomation(T):
    ing_list=[]
    val_list=[]
    for i in range(1,2*T[0][0],2):
        Y=[T[i],T[i+1]] 
        beni=5
        if Y[0][0]==0 or Y[1][0]==0:
            beni=10
        ing=[]
        for k in range(1,len(Y[0])):
            ing.append(Y[0][k])
        G=none_existence(ing,ing_list)
        for p in range(len(G)):
            ing_list.append(G[p])
            val_list.append(0)
        val=Y[0][0]
        for i in position_list(ing,ing_list):
            val_list[i]+=abs(beni-int(val))
        ing1=[]
        for n in range(1,len(Y[1])):
            ing1.append(Y[1][n])
        G=none_existence(ing1,ing_list)
        for i in range(len(G)):
            ing_list.append(G[i])
            val_list.append(0)
        val1=Y[1][0]
        for i in position_list(ing1,ing_list):
            val_list[i]-=abs(beni-val1)
    return [val_list,ing_list]

def resolution_all(F):
    L=file_managing(F)
    m=liste_transfomation(L)
    conc=[]
    end=''
    for i in range(len(m[0])):
        if m[0][i]>=0:
            conc.append(m[1][i])
    for i in range(len(conc)):
       end=end+' '+conc[i]
    return print(len(conc),' ',end)
