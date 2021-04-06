import numpy  as np
#Arr= np.array([[[3,2,1],[6,4,5]],[[3,2,1],[6,4,5]]])
#print(Arr)
a=np.eye(125,dtype=float)

#array alamat array di komputer
print(len(a))

b=np.array([[2,3,2]])
c=np.array([[5,4,3]])
np.concatenate([b,c])
d=b[2-1]*[5]*[5]
e=b[3-1]*5+2-1*5
print(d+e)


















