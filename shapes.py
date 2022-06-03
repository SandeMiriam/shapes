#Class Circle
#A Circle instance accepts attribute radius (r)
#It has a method area that returns the area (A) of the circle using the formula A=πr2
#It has a method to calculate circumference (c) using the formula C=2πr
from msilib.schema import Class


class Circle:
    def __init__(self,r):
        self.r=r
   
   
    def area(self):
        A=3.142*self.r*self.r
        return A
        
    def circumference(self):
        C=(3.142*2*self.r)
        return C


#Class Square
#A Square instance accepts the attribute side (a)
#It has method area that returns the area (A) of the square using the formula A=a2
#It has a method to calculate the perimeter (P) of the square using the formula P=4a

class Square:
   
    def __init__(self,a):
        self.a=a

    def area(self):
        A=a*self.a
        return A

    def perimeter(self):
        P=4*self.a
        return P
      #Class Rectangle
#A Rectangle instance accepts two sides of a rectangle (w,l)
#It has method to calculate the area (A) of the rectangle using the formula A=wl
#It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w) 

class Rectangle:
    def __init__(self,l,w):
     self.l=l
     self.w=w
     
    def area(self):
        A=self.l*self.w
        return A

    def perimeter(self):
        P=2(self.l + self.w)
        return P

 
#Class Sphere
#A Sphere Instance accepts the radius of the sphere (r)
#It has a method to calculate the surface area (A) using the formula A=4πr2
#It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class Sphere:
    def __init__(self,r):
        self.r=r
    
    def sa(self):
        A=4*3.142*self.r*self.r
        return

    def volume(self):
        V=(4/3)*(3.142*self.r**3)
        return V

