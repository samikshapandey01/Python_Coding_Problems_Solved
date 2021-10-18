import numpy as np
import pandas as pd

file_nm=input("Enter name for csv file")

eq=pd.read_csv(file_nm,header=None)


#Linear equations can be written in form Ax=b, where A is matrix of coefficients and x is matrix of variables.
#In csv file last row is b matrix.Converting rest of the data(except last column in csv file) to numpy matrix
A=np.array(eq.iloc[:,0:-1])

print("Matrix A:")
print(A)

#b matrix is last column in csv file.
b=np.array(eq.iloc[:,-1])
print("\nMatrix b:")
print(b)

#Function to solve linear equations with matrix A and b as input arguments
def solve(A,b):
    det=round(np.linalg.det(A),2)#determinant of A matrix
    if det!=0:#determinant is 0 for singular matrix
        inva = np.linalg.inv(A)
        x=inva@b #x=Ainverse dot b
        print("Solution x:")
        print(x)
        ct=1
        for i in x:
            x='x'+f'{ct}'
            print(f"{x}={i}")
            ct+=1
    else:
        print("No Solution as determinant of A is 0")

#A should be a square matrix for unique solutions
x,y=A.shape
b_s=b.shape[0]
if x==y:
    print("\nNo. of rows and columns in A matrix:",x,y)
    print("A is a square matrix\n")
    if x==b_s: #check if rows in A and b are same
        solve(A,b)#Call function to solve the equations with matrix A and b
    else:
        print("Matrix b is different shape than matrix A")
else:
    print("\nA is not a square matrix,hence unique solution doesnt exists")
    
 