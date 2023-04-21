import pandas as pd
import numpy as np
def main():
    print("Welcome to the program")
    df=read_csv(n=input("which file you want to read: "))
    print(df)
    pc=per_to_int(df)
    df_h,df_t=csv_divide(df,pc)
    x,y=column_drop(df)
    x_train,y_train=train_data(df_h,x,y)
    x_test,y_test=test_data(df_t,x,y)

#READ THE CSV FILE
def read_csv(n):
    return pd.read_csv(n) #READING THE FILE AND RETURNING IT'S VALUE

#PROGRAM TO DIVIDE THE DATA ON THE BASIS OF PERCENTAGE INPUT GIVEN INTO 2 PARTS NAMELY HEAD AND TAIL   
def csv_divide(df,per):
    ln=len(df)
    df_h=df.head(pc) #UPPER PART OF THE DATA
    df_t=df.tail(ln-pc) #LOWER PART OF THE DATA
    return df_h, df_t  #RETURNING THE DIVIDED DATA

#PROGRAM TO FROP THE COLUMN WHICH CONTAINS STRING VALUES
def column_drop(df):
    c=df.columns.tolist()
    dtype=df.dtypes.to_dict()
    for i in dtype:
        if dtype[i]==object:
            c.remove(i)
    x=[]
    y=[]
    x.append(c[len(c)-1])
    y.append(c[0:len(c)-1])
    return x,y  #RETURNING THE LIST OF COLUMNS 
    
#PROGRAM TO CONVERT PERCENTAGE INTO INTEGER FORM AND RETURN THE VALUE
def per_to_int(df):
    p=input("Enter the percentage of data you want to train: ")
    p=int(p.replace("%",""))
    ln=len(df)
    pc=int((c/100)*ln)
    return pc

#PROGRAM TO ACQUIRE DATA FOR TRAINING IN NUMPY FORM
def train_data(df_h,x,y):
    
    listx=df_h[x].to_numpy()
    listy=df_h[y[0]].to_numpy()
    
    return listx,listy

#PROGRAM TO AQUIRE DATA FOR TESTING IN NUMPY FORM
def test_data(df_t,x,y):
    
    listx=df_t[x].to_numpy()
    listy=df_t[y[0]].to_numpy()
    
    return listx,listy




if __name__ == "__main__":
    main()