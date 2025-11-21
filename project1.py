num=[]        
def inputData():
    global new
    print()
    num=input("Enter data for a 1D array(seperated by spaces):").split()
    new=[int(a) for a in num]
    print(new)
    print("Data has been stored successfully!")   

def displayData():
    print("Data Summary:")
    print("- Total elements:",len(new))
    print("- Minimum value:",min(new))
    print("- Maximum value:",max(new))
    print("-Sum All values :",sum(new))
    print("-Average value :",sum(new)/len(new))
    print()  
def factorial(i):
    global result
    if i<1:
        return print("The number is not valid.")
    if i==1:
        return 1
    return i*factorial(i-1)
def threshold():
        val=int(input("Enter a Threshold value to filter out data above this value:"))
        newnum=list(filter(lambda x:x>=val,new))
        print(f"Filtered Data (value >= {val})")
        print(newnum) 

def sortData():
    print("Choose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    sort=int(input("Enter your choice:"))
    if sort==1:
        new.sort()
        print("Sorted Data in Ascending Order:")
        print(new)
    elif sort==2:
        new.sort(reverse=True)
        print("Sorted Data in Descending Order:")
        print(new)
    else:
        print("Choice is incorrect.") 

def statistics():
    print("Data Statistics :")
    print()
    print("- Minimum value:", min(new))
    print("- Maximun value:",max(new))
    print("- Sum of the ALL value:",sum(new))
    print("- Average Value:",sum(new)/len(new))  

def exit():
    print("Thank you for using the Data Analyzer and Transformer Program.Goodbye!")   
 
def invalid():
     print("Choice is incorrect") 

while True:
    print("Welcome to the Data Analyzer and Transformer Program")
    print()
    print("Main Menu:")
    print("1. Input Data ")
    print("2. Display Data Summary (Built-in-Functions)")
    print("3. Calculator Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice=int(input("Please enter your choice:"))
    
    if choice==1:
        inputData()

    elif choice==2:
        displayData()

    elif choice==3:
        value=int(input("Enter a number to calculate its factorial:"))
        result=factorial(value)
        print(result)
        factorial(value) 

    elif choice==4:
        threshold() 

    elif choice==5:
        sortData() 

    elif choice==6:
        statistics()

    elif choice==7: 
        exit()
        break    
    else:
        invalid()

