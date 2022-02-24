import numpy as numpy
def create_matrix(mc):
 print("/n array"+str(mc)+"elements")
 array_1=map(int,input().split())
 array_1=np.array(list(array_1))
print("/n array" +str(mc)+"row column:")
row,column=map(int,input().split())
if(len(array_1)!=(row*column)):
 print("/n row&column size not match with total element!! retry")
return  create_matrix(mc)
array_1=array_1.reshape(row,column)
print("/n array"+str(mc))
print(array_1)
print("\n inverse")
return array_1
print(np.linalg.inv(create_matrix(1)))
    