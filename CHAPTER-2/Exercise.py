#  SPHERE'S diameter , circumference, surface_area, volume

# Inputs : ==>
            # -Radius
            
# Outputs : ==>
            # -Diameter = (Radius*2)
            # -Cirmference =  math.pi * Radius*Radius
            # -volume  = 4/3(math.pi)* Radius^3
            # -surface_area =>4(maths.pi) * Radius ^2 
            
import math          
radius = float(input('Enter the radius of the Sphere:'))

def  outputs(radius):
        diameter = (radius*2)
        cirmference =  math.pi * radius ** 2
        volume  = 4/3 * math.pi* radius **  3
        surface_area = 4 * math.pi * radius ** 2
        return (f'The outputs are as follows \nVolume :{volume:.2f} \n diameter:{diameter:.2f} \n circumference:{cirmference:.2f}\n surface_area:{surface_area:.2f}')
    
print(outputs(radius))

