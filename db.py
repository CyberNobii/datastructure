
def insertion():
    user_input1=int(input("Enter the element to insert :"))
    data.append(user_input1)
    print("Data Inserted")
    
def deletion():
    print(data)
    user_input2=int(input("Enter element to delete :"))
    if user_input2 in data:
        data.remove(user_input2)
    else:
        print("Element not found")

def searching():
    user_input3=int(input("Enter the element to search :"))
    if user_input3 in data:
        s=data.index(user_input3)
        print("Data present at ",s)
    else:
        print("Element not found")

def traversaling():
    if data:
        print("Current data is ",data)
    else:
        print("Data list is empty !!")

def sorting():
    data.sort()
    print("Data sorted succesfully")
    print("Sorted list :",data)

def merging():
    n=int(input("Enter the number of data :"))
    new_list=[]
    for i in range(n):
        element=int(input("enter the data :"))
        new_list.append(element)
        print("element added succesfully")
    data.extend(new_list)
    print("Elemnt extended sucessfuly")


data=[]

while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Travers")
    print("5. Sort")
    print("6. Merg")
    print("7. Exit")
    ch=int(input("Enter Your Choice :"))

    if ch==1:
        insertion()
    elif ch==2:
        deletion()
    elif ch==3:
        searching()
    elif ch==4:
        traversaling()
    elif ch==5:
        sorting()
    elif ch==6:
        merging()
    elif ch==7:
        print("Exiting..")
        break
    else:
        print("Invalid Choice !!")
