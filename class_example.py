"""Class examples and patterns"""

class car():
    def fast(self):
        print("Go fast")
    
    def slow(self):
        print("Go slow") 

class drive():
   def __init__(self, accel, drv):
        self.acceleration = accel
        self.drift = drv   

class vw(car):
    def __init__(self, drive_obj):
        self.drive_obj = drive_obj

d = drive(10, 5)

k = vw(d)

k.fast()

print(k.drive_obj.acceleration, k.drive_obj.drift) 
