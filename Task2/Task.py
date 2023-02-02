import pandas as pd
#read data from a csv
def reader_csv(str):
    dataa =pd.read_csv(str)
    print(dataa)

def desc(df,n):
    #First calculating mean
    mean_m=df["Maths Marks"]
    mean_c=df["Chemistry Marks"]
    mean_p=df["Physics Marks"]
    maths_t=0
    phy_t=0
    chem_t=0
    mm=[]
    cc=[]
    pp=[]


    for i in range(1,n):
        maths_t+=mean_m[i]
        chem_t+=mean_c[i]
        phy_t+=mean_p[i]
        m_mean=maths_t/n
        c_mean=chem_t/n
        p_mean=phy_t/n

    #calculating minimum
    for i in mean_m:
        mm.append(i)
        mm.sort()
        mm_min=mm[0]
        mm_max=mm[-1]
    for i in mean_c:
        cc.append(i)
        cc.sort()
        cc_min=cc[0]
        cc_max=cc[-1]
    for i in mean_p:
        pp.append(i)
        pp.sort()
        pp_min=pp[0]
        pp_max=pp[-1]


    category=["count","mean","max","min"]
    maths_dd=[n,m_mean,mm_max,mm_min]
    chem_dd=[n,c_mean,cc_max,cc_min]
    phy_dd=[n,p_mean,pp_max,pp_min]


    ddff={"":category,"Maths":maths_dd,"Physics":phy_dd,"Chemistry":chem_dd}
    dff=pd.DataFrame(ddff,index=range(1,5)) 
    print(dff)



#input data 
def data_input(n):
    lname=[]
    lmaths=[]
    lchem=[]
    lphy=[]
    remarks=[]
    for i in range(0,n):
        name=input("Enter name of Student")
        while True:
            if any(char.isdigit() for char in name):
                print("Enter a suitable input Integers are not allowed")
                name=input("Enter name of Student")
            else:
                break
        while True:
            try:
                maths=int(input("Enter Marks in Maths"))
            except ValueError:
                print("Error:Enter in Integer")
            else:
                break
        while True:
            try:
                chem=int(input("Enter Marks in Chemistry"))
            except ValueError:
                print("Error:Enter in Integer")
            else:
                break          
        while True:
            try:
                phy=int(input("Enter Marks in Physics"))
            except ValueError:
                print("Error:Enter in Integer")
            else:
                break      
        z=(maths+chem+phy)/3
        if z>90:
            remarks.append("Oustanding")
        elif  80<=z<90:
            remarks.append("Great")
        elif 70<=z<80:
            remarks.append("Good")
        else:
            remarks.append("Improve")
        lname.append(name)
        lmaths.append(maths)
        lchem.append(chem)
        lphy.append(phy)
    ser={"Names":lname,"Maths Marks":lmaths,"Chemistry Marks":lchem,"Physics Marks":lphy,"Remarks":remarks}
    df=pd.DataFrame(ser,index=range(1,n+1))
    print(df)
    #asking whether you want to create a user file
    decision=input("Do you want to input this data into a csv file?(Y/N) ")
    while True:
        if decision=="Y":
            str1=input("Enter the name of file: ")
            df.to_csv(str1)
            break
        elif decision=="N":
            print("not inputting the data")
            break
        else:
            print("Wrong output")
    decision2=input("Calculate the describe() of the data")
    while True:
        if decision2=="Y":
            desc(df,n)
            break
        elif decision2=="N":
            print("not inputting the data")
            break
        else:
            print("Wrong output")



user_name=input('''Welcome to program to enter Student's marks
What's Your Name?:''')

print(f"Hello {user_name}")

while True:
    print('''Choose the operation you want to perform
    1-Enter Student's Data
    2-Import a csv
    3-Exit the program''')

    ch=int(input("Enter your choice"))

    if ch==1:
        n=int(input("Enter the number of data of students to be entered"))
        data_input(n)
        

    elif ch==2:
        str=input("enter the name of csv file")
        reader_csv(str)

    elif ch==3:
        break

    else:
        ("print wrong output")
