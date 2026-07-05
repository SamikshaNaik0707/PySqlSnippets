   
#Task 1: Build the employee directory DataFrame
#using a Dictionary of Lists.     
#Task 2: Build the exact same DataFrame again
#using a List of Lists.       
#Task 3: Run .shape
#and .dtypes on your result to confirm
# it looks correct.

# Task 1 Build the employee directory DataFrame using a Dictionary of Lists.

import pandas as pd
emp_info={
    'Eame':['Shrikant','Durvang','Ashwin'],
    'Age':['42','24','38'],
    'City':['Pune','Mumbai','Surat']
}

df_dict=pd.DataFrame(emp_info)
print("This is a Dataframe using Dictionary:")
print(df_dict)
print('**************************')

#Task 3 Run .shape and .dtypes on your result to confirm it looks correct.

df_dshape=(df_dict.shape)
print('The shape of dataframe is:',df_dshape)
print('**************************')
df_data_type=(df_dict.dtypes)
print('The datatypes are:',df_data_type)

#Task 2 Build the exact same DataFrame again using a List of Lists. 

emp_details=[['Swapnil','42','Bangluru'],
             ['Kishor','42','Raipur'],
             ['Swayam','26','Hyderabad']]
columns=['Name','Age','City']

df_list=pd.DataFrame(emp_details,columns=columns)
print('**************************')
print("This is a Dataframe using List:")
print(df_list)
print('**************************')

#Task 3 Run .shape and .dtypes on your result to confirm it looks correct.

df_lshape=(df_list.shape)
print('The shape of dataframe is:',df_lshape)
print('**************************')
df_ldata_type=(df_list.dtypes)
print('The datatypes are:',df_ldata_type)
