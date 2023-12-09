# The program outputs the nautical miles from an input of distance in km
#  total degree are 90  and each degree takes sixty minutes 
# each mile is the distance travelled in one minute 
# so the distance travelled in 60 minutes is 60 nautical miles 
#  we cover 60 nautical miles per degree so the total distance is 90 * 60

# But one km is 1/10000 of the total distance 



# therefore the  distance in km into nautical miles 

# Constants 
# TOTAL_DISTANCE = 90 * 60 
# KM = 1/10000 * TOTAL_DISTANCE

# def calculate_nautical_mile(kilometers):
#     # calculate the distance in nautical mile
#     kilometres = int(input('Enter the distance covered in kilometers:'))
#     nautical_miles = kilometers * KM
#     return (f'The nautical miles are {nautical_miles}')

# print(calculate_nautical_mile(34))

TOTAL_DISTANCE = 90 * 60 
CONVERSION_FACTOR = 1/10000 * TOTAL_DISTANCE

def calculate_nautical_mile(kilometers):
    # calculate the distance in nautical mile
    nautical_miles = kilometers * CONVERSION_FACTOR
    return f'The nautical miles are {nautical_miles}'

# Get user input for the distance in kilometers
user_input_kilometers = float(input('Enter the distance covered in kilometers:'))

# Call the function with user input
result = calculate_nautical_mile(user_input_kilometers)

# Print the result
print(result)