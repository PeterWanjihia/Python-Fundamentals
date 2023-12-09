# Allow the sides of a triangle as input

def is_right_triangle(hypotenuse,adjacent,base):
    if hypotenuse <= 0  or adjacent<= 0 or base <= 0:
        return False  # All sides must be positive
    
    if hypotenuse ** 2 == adjacent ** 2 + base ** 2:
        return True  #The pythagorean theorem
    else:
        return False
    
def main():
    try:
        hypotenuse = float(input('Enter the length of the hypotenuse: '))
        adjacent = float(input('Enter the length of the adjacent side: '))
        base = float(input('Enter the length of the base side: '))
        
        
        if is_right_triangle(hypotenuse, adjacent, base):
            print('This is a right-angled triangle')
        else:
            print('This is not a right-angled triangle')
    except ValueError:
            print('Invalid input. Please enter valid numerical values.')
            
            
if __name__ == '__main__':
    main()



    
        