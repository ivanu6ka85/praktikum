#class Rectangle:
#    def __init__(self, width, height):
#        self.width=width
#        self.height=height

#    def getWidth(self):
#        return self.width

#    def getHeight(self):
#        return self.height

#    def getArea(self):
#        return self.width*self.height
class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def get_area(self):
        return self.a*self.b

class Square:
    def __init__(self,a):
        self.a =a
    def get_area_square(self):
        return self.a ** 2

class Circle:
    def __init__(self,r):
        self.r = r

    def get_area_square_circle(self):
        return self.r **2 * 3.14

