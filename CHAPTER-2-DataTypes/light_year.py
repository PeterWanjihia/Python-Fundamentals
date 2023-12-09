#  A program that calculates and displays the value of a light year 

# Calculate light year value
# Display light year value

# Distance = speed * time 
        #   = speed * (Number of seconds in a year)
# dailyHours = 24 
# speed_of_light = 3 * 10 ** 8
# seconds_in_day = 3600 * 24 

# days_in_year = int(input('Enter the days in a year:'))

# seconds_in_year = seconds_in_day * days_in_year
        
# def results(seconds_in_year,speed_of_light):
#     light_year_distance = seconds_in_year * speed_of_light
#     return (f'The distance of a light year is {light_year_distance}')

# print(results(seconds_in_year,speed_of_light)) 

# Constants 
SPEED_OF_LIGHT = 3 * 10 ** 8
SECONDS_IN_DAY = 3600 * 24 

def calculate_light_year_distance(user_input_days):
    # calculate the distance of a light year
    seconds_in_year = SECONDS_IN_DAY * user_input_days
    light_year_distance = seconds_in_year * SPEED_OF_LIGHT
    return light_year_distance

def main():
    try:
        user_input_days = int(input('Enter the number of days in a year:'))
        light_year_distance  =  calculate_light_year_distance(user_input_days)
        print(f'The distance of a light_yaer is {light_year_distance}  meters away')
    except:
        print('Invalid input:Please enter a valid integer for the numberof days ')
        
        
        
if __name__ == '__main__':
    main()