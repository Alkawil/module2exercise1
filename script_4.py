total_sum = 0
for i in range(1,6):
    while True:
        try:
            x = int(input("Enter int #{}:" .format(i)))
            total_sum = total_sum + x
            break
        except ValueError:
            print("Invalid input. Please enter a int.")
            continue       
print("Your sum is",total_sum)
# initializing the sum to calculate to be 0.Passing in a for loop ranging from 1 to 6 for the users to enter  integers.
# we are using a while loop which breaks if valid integer is given by the user.Each time the user enters a valid integer we are adding it up to the total_sum which calculates the sum at the end.If by any chance the user enters and invalid integer like float,double,string etc,the try block will be skipped and it enters the except block for the further execution and printing out an error statement.It will print out this error statement until the user enters 5 valid integers.After entering 5 integers it will come out of the while loop and print out the sum of the entered 5 integers.
#https://python-course.eu/python-tutorial/errors-and-exception-handling.php