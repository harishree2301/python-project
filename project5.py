num=[]
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
        new=[int(a) for a in num]
        
        if choice==1:
            num=input("Enter data for a 1D array(seperated by spaces):").split()
            print(num)
            
            print("Data has been stored successfully!")
           
        elif choice==2:
            print("Data Summary:")
            print("- Total elements:",len(num))
            print("- Minimum value:",min(num))
            print("- Maximum value:",max(num))
           

            print("-Sum All values :",sum(new))
            print("-Average value :",sum(new)/len(num))
            print()
        
        elif choice==3:
             def factorial(i):
                  if i<1:
                       return print("The number is not valid.")
                  if i==1:
                       return 1
                  return i*factorial(i-1)
             value=int(input("Enter a number to calculate its factorial:"))
             result=factorial(value)
             print(result)
             

        elif choice==4:
             val=input("Enter a Threshold value to filter out data above this value:")
             newnum=list(filter(lambda x:x>=val,num))
             print(f"Filtered Data (value >= {val})")
             print(newnum)
             
        elif choice==5:
             print("Choose sorting option:")
             print("1. Ascending")
             print("2. Descending")

             sort=int(input("Enter your choice:"))


             if sort==1:
                  num.sort()
                  print("Sorted Data in Ascending Order:")
                  print(num)
             elif sort==2:
                  num.sort(reverse=True)
                  print("Sorted Data in Descending Order:")
                  print(num)
             else:
                  print("Choice is incorrect.")
             
        elif choice==6:
             print("Data Statistics :")
             print()
             print("- Minimum value:", min(num))
             print("- Maximun value:",max(num))
             print("- Sum of the ALL value:",sum(new))
             print("- Average Value:",sum(new)/len(num))
        elif choice==7: 
             print("Thank you for using the Data Analyzer and Transformer Program.Goodbye!")   
             break
        else:
             print("Choice is incorrect") 


              
