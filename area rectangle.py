class Rectangle:
    def __init__(self):
        self.l=int(input("enter the length:"))
        self.w=int(input("enter the width:"))
    def area(self):
        return self.l*self.w
    def __lt__(self,value):
        return(self.l*self.w)<(value.l*value.w)
r1=Rectangle()
print('Area1 =',r1.area())
print()
r2=Rectangle()
print('Area=',r2.area())
if r1<r2:
      print('\n Rectangle 1 is less than rectangle 2')
else:
      print('\n Rectangle 2 is less than rectangle 1')
      
      
                   
        
    
