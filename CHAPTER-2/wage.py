# Constants
HOURLY_WAGE = float(input('Input the hourly wage:'))

OVERTIME_WAGE = 1.5 * HOURLY_WAGE
try:
    hoursWorked = float(input('Enter the number of hours:'))
    overtimeHours = float(input('Enter  the number of OT hours:'))

    def calculatePay(hoursWorked,overtimeHours,HOURLY_WAGE,OVERTIME_WAGE):
        
        total_pay =  hoursWorked * HOURLY_WAGE + overtimeHours * OVERTIME_WAGE
        
        return (f'The total pay is {total_pay}')

    print(calculatePay(hoursWorked,overtimeHours,HOURLY_WAGE,OVERTIME_WAGE))
    
except ValueError:
    print('Invalid input. Please enter valid numerical values for hours and overtime hours.')