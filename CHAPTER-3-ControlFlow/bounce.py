# Calculate the distance travelled by a ball after successive bounces 
# Input => 
        # --->Initial height of the ball
        # --->Number of bounces of the ball
        
# Constants 
bouncing_index = 0.6 
initial_height = int(input('Enter the intial height of the ball:'))
number_of_bounces = int(input('Enter the number of bounces:'))


def calculate_distance(initial_height,number_of_bounces):
    total_distance = 0
    
    for  i in range(number_of_bounces):
        new_height = initial_height * bouncing_index
        distance = initial_height + new_height
        initial_height = new_height
        total_distance += distance
    return total_distance     
    
        
        
print(calculate_distance(initial_height,number_of_bounces))


