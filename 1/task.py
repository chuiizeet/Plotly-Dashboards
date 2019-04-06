import numpy as np
import pandas as pd

np.random.seed(101)

mat = np.random.randint(1,101,(100,5))
print(mat)

df = pd.DataFrame(mat, columns=['f1','f2','f3','f4','label'])
print(df)

random_numbers = np.random.randint(0,100,(50,4))
df = pd.DataFrame(data=random_numbers, columns=['A','B','C','D'])
print(df)
