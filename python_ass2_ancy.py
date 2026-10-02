import numpy as np
import pandas as pd
print("1...........................................................")

array1=np.array([1,2,3,4,5,6,7,8,9,10])
array2=array1.reshape(2,5)
print(array2)
print("2...........................................................")
array3=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(array3[5:15])
print("3............................................................")

print(np.mean(array1))
print(np.median(array1))
print(np.std(array1))
print("4............................................................")

x=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
y=np.array([1,2,3,7])
z=x-y
print(z)

print(".5...........................................................")

import pandas as pd
from google.colab import files

data={'Name': ['Anu','Rinu','John','Mariya','Suraj','Mariam','Jeeva','James','Noha','Hazel'],'Age':[20,21,35,22,37,28,21,20,21,20],'gender':['male','female','female','male','female',
               'male','female','male','male','female']}
df=pd.DataFrame(data)
df['Occupation']=['Programmer','Manager','Analyst','Programmer','Manager','Analyst','Programmer','Manager','Analyst','Programmer']
print(df)
print(df[df['Age']>=30])
print("...................................")

df.to_csv('students.csv')
files.download('students.csv')
data1 = pd.read_csv('students.csv',index_col=0)
data1
print("..................................")


