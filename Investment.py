"""
Program:Investment.py
Author:Peter Wanjihia

Compute an invetment report.

1.The inputs are :
    starting investment amount
    number of years
    interest rate in percentage
    
2.The report is displayed in tabular form with a header

3.Computation and outputs:
    for each year 
        compute the interest and add it to the investment
        print a formatted row of results for that years
        
4.The ending investment and interest are also displayed         
"""

# Initialize the inputs
startBalance = int(input("Enter the investment amount:"))
years = int(input("Enter the number of years:"))
rate = int(input("Enter the interest as %:"))

# Convert the rate to a decimal number
rate = rate / 100.00

#Initialize the accumulator for the interest
totalInterest = 0.0

# Display the header for the table
print ("%4s%18s%10s%16s" %('Year','Starting Balance','Interest','Ending Balance'))

# Compute and display the results for each year
for year in range(1,years+1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print("%4d%18.2f%10.2f%16.2f" %(year ,startBalance,interest,endBalance))
    startBalance = endBalance
    totalInterest += interest

# Display the totals for the period  
print ("Ending balance: %0.2f" % endBalance)
print("Total interest earned: %0.3f" % totalInterest)    