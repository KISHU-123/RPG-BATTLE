class circle:
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        return 3.14*self.radius*self.radius
    def getcircumference(self):
        return 2*3.14*self.radius

ob = circle()
x= int(input("enter the radius"))
print("the radius is ",x)
print("the area and circumference are ",ob.getarea,ob.getcircumference ,"respectively")