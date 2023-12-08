# Outputs the momentum 

# Inputs =>
            # i)mass(kg)
            # ii)velocity(m/s)
            
# Outputs => momentum

mass  = float (input('Enter mass of body:'))
velocity = float (input('Enter the velocity of body:'))

momentum = mass * velocity

kEnergy  = 1/2 * mass * velocity ** 2

def fmomentum(x,y):
    return (f'The momentum of this body is {momentum:.2f}\n While the momentum is {kEnergy:.2f}')

print(fmomentum(mass,velocity))
