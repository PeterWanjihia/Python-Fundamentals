# Enter all sides of a triangle
# Check whether  the triangle is equilateral or not


s1 = float(input('Enter the length of  side 1:'))
s2 = float(input('Enter the length of  side 2:'))
s3 = float(input('Enter the length of  side 3:'))


# Checking 
def check_triangle(s1,s2,s3):
    if s1==s2 and s2 == s3 and s3 == s1:
        return('Equilateral triangle')
    else:
        return('Not Equilateral triangle')
    
print(check_triangle(s1,s2,s3))
    
